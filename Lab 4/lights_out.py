import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont

import adafruit_ssd1306
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
mpr121 = adafruit_mpr121.MPR121(i2c)

WIDTH = 128
HEIGHT = 32

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

right = False;
left = False;

def drawRight():
    color = 0 if right else 255;
    draw.rectangle((0, 0, oled.width/2, oled.height), outline=color, fill=color)

def drawLeft():
    color = 0 if left else 255
    draw.rectangle((oled.width/2, 0, oled.width, oled.height), outline=color, fill=color)

while True:
    oled.image(image)
    oled.show()

    for i in range(12):
        if mpr121[i].value:
            if i == 6:
                right = not right
                drawRight()
            if i == 10:
                left = not left
                drawLeft()
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
