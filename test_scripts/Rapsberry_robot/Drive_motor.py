#!/usr/bin/env python
# Simply sets motors on and off in both directions
# Motor A Pins 19 and 21
# Motor B Pins 24 and 26

import time, RPi.GPIO as GPIO

MotorA_dir = 26
MotorA_speed = 24
MotorB_dir = 21
MotorB_speed = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)

# wait after setup to check nothing happens!
time.sleep(3)

# switch MotorA on forwards
GPIO.output (MotorB_speed, 1)
GPIO.output (MotorB_dir, 0)

# wait another 3 seconds
time.sleep(3)

# switch MotorA on backwards
GPIO.output (MotorB_speed, 0)
GPIO.output (MotorB_dir, 1)

# wait another 3 seconds
time.sleep(3)

# switch MotorA off
GPIO.output (MotorB_speed, 0)
GPIO.output (MotorB_dir, 0)

# wait another 3 seconds
time.sleep(3)

# switch MotorB on Forwards
GPIO.output (MotorA_speed, 1)
GPIO.output (MotorA_dir, 0)

# wait another 3 seconds
time.sleep(3)

# switch MotorB on Backwards
GPIO.output (MotorA_speed, 0)
GPIO.output (MotorA_dir, 1)

# wait another 3 seconds
time.sleep(3)

# switch MotorB off
GPIO.output (MotorA_speed, 0)
GPIO.output (MotorA_dir, 0)

GPIO.cleanup()