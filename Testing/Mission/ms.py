import Jetson.GPIO as GPIO
import time

# sets up mission switch
pin_number = 32	# what pin number is it connected to, needs to be a GPIO pin found on pinout
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.IN)	# the button is an input

# this just prints out the value
"""
print("Starting to monitor GPIO")
while True:
	status = GPIO.input(pin_number)
	print(f"Pin {pin_number} status: {status}")
	time.sleep(1)

"""

# this is stuck in a loop until the button is pressed
# the rest of our code would be stuck behind the loop
# the button is active low
try:

	print("Mission switch activating…")

	while (GPIO.input(pin_number) == GPIO.HIGH):
		print("HIGH")
		time.sleep(0.5)
	
	print("LOW")

finally:
	GPIO.cleanup()

