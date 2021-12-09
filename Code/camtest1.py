import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	# camera warm up
	time.sleep(2)
	print("running")
	camera.capture('../pics/camtest.png')
	print("done")
