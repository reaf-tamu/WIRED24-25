import time
import Jetson.GPIO as GPIO


# sets up mission switch
pin_number = 32	# what pin number is it connected to, needs to be a GPIO pin found on pinout
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.IN)	# the button is an input


# activate mission switch
print("Mission switch activating…")
while (GPIO.input(pin_number) == GPIO.HIGH):
	print("HIGH")
	time.sleep(0.5)
print("LOW")

from adafruit_servokit import ServoKit
# thrusters
# Initialize PCA9685 with 16 channels,
kit = ServoKit(channels=16)

#Set correct PWM range for ESCs: 1100–1900 µs,
kit.servo[7].set_pulse_width_range(1100, 1900)

class Motor:
    def init(self, channel):
        self.channel = channel
        self.speed = 90  # Default to neutral (1500 µs)
        self.prev_speed = None  # Force update on first run

    def set_speed(self, angle):
        self.speed = angle

    def run(self):
        if self.prev_speed != self.speed:
            print(f"Sending PWM: {self.speed}°")
            kit.servo[self.channel].angle = self.speed
            self.prev_speed = self.speed

    def stop(self):
        self.set_speed(90)
        self.run()

# Initialize A1 on channel 7 (ESC signal wire is connected here),
A1 = Motor(7)


# ESC Initialization,
print("Initializing ESC with 1500 µs (90°) signal...")
A1.set_speed(90)
A1.run()
time.sleep(5)  # Wait 5 seconds for ESC to arm (listen for 2 beeps)





# run thrusters
while True:
	# running speed
	A1.set_speed(80)  # ~1400 µs (reverse)
	A1.run()
	print(f"Thruster speed: {A1.self_speed}")
	time.sleep(1)


