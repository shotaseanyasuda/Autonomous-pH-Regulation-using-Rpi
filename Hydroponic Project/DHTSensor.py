# DHTSensor.py

import time
import board
import adafruit_dht

# DHTSensor can only take readings every 3 seconds. Any smaller increment causes it to glitch and crash
class DHTSensor():
    
    def getTemperature():
        # Initial the dht device, with data pin connected to:
        dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio = False)
        
        # dhtDevice.temperature gives a reading in Celcius
        temperature = dhtDevice.temperature
        return temperature
    
        
    
    def getHumidity():
        # Initial the dht device, with data pin connected to:
        dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio = False)
        humidity = dhtDevice.humidity
        return humidity
    
    #print("Temp in Fahrenhieit: " + str(getTemperature()) + "F")
    #time.sleep(5)
    #print("Humidity: " + str(getHumidity()) + "%")
