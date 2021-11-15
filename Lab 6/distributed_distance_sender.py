import time
import board
import busio
import qwiic
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/joe/test/distance'
topic_cap = 'IDD/joe/test/cap'

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

while True:
    try:
        if mpr121[10].value:
            val = f"Dogecoin was touched!"
            print(val)
            client.publish(topic_cap, val)
        if mpr121[6].value:
            val = f"Coin was touched!"
            print(val)
            client.publish(topic_cap, val)
        ToF.start_ranging()# Write configuration bytes to initiate measurement
        time.sleep(.005)
        distance = ToF.get_distance() # Get the result of the measurement from the sensor
        time.sleep(.005)
        ToF.stop_ranging()
        distanceInches = distance / 25.4
        
        if (distance > 45):
            val = "Bagon is " + str(distance) + "mm from the Pokeball trap!"
            print(val)
            client.publish(topic, val)
        else:
            val = "Bagon is ready to catch!"
            print(val)
            client.publish(topic, val)

    except Exception as e:
        print(e)
