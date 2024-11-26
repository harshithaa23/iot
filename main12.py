from machine import Pin, I2C
import ssd1306
from time import sleep
 
# ESP32 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
 
oled.text('Welcome', 0, 0)
oled.text('cranes ', 0, 10)
oled.text('datascience', 0, 20)
oled.text('Arpita ', 0, 30)
       
oled.show()