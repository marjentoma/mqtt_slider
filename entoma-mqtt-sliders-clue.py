"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt

def display_text(temp):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*(temp["clueSlider/accelXRange"], temp["clueSlider/accelYRange"], temp["clueSlider/accelZRange"]))
    clue_data[1].text = "Gyro: {} {} {} dps".format(*(temp["clueSlider/gyroXRange"], temp["clueSlider/gyroYRange"], temp["clueSlider/gyroZRange"]))
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*(temp["clueSlider/magneticXRange"], temp["clueSlider/magneticYRange"], temp["clueSlider/magneticZRange"]))
    clue_data[3].text = "Pressure: {} hPa".format(temp["clueSlider/pressureRange"])
    clue_data[4].text = "Temperature: {} C".format(temp["clueSlider/tempRange"])
    clue_data[5].text = "Humidity: {} %".format(temp["clueSlider/humidityRange"])
    clue_data[6].text = "Proximity: {}".format(temp["clueSlider/proximityRange"])
    clue_data[7].text = "Color: R:{}G:{}B:{}C:{}".format(*(temp["clueSlider/colorRRange"], temp["clueSlider/colorGRange"], temp["clueSlider/colorBRange"], temp["clueSlider/colorCRange"]))
    clue_data.show()

sensor = {
    "clueSlider/accelXRange" : 0,
    "clueSlider/accelYRange" : 0,
    "clueSlider/accelZRange" : 0,
    "clueSlider/gyroXRange" : 0,
    "clueSlider/gyroYRange" : 0,
    "clueSlider/gyroZRange" : 0,
    "clueSlider/magneticXRange" : 0,
    "clueSlider/magneticYRange" : 0,
    "clueSlider/magneticZRange" : 0,
    "clueSlider/pressureRange" : clue.pressure,
    "clueSlider/tempRange" : clue.temperature,
    "clueSlider/humidityRange" : clue.humidity,
    "clueSlider/proximityRange" : clue.proximity,
    "clueSlider/colorRRange" : 0,
    "clueSlider/colorGRange" : 0,
    "clueSlider/colorBRange" : 0,
    "clueSlider/colorCRange" : 0
}

# this function holds the condition  if rc is equal to 0 then the client will subscribe then after it will display the text
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clueSlider/#")
        display_text(sensor)

# this function  holds the messages or the payload
def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload.decode())
    sensor[msg.topic]= msg.payload.decode()
    display_text(sensor)

clue_data = clue.simple_text_display(text_scale=2) 

client = mqtt.Client()
client.on_connect = on_connect #calling the function on_connect above
client.on_message = on_message #calling the function on_message above

client.connect("mqtt.eclipseprojects.io", 1883, 60) #connect to the browser

client.loop_forever() #loop forever