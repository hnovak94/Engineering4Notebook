import time
import picamera


with picamera.PiCamera() as camera:
	camera.resolution = (1024, 786) # sets resolution of picture
	camera.start_preview()
	time.sleep(2)
	
	print("running") # so i know the camera is running 
	
	camera.image_effect = 'negative' # applies 'negative' filter
	camera.capture('../pics/c1.png') # where the image is saved and its name
	print("image 1") # so i know when image 1 is done, easier to find where the problem is
	
	camera.image_effect = 'sketch' # applies 'sketch' filter
	camera.capture('../pics/c2.png') # where the image is saved and its name
	print("image 2") # i know image 2 is done
	
	camera.image_effect = 'oilpaint' # applies 'oilpaint' filter
	camera.capture('../pics/c3.png') # where the image is saved and its name
	print("image 3") # i know image 3 is done
	
	camera.image_effect = 'blur' # applies 'blur' filter
	camera.capture('../pics/c4.png') # where the image is saved and its name
	print("image 4") # i know image 4 is done
	
	camera.image_effect = 'cartoon' # applies 'cartoon'
	camera.capture('../pics/c5.png') # where the image is saved and its name
	print("image 5") # i know image 5 is done
	
	print("done") # done taking all the images 
