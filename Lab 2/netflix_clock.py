from time import strftime, sleep, time
from datetime import datetime
import subprocess
import digitalio
import board
import textwrap
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
smallerFont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

halfSecondCost = .0000017361
totalCost = 0.00

while True:
    # Draw a Netflix red filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(229, 9, 20))

    # Netflix
    totalCost += halfSecondCost
    
    # Get 25 decimal places
    totalCostAsString = '{:.25f}'.format(totalCost)
    print(totalCostAsString)
    
    # Wrap the text for exta intensity
    totalCostSplit = textwrap.wrap(totalCostAsString, 9)
         
    y = top
    draw.text((x + 5, y + 10), "Netflix Damage", font=smallerFont, fill="#FFFFFF")
    draw.text((x + 20, y + 45), "$" + totalCostSplit[0], font=font, fill="#FFFFFF")
    draw.text((x + 35, y + 72), totalCostSplit[1], font=font, fill="#FFFFFF")
    draw.text((x + 35, y + 99), totalCostSplit[2], font=font, fill="#FFFFFF")
    
    
    # Display image.
    disp.image(image, rotation)
    
    # Increment every .5 seconds
    sleep(.5 - time() % .5)
