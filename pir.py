from machine import Pin
import time

pir_pin=Pin(14,Pin.IN)

def motion_detected(p):
    print("Motion detected")
    
pir_pin.irq(trigger=Pin.IRQ_RISING, handler = motion_detected)

try:
    print("motion detection using PIR sensor .press Ctrl+C to exit")
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Exiting....")