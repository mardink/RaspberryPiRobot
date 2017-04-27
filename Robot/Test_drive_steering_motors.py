#!/usr/bin/env python
# Simply sets motors on and off for driving motor and steering motor
# Motor A Pins 19 and 21
# Motor B Pins 24 and 26

import time, RPi.GPIO as GPIO

MotorA_dir = 7
MotorA_speed = 8
MotorB_dir = 9
MotorB_speed = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)

# wait after setup to check nothing happens!
time.sleep(3)

# switch Driving Motor on backwards
GPIO.output (MotorB_speed, 1)
GPIO.output (MotorB_dir, 0)

# wait another 1 seconds
time.sleep(1)

# switch Driving Motor on forwards
GPIO.output (MotorB_speed, 0)
GPIO.output (MotorB_dir, 1)

# wait another 1 seconds
time.sleep(1)

# switch Driving Motor off
GPIO.output (MotorB_speed, 0)
GPIO.output (MotorB_dir, 0)

# wait another 1 seconds
time.sleep(1)

# switch Steering Motor left
GPIO.output (MotorA_speed, 1)
GPIO.output (MotorA_dir, 0)

# wait another 1 seconds
time.sleep(1)

# switch Steering Motor right
GPIO.output (MotorA_speed, 0)
GPIO.output (MotorA_dir, 1)

# wait another 1 seconds
time.sleep(1)

# switch Steering Motor off
GPIO.output (MotorA_speed, 0)
GPIO.output (MotorA_dir, 0)

GPIO.cleanup()