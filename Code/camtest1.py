import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768) # resolution of the image
	camera.start_preview()
	# camera warm up
	time.sleep(2)
	print("running")
	camera.capture('../pics/camtest.png') # takes picture
	# () indicates where the image will be saved and what its name will be 
	print("done")
