#wap to measure the moisture of soil and display on the lcd
import machine
from machine import Pin, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

soil_moisture_pin=14
soil_moisture_sensor = Pin(soil_moisture_pin, Pin.IN)
while True:
    soil_moisture = soil_moisture_sensor.value()
    if soil_moisture == 0:
        lcd.putstr("soil wet")
        sleep(2)
        lcd.clear()
    else:
        lcd.putstr("soil dry")
        sleep(2)
        lcd.clear()
        
    