# External module imports
import RPi.GPIO as GPIO
from time import sleep

# Pin Definitions:
IRsensorPin = 18

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(IRsensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Pin set as input

def wait_for_IR():
	GPIO.wait_for_edge(IRsensorPin, GPIO.RISING)
	sleep(1)

