from datetime import datetime
import json

i = 0
utcTime = datetime.utcnow()
sensorLat = 60.16920526
sensorLon = 24.95115530
#sensorTime =time.localtime()
interval = 2

container = []
dic = {"gps": {"data": None, "UTCtime": str(utcTime), "latitude": sensorLat, "N_S": "N" ,"longitude": sensorLon, "E_W": "E"}}



while i < 10:
    i = i+1
    sensorLat = sensorLat + 0.0000056 # one step north. 1 metre = 0.00000899 degree
    sensorLon = sensorLon + 0.0000123 # one step east. 1 metre = 0.00000899*cos(lat) degree = 0.00000448 degree at Lat 60.169
    utcTime = datetime.utcnow()
    dic = {"gps": {"data": "$GNRMC,131025.000,A,6015.14286,N,02500.56340,E,0.00,303.89,270322,,,A,V01", "UTCtime": str(utcTime), "latitude": sensorLat, "N_S": "N" ,"longitude": sensorLon, "E_W": "E"}}
    container.append(dic)
   


print(container)
with open("sample.json", "w") as outfile:
    json.dump(container, outfile)



