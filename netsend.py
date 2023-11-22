import serial
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BOARD)

#set the GPIO input pins
pirPin = 8

GPIO.setup(pirPin, GPIO.IN)

subprocess.call("pd-extended yourpatch.pd &", shell=True)

pirValue = 0

def send2Pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")

while True:
    pirValue = GPIO.input(pirPin)
    send2Pd(str(pirValue))
    
    time.sleep(0.1)