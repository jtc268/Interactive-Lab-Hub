import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/joe/captest'

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    if mpr121[10].value:
        val = f"Doge was touched!"
        print(val)
        client.publish(topic, val)
    if mpr121[6].value:
        val = f"Grogu was touched!"
        print(val)
        client.publish(topic, val)
    time.sleep(0.25)
