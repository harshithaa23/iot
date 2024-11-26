from machine import Pin, ADC
import time

# Define the pin to which the analog output of the MQ-3 sensor is connected
mq3_analog_pin = 34  # Change this pin number as per your wiring

# Define the threshold voltage (you might need to adjust this based on your specific sensor and application)
threshold_voltage = 1.5  # Adjust this value according to your sensor specifications

# Create an ADC object
adc = ADC(Pin(mq3_analog_pin))

# Create a digital pin for the digital output
mq3_digital_pin = Pin(32, Pin.IN)  # Change this pin number as per your wiring

while True:
    # Read the raw ADC value from the MQ-3 sensor
    raw_value = adc.read()

    # Calculate the voltage based on the raw ADC value (assuming 3.3V reference voltage)
    voltage = raw_value / 4095 * 3.3  # ESP32 ADC is 12-bit (2^12 = 4096)

    # Check if the voltage crosses the threshold
    if voltage > threshold_voltage:
        mq3_digital_pin.value(1)  # Set the digital pin high
        print("Gas detected!")
    else:
        mq3_digital_pin.value(0)  # Set the digital pin low
        print("No gas detected.")

    # Wait for some time before taking the next reading (e.g., 1 second)
    time.sleep(1)