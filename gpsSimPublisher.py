import paho.mqtt.client as mqtt
import json
import time

mqttBroker ="test.mosquitto.org"
c_id = "theSensorSimulatorSquare" + str(int(time.time())) + "88"
client = mqtt.Client (client_id=c_id, clean_session=True)
client.connect(mqttBroker, port=1883)

mqttTopic = "XXXXXXXXXX"

with open("sample.json", 'r') as jsonFile:
    desDataList = json.load(jsonFile)


i = 0
interval = 2
max = len(desDataList)
while True:
    if i < 3:
        buf = json.dumps(desDataList[i])
        client.publish(mqttTopic ,buf)
        i += 1
        time.sleep(2)
    else:
        i = 0   # Reset loop, send data from start
        time.sleep(10)
        
