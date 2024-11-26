import machine
from machine import Pin, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import dht

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
sensor = dht.DHT11(Pin(14))

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    #temp_f = temp * (9/5) + 32.0
    lcd.putstr('Temperature: %3.1f C' %temp)
    sleep(3)
    lcd.clear()
    #print('Temperature: %1.2f F' %temp_f)
    lcd.putstr('Humidity: %3.1f %%' %hum)
    sleep(3)
    lcd.clear()
  except OSError as e:
    lcd.putstr('Failed to read sensor.')
    sleep(3)
    lcd.clear()
