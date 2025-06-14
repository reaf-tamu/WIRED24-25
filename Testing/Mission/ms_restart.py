import Jetson.GPIO as GPIO
import time

# Setup
# sets up mission switch
pin_number = 32	# what pin number is it connected to, needs to be a GPIO pin found on pinout
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.IN)	# the button is an input

# this is stuck in a loop until the button is pressed
# the rest of our code would be stuck behind the loop
# the button is active low

try:

	print("Mission switch activating…")

	while True:
		if GPIO.input(pin_number) == GPIO.LOW:
			
			while GPIO.input(pin_number) == GPIO.LOW: # Button is held down for a sec
				time.sleep(1)
			
			print("Low")
			
			
			while True:
				if GPIO.input(pin_number) == GPIO.LOW:
					break # restarts code if button pressed again
			
				else: 
print("HIGH") # if you wanted to still print high after the button is pressed
time.sleep(0.5)
		else:
			print("HIGH")
			time.sleep(0.5)

finally:
	GPIO.cleanup()
