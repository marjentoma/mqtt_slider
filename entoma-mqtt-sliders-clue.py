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
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(temp["slider/xccelerometer"] , temp["slider/yccelerometer"], temp["slider/zccelerometer"])
    clue_data[1].text = "Gyro: {} {} {} dps".format(temp["slider/xgyroscope"], temp["slider/ygyroscope"] , temp["slider/zgyroscope"])
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(temp["slider/xmagnetic"], temp["slider/ymagnetic"], temp["slider/zmagnetic"])
    clue_data[3].text = "Pressure: {} hPa".format(temp["slider/pressure"])
    clue_data[4].text = "Altitude: {:.0f} m".format(temp["slider/light"])
    clue_data[5].text = "Temperature: {} C".format(temp["slider/temperature"])
    clue_data[6].text = "Humidity: {} %".format(temp["slider/humidity"])
    clue_data[7].text = "Proximity: {}".format(temp["slider/proximity"])
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(temp["slider/red"], temp["slider/green"], temp["slider/blue"], temp["slider/light"])
    clue_data.show()
sensor = {
    "slider/xccelerometer" :0,
    "slider/yccelerometer" : 0,
    "slider/zccelerometer" :0,
    "slider/xgyroscope" :0,
    "slider/ygyroscope" :0,
    "slider/zgyroscope" :0,
    "slider/xmagnetic" :0,
    "slider/ymagnetic" :0,
    "slider/zmagnetic" :0,
    "slider/pressure" :0,
    "slider/temperature" :0,
    "slider/humidity" :0,
    "slider/red" :0,
    "slider/green" :0,
    "slider/blue" :0,
    "slider/proximity" :0,
    "slider/light" :0,
}

# this function holds the condition  if rc is equal to 0 then the client will subscribe then after it will display the text
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("slider/#")
        display_text(sensor)

# this function  holds the messages or the payload
def on_message(client, userdata, msg):
    display_text(int(msg.payload.decode()))

clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(text_scale=2) 

client = mqtt.Client()
client.on_connect = on_connect #calling the function on_connect above
client.on_message = on_message #calling the function on_message above

client.connect("mqtt.eclipseprojects.io", 1883, 60) #connect to the browser

client.loop_forever() #loop forever