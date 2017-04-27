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

global servo_min
global servo_base
global servo_max
global servo0_pos
global servo1_pos
global servo2_pos
global servo3_pos
global servo_min_Shoulder
global step

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_base = 375 # base pulse lenth out of 4096, 1.5ms
servo_max = 600  # Max pulse length out of 4096
servo_min_Shoulder = 275 # Min pulse length out of 4096
servo0_pos = 375  # actual position
servo1_pos = 375  # actual position
servo2_pos = 375  # actual position
servo3_pos = 375  # actual position
step = 50 #change of pulselength per step

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def StopAllServos(): #Set all signals off
    pwm.set_pwm(0, 0, 0)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(3, 0, 0)
# rotate base
def BaseToBase():
    pwm.set_pwm(0,0, servo_base)

def BaseTurnRight(): #Turn the base to the right
    global servo0_pos
    if servo0_pos < servo_min:
        servo0_pos = servo_min
    elif servo0_pos > servo_max:
        servo0_pos = servo_max
    else:
        servo0_pos = servo0_pos
    pwm.set_pwm(0, 0, servo0_pos)
    servo0_pos = servo0_pos - step

def BaseTurnLeft(): #Turn the base to the right
    global servo0_pos
    if servo0_pos < servo_min:
        servo0_pos = servo_min
    elif servo0_pos > servo_max:
        servo0_pos = servo_max
    else:
        servo0_pos = servo0_pos
    pwm.set_pwm(0, 0, servo0_pos)
    servo0_pos = servo0_pos + step

# Rotate Shooulder
def ShoulderToBase():
    pwm.set_pwm(1,0, servo_base)

def ShoulderTurnUp():
    global servo1_pos
    if servo1_pos < servo_min_Shoulder:
        servo1_pos = servo_min_Shoulder
    elif servo1_pos > servo_max:
        servo1_pos = servo_max
    else:
        servo1_pos = servo1_pos
    pwm.set_pwm(1, 0, servo1_pos)
    servo1_pos = servo1_pos - step

def ShoulderTurnDown():
    global servo1_pos
    if servo1_pos < servo_min_Shoulder:
        servo1_pos = servo_min_Shoulder
    elif servo1_pos > servo_max:
        servo1_pos = servo_max
    else:
        servo1_pos = servo1_pos
    pwm.set_pwm(1, 0, servo1_pos)
    servo1_pos = servo1_pos + step

# Rotate Elbow
def ElbowToBase():
    pwm.set_pwm(2,0, servo_base)

def ElbowTurnUp():
    global servo2_pos
    if servo2_pos < servo_min:
        servo2_pos = servo_min
    elif servo2_pos > servo_max:
        servo2_pos = servo_max
    else:
        servo2_pos = servo2_pos
    pwm.set_pwm(2, 0, servo2_pos)
    servo2_pos = servo2_pos - step

def ElbowTurnDown():
    global servo2_pos
    if servo2_pos < servo_min:
        servo2_pos = servo_min
    elif servo2_pos > servo_max:
        servo2_pos = servo_max
    else:
        servo2_pos = servo2_pos
    pwm.set_pwm(2, 0, servo2_pos)
    servo1_pos = servo2_pos + step

#Gripper
def GripperOpen():
    pwm.set_pwm(3, 0, servo_min)

def GripperClose():
    pwm.set_pwm(3, 0, servo_max)


print('Moving servos, press Ctrl-C to quit...')
GripperClose()
BaseToBase()
ShoulderToBase()
ElbowToBase()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnRight()
time.sleep(1)
BaseTurnLeft()
time.sleep(1)
BaseTurnLeft()
time.sleep(1)
BaseTurnLeft()
time.sleep(1)
BaseTurnLeft()
time.sleep(1)
BaseTurnLeft()
time.sleep(1)
BaseTurnLeft()
time.sleep(1)
ShoulderToBase()
time.sleep(1)
ShoulderTurnUp()
time.sleep(1)
ShoulderTurnUp()
time.sleep(1)
ShoulderTurnUp()
time.sleep(1)
ShoulderTurnUp()
time.sleep(1)
ShoulderTurnUp()
time.sleep(1)
ShoulderTurnUp()
time.sleep(1)
ShoulderTurnDown()
time.sleep(1)
ShoulderTurnDown()
time.sleep(1)
ShoulderTurnDown()
time.sleep(1)
ShoulderTurnDown()
time.sleep(1)
ShoulderTurnDown()
time.sleep(1)
ElbowToBase()
time.sleep(1)
ElbowTurnUp()
time.sleep(1)
ElbowTurnUp()
time.sleep(1)
ElbowTurnUp()
time.sleep(1)
ElbowTurnUp()
time.sleep(1)
ElbowTurnUp()
time.sleep(1)
ElbowTurnDown()
time.sleep(1)
ElbowTurnDown()
time.sleep(1)
ElbowTurnDown()
time.sleep(1)
ElbowTurnDown()
time.sleep(1)
ElbowTurnDown()
time.sleep(1)
GripperOpen()
time.sleep(1)
GripperClose()
time.sleep(1)
StopAllServos()
