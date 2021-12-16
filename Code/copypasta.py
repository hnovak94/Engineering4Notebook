import picamera
from time import sleep
from gpiozero import Button
import time

button = Button(27)

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 786)
	camera.start_preview()
	time.sleep(.2)

	print("running")

	button.wait_for_press()
	camera.capture('../pics/cp.png')
	camera.stop_preview
	print("done")
