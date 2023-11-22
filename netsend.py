import serial
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)

#identify this device among other senders on the network
THIS_BOARD = 0

TARGET_ADDRESSES = ["192.168.0.7"]

#set the GPIO input pins
pirPin = 8

GPIO.setup(pirPin, GPIO.IN)

#subprocess.call("pd-extended yourpatch.pd &", shell=True)

pirValue = 0

def send2Pd(message=''):
	for addr in TARGET_ADDRESSES:
	    os.system("echo '" + str(THIS_BOARD) + " " + message + "' | pdsend 3000 " + addr + " udp")

while True:
    pirValue = GPIO.input(pirPin)
    send2Pd(str(pirValue))
    
    time.sleep(0.1)
