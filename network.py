import network

ssid = "LOKI"
password = "loki1234"

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)

while not wlan.isconnected():
    pass
print("connected to wifi")