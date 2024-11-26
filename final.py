import machine
import time
from machine import Pin,I2C,PWM
from lcd_iot import LcdApi
from i2c_iot import I2cLcd
from time import sleep
import dht
from machine import Pin,PWM

#lcd code
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
sensor = dht.DHT11(Pin(14))
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)     
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
rtc = machine.RTC()
current_time = rtc.datetime()

# Initialize the garage door servo motor
servo = machine.PWM(machine.Pin(15), freq=50)
servo.duty(0)

# Configure the ESP32 WiFi as Station mode
import network

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('Connecting to network...')
    sta.active(True)
    sta.connect('Redmi 10', '9880152461')  # Replace with your WiFi SSID and password
    while not sta.isconnected():
        pass
print('Network config:', sta.ifconfig())

# Configure the socket connection over TCP/IP
import socket

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))  # Bind to all available interfaces on port 80
s.listen(5)       # Listen for incoming connections with a backlog of 5

# Function for creating the web page to be displayed
def web_page():
    return """  
    <html>  
        <head>  
         <meta content="width=device-width, initial-scale=1" name="viewport"></meta>
         <style>
           body {
             font-family: Arial, sans-serif;
           }

           h2 {
             color: #333333;
           }

           button {
             background-color: #4CAF50; /* Green */
             border: none;
             color: white;
             padding: 15px 32px;
             text-align: center;
             text-decoration: none;
             display: inline-block;
             font-size: 16px;
             margin: 4px 2px;
             cursor: pointer;
           }
         </style>
        </head>  
        <body>  
          <center><h2>Pet Feeder</h2></center>  
          <center>
           <img src="https://th.bing.com/th/id/OIG.bxu5iRZYQ_eqj_7BDv10?pid=ImgGn" alt="Happy pets" style="width: 100%;">
           <form>  
            <button name="door" type="submit" value="open"> Start Feeding Pet </button>  
            <button name="door" type="submit" value="close"> Stop Feeding Pet </button>  
           </form>  
          </center>  
        </body>  
    </html>"""

formatted_time = "{:02d}-{:02d}-{:04d}      {:02d}:{:02d}:{:02d}".format(
    current_time[2], current_time[1], current_time[0],
    current_time[4], current_time[5], current_time[6]
)
lcd.clear()
lcd.putstr(f"{formatted_time}")
lcd.move_to(0, 1)  # Move to the second line




while True:
    # Socket accept()
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
   
    # Socket receive()
    request = conn.recv(1024)
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    open_door = request.find('/?door=open')
    close_door = request.find('/?door=close')
    
    if open_door != -1:
        print('Open Door')
        servo.duty(15) 
        sleep(2)
        lcd.clear()
        lcd.putstr("Food Dispensed.")
        lcd.putstr(" Enjoy your meal!")
        servo.duty(0)
        
    elif close_door != -1:
        print('Close Door')
        servo.duty(120)  
        sleep(2)
        servo.duty(0)
        

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
   
    # Socket close()
    conn.close()