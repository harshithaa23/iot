from machine import Pin
import time

soil_moisture_pin=14

soil_moisture_sensor = Pin(soil_moisture_pin, Pin.IN)

while True:
    
    soil_moisture = soil_moisture_sensor.value()
    
    if soil_moisture == 0:
        print("soil is wet")
    else:
        print("soil is dry")
        
    time.sleep(3)