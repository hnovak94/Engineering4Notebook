# RPi GPIO Pin Introduction
# Harriet Novak
# 9.18.21
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep
GPIO.setmode(GPIO.BCM) # pin numbering scheme same as BCM numbering scheme
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

while True:

	GPIO.output(21, GPIO.HIGH)
	GPIO.output(20, GPIO.LOW)
	time.sleep(1)

	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.HIGH)
	time.sleep(1)
