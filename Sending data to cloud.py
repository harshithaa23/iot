import dht
import machine
import network
import time
import urequests

# Replace with your WiFi credentials
WIFI_SSID = "LOKI"
WIFI_PASSWORD = "loki1234"

# Replace with your ThingSpeak API key
THINGSPEAK_API_KEY = "OFSTHXYCKSUL2K1B"

DHT_PIN = 14  # GPIO pin where the DHT11 sensor is connected

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print("Connected to WiFi:", sta_if.ifconfig())

def read_dht11():
    dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))
   
    # Try to read from the sensor up to 3 times
    for _ in range(3):
        try:
            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()
            return temperature, humidity
        except Exception as e:
            print("Error reading DHT11:", e)
            time.sleep(2)  # Wait for 2 seconds before retrying

    print("Failed to read from DHT11 after multiple attempts.")
    return None, None


def send_to_thingspeak(temperature, humidity):
    api_url = "http://api.thingspeak.com/update"
    data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": temperature,
        "field2": humidity,
    }
    response = urequests.post(api_url, json=data)
    print("ThingSpeak response:", response.text)
    response.close()

def main():
    connect_to_wifi()

    while True:
        temperature, humidity = read_dht11()
        print("Temperature: {}°C, Humidity: {}%".format(temperature, humidity))

        send_to_thingspeak(temperature, humidity)

        # Upload data every 15 seconds (adjust as needed)
        time.sleep(10)

if __name__ == "__main__":
    main()

