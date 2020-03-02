"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""
from gpiozero import Button
from time import sleep

button = Button(18)
import bluetooth
import sys

def make_connection():
    serverMACAddress = sys.argv[0] 
    port = 29
    try: 
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.connect((serverMACAddress, port))
        counter = 0
        sleep(5)
        while True:
            print(counter)
            if button.is_pressed:
                counter += 1
                if counter == 100:
                    counter = -20
                    s.send("Long click")
            else:
                if 10 < counter > 0:
                    counter = 0
                    s.send("Click")
                counter = 0
            sleep(0.01)
                
    except Exception as e:
        print(e)
        return False
    return True

while True:
    sleep(1)
    try: 
        make_connection()
    except: 
        print("No server yet") 
s.close()
exit(0)

