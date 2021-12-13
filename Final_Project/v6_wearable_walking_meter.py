from __future__ import print_function
from datetime import datetime
import math
import sys
import time
import os
import paho.mqtt.client as mqtt
import uuid
import board
import adafruit_mpu6050
import qwiic_led_stick

## Level color Configuration
levels = [
    [255, 255, 255], # level 0 - white
    [255, 255, 0], # level 1 - yellow
    [0, 255, 0], # level 2 - green
    [0, 255, 255], # level 3 - cyan
    [0, 0, 255], # 4 - blue
    [255, 0, 255], # 5 - magenta
    [255, 0, 0], # 6 - red
    [127, 0, 255], # 7 - purple
    [255, 127, 0], # 8 - orange
    [127, 255, 0], # 9 - neon green
]

# initial state
level = 0
progress = 0
name = "husky"
lumineers = ["jumpluff", "sneasel"] # THIS IS HARDCODED
day = datetime.now().strftime("%d")
print("today is day: ", day)

# Accelerometer Setup
i2c = board.I2C() 
mpu = adafruit_mpu6050.MPU6050(i2c)

### LED Setup
stick = qwiic_led_stick.QwiicLEDStick()

if stick.begin() == False: print("Qwiic LED Stick err", file=sys.stderr)
stick.LED_off() 
stick.set_all_LED_brightness(31)

# MQTT Setup
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic + '/jumpluff') # THIS IS HARDCODED
    client.subscribe(topic + '/sneasel') # THIS IS HARDCODED
    client.subscribe(topic + '/increase') 
    client.subscribe(topic + '/reset') 
    client.subscribe(topic + '/levelup') 
def on_message(client, userdata, message):
    global level
    global progress
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    topic = os.path.basename(os.path.normpath(message.topic))
    print("topic is: ", topic)
    # for demo purposes
    if (topic == "levelup"):
        for i in range(9):
            level = i+1
            party(2000)
            showProgress()
            time.sleep(3)
    
    # for demo purposes
    if (topic == "increase"):
        level = 0
        progress = 10
        for i in range(progress):
            stick.set_single_LED_color(i, levels[level][0], levels[level][1], levels[level][2])
            time.sleep(2)
        level = 1
    # for demo purposes
    if (topic == "reset"):
        level = 0
        progress = 0
    if (topic in lumineers):
        # can only advance if we've completed the first level
        if (level >= 1 or progress == 10):
            party(10000)
            if level < 9: level += 1 # maximum of 10 levels for now
            # lumineers.remove(lumineer)
            print("A Lumineer has succeeded! You are now level: ", level)
        else: print("A Lumineer succeeded, but you were not ready to advance. p:", progress, ", l: ", level)

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
topic = 'IDD/jtc268/Lumineer'
client.on_connect=on_connect
client.on_message=on_message 
client.connect('farlab.infosci.cornell.edu', port=8883)

# LED Logic
## walking_rainbow from https://qwiic-led-stick-py.readthedocs.io/en/latest/ex8.html
def walking_rainbow(LED_stick, rainbow_length, LED_length, delay):
    red_array = [None] * LED_length
    blue_array = [None] * LED_length
    green_array = [None] * LED_length

    for j in range(0, rainbow_length):
        for i in range(0, LED_length):
            # There are n colors generated for the rainbow
            # The value of n determines which color is generated at each pixel
            n = i + 1 - j
            # Loop n so that it is always between 1 and rainbow_length
            if n <= 0:
                n = n + rainbow_length
            # The nth color is between red and yellow
            if n <= math.floor(rainbow_length / 6):
                red_array[i] = 255
                green_array[i] = int(math.floor(6 * 255 / rainbow_length * n))
                blue_array[i] = 0
            # The nth color is between yellow and green
            elif n <= math.floor(rainbow_length / 3):
                red_array[i] = int(math.floor(510 - 6 * 255 / rainbow_length * n))
                green_array[i] = 255
                blue_array[i] = 0
            # The nth color is between green and cyan
            elif n <= math.floor(rainbow_length / 2):
                red_array[i] = 0
                green_array[i] = 255
                blue_array[i] = int(math.floor(6 * 255 / rainbow_length * n - 510))
            # The nth color is between blue and magenta
            elif n <= math.floor(5 * rainbow_length / 6):
                red_array[i] = int(math.floor(6 * 255 / rainbow_length * n - 1020))
                green_array[i] = 0
                blue_array[i] = 255
            # The nth color is between magenta and red
            else:
                red_array[i] = 255
                green_array[i] = 0
                blue_array[i] = int(math.floor(1530 - (6 *255 / rainbow_length * n)))
        # Set all the LEDs to the color values according to the arrays
        LED_stick.set_all_LED_unique_color(red_array, green_array, blue_array, LED_length)
        time.sleep(delay)

## party(int partyTime): party mode
def party(partyTime):
    startTime = round(time.time() * 1000)
    while(round(time.time() * 1000) - startTime < partyTime):
      walking_rainbow(stick, 20, 10, 0.1)
      
def showProgress():
    global level
    global progress
    for i in range(progress):
      stick.set_single_LED_color(i, levels[level][0], levels[level][1], levels[level][2])
      time.sleep(0.1)

# Game Loop
while True:
    # show lights based on status
    showProgress()

    # if new day, reinstantiate player
    if day != datetime.now().strftime("%d"):
        level = 0
        progress = 0
        # lumineers = []
        print("New day. Stats reset.")
    
    # check accelerometer for progress
    if (progress < 10) and (mpu.acceleration[0] < 1):
       progress += 1
       print("Progress: ", progress)

    # check if we have completed the entry level
    if (level == 0) and (progress == 10):
        level += 1
        client.publish(topic + '/' + name, 'completed')
        # post to MQTT
        print("Completed the Entry Level")
        
    client.loop(.1)

