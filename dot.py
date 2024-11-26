
from machine import Pin
from utime import sleep_ms # milli sec


led = Pin(15, Pin.OUT)
led1 = Pin(2, Pin.OUT)
led2 = Pin(0, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(16, Pin.OUT)
while True:
    led.on()
    sleep_ms(200)
    led1.on()
    sleep_ms(200)
    led2.on()
    sleep_ms(200)
    led3.on()
    sleep_ms(200)
    led3.on()
    sleep_ms(200)
    led.off()
    sleep_ms(200)
    led1.off()
    sleep_ms(200)
    led2.off()
    sleep_ms(200)
    led3.off()
    sleep_ms(200)
    led4.off()
    sleep_ms(200)