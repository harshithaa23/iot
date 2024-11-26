import urequests
import time

# ThingSpeak channel details
channel_id = '2352494'
read_api_key = '0GYNV8DUGKHRMQUA'

def read_thingspeak():
    url = 'https://api.thingspeak.com/channels/{}/feeds/last.json?api_key={}'.format(channel_id, read_api_key)

    try:
        response = urequests.get(url)
        data = response.json()
        # Assuming your ThingSpeak channel has fields named field1, field2, etc.
        field1_value = data.get('field1')
        field2_value = data.get('field2')
        # Add more fields as needed

        print("Field 1:", field1_value)
        print("Field 2:", field2_value)
        # Print or use the values as needed

    except Exception as e:
        print("Error:", e)

    finally:
        if response:
            response.close()

# Read ThingSpeak data every 10 seconds
while True:
    read_thingspeak()
    time.sleep(10)