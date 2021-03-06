"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""
"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth, sys

hostMACAddress = sys.argv[1] # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 29 
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            #client.send(data) # Echo back to client
except Exception as e:
    print(e)
    print("Closing socket")
    client.close()
    s.close()
