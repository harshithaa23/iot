import machine 
import time

led = machine.Pin(2, machine.Pin.OUT)
while True:
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(2)