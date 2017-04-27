# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position
# Author: Martijn Hiddink 2016
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_base = 375 # base pulse lenth out of 4096, 1.5ms
servo_max = 600  # Max pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


print('Moving servo on channel 0, press Ctrl-C to quit...')
# Move servo on channel O between extremes.
# Rotate base
pwm.set_pwm(1, 0, servo_max)
time.sleep(1)
pwm.set_pwm(1, 0, servo_base)
time.sleep(1)
pwm.set_pwm(1, 0, servo_min)
time.sleep(1)
pwm.set_pwm(1, 0, 0) #Set the signal off
pwm.set_pwm(2, 0, 0) #Set the signal off
pwm.set_pwm(3, 0, 0) #Set the signal off
pwm.set_pwm(4, 0, 0) #Set the signal off