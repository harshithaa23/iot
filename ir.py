import machine
import time

ir_sensor_pin=machine.Pin(15,machine.Pin.IN)

def check_ir_sensor():
    return ir_sensor_pin.value()

while True:
    if check_ir_sensor() == 0:
        print("object detected")
    else:
        print("object not detected")
    time.sleep(1)
    
#wap to beep the buzzer when object detected