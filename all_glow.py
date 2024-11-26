from machine import Pin
import time
num_rows = 7
num_cols = 5
row_pins = [15, 2, 4, 16, 17, 5, 18]
col_pins = [19, 21, 22, 23, 14]  
row_pins = [Pin(pin, Pin.OUT) for pin in row_pins]
col_pins = [Pin(pin, Pin.OUT) for pin in col_pins]
def light_up_first_column():
    col_pins[1].value(0)  # Set the first column pin to LOW
    for row_pin in row_pins:
        row_pin.value(1)  # Set all row pins to HIGH
# Function to clear the LED matrix
def clear_display():
    for row_pin in row_pins:
        row_pin.value(0)  # Set to LOW for common cathode
    for col_pin in col_pins:
        col_pin.value(1)  # Set to HIGH to turn off all columns
while True:
    light_up_first_column()
    time.sleep(1)
    clear_display()