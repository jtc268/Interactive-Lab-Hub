from time import strftime, sleep
from datetime import datetime
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a Netflix red filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(229, 9, 20))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
smallerFont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

monthlyCost = 8.99
totalCost = 0.00

while True:
    # Draw a Netflix red filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(229, 9, 20))

    # Netflix
    today = datetime.now()
        
    # Check for first of month - Uncomment when ready for production
    #
    # if today.day == 1:
    #     totalCost += monthlyCost
    #     print(str(totalCost))
        
    # Demo: 5 second timer - Remove before shipping
    if ((today.second % 5) == 0):
        totalCost += monthlyCost
        print(str(totalCost))
        
    y = top
    draw.text((x + 10, y + 10), "Netflixes", font=smallerFont, fill="#FFFFFF")
    draw.text((x + 35, y + 45), "$" + str(totalCost), font=font, fill="#FFFFFF")
    
    
    # Display image.
    disp.image(image, rotation)
    sleep(1)
