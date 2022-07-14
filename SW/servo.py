# External module imports
import RPi.GPIO as GPIO
from time import sleep

# Pin Definitions:
ServoPin = 19

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ServoPin, GPIO.OUT) # Pin set output

# PWM Setup:
servo_pwm = GPIO.PWM(ServoPin, 50) # Frequency 50Hz, period 20ms
servo_pwm.start(0)

def close_door():
	servo_pwm.ChangeDutyCycle(5)
	sleep(0.2)
#	servo_pwm.stop()

def open_door():
	servo_pwm.ChangeDutyCycle(10)
	sleep(0.2)
#	servo_pwm.stop()


