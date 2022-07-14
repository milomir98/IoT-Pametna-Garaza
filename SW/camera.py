# External module imports
from picamera import PiCamera
from time import sleep
import os

# Camera init
camera = PiCamera()

def take_a_picture():
	if(os.path.isfile('/home/pi/Desktop/PES_Projekat/tablica.jpg')):
		os.remove('/home/pi/Desktop/PES_Projekat/tablica.jpg')
	else:
		print("Picture doesn't exist")
	camera.start_preview()
	sleep(5)
	camera.capture('/home/pi/Desktop/PES_Projekat/tablica.jpg')
	camera.stop_preview()




