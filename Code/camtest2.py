import time
import picamera


with picamera.PiCamera() as camera:
	camera.resolution = (1024, 786)
	camera.start_preview()
	time.sleep(2)
	
	print("running")
	
	camera.image_effect = 'negative'
	camera.capture('../pics/c1.png')
	print("image 1")
	
	camera.image_effect = 'sketch'
	camera.capture('../pics/c2.png')
	print("image 2")
	
	camera.image_effect = 'oilpaint'
	camera.capture('../pics/c3.png')
	print("image 3")
	
	camera.image_effect = 'blur'
	camera.capture('../pics/c4.png')
	print("image 4")
	
	camera.image_effect = 'cartoon'
	camera.capture('../pics/c5.png')
	print("image 5")
	
	print("done")
