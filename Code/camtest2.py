import time
import picamera


with picamera.PiCamera() as camera:
	camera.resolution = (1024, 786)
	camera.start_preview()
	time.sleep(2)
	print("running")
	camera.image_effect()
	camera.capture('../pics/c1.png')
	PiCamera.IMAGE_EFFECTS = 'negative'
	print("image 1")
	camera.capture('../pics/c2.png')
	PiCamera.IMAGE_EFFECTS = 'sketch'
	print("image 2")
	camera.capture('../pics/c3.png')
	PiCamera.IMAGE_EFFECTS = 'oilpaint'
	print("image 3")
	camera.capture('../pics/c4.png')
	PiCamera.IMAGE_EFFECTS = 'blur'
	print("image 4")
	camera.capture('../pics/c5.png')
	PiCamera.IMAGE_EFFECTS = 'cartoon'
	print("image 5")
	print("done")
