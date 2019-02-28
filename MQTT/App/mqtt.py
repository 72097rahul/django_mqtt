from paho.mqtt import client as mqtt
import json
import time
from .views import get_data


def on_connect(client, userdata, flags, rc):
    client.subscribe("take/singgle",0)


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    data=json.loads(message)
    data = get_data(data)
    data= json.dumps(data)
    client.publish("data/out", data, 0)
    


client = mqtt.Client("rahul")
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.108",1883)

