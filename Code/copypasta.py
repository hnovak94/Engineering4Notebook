import picamera
from time import sleep
from gpiozero import Button
import time

button = Button(27) # sets pin for button

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 786) # sets resolution of image
	camera.start_preview()
	time.sleep(.2)

	print("running")

	button.wait_for_press() 
	camera.capture('../pics/cp3.png') # where image is saved and its name
	camera.stop_preview
	print("done")
