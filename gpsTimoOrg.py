import paho.mqtt.client as mqtt
import time
mqttBroker ="test.mosquitto.org"
c_id = "theSensorSimulatorSquare" + str(int(time.time())) + "88"
client = mqtt.Client (client_id=c_id, clean_session=True)
client.connect(mqttBroker, port=1883)
i = 1
sensorLat = 60.16920526
sensorLon = 24.95115530
sensorTime =time.localtime()
sensorEpoch =int(time.time())
interval = 1
while i < 101:
    i = i+1
    sensorLat = sensorLat + 0.0000056 # one step north. 1 metre = 0.00000899 degree
    sensorLon = sensorLon + 0.0000123 # one step east. 1 metre = 0.00000899*cos(lat) degree = 0.00000448 degree at Lat 60.169
    sensorEpoch = sensorEpoch + interval
    client.publish("Walking01/status/location", "{\"name\":\"Walker01\",\"time\":\""+str(time.ctime())+"\",\"epoch\":" +str(sensorEpoch)+",\"lat\":"+str(sensorLat)+",\"lon\":"+str(sensorLon)+"}")
    print("Published " + str(time.ctime()) + " epoch " + str(sensorEpoch) + " Lat " + str(sensorLat) + " Lon " + str(sensorLon) +" to topic Walking01/status/location")
    time.sleep(interval)
client.disconnect()