#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Led_blue = 21 
Led_red = 17
Buzzer = 22
Button_left = 4 #Pin 7 on the board
Button_right = 18 #Pin 12 on the board
Servo_pan = 25 #Pin 22 on the board
Servo_tilt = 24 #Pin 18 on the board
Sonar = 8
MotorA_dir = 7
MotorA_speed = 8
MotorB_dir = 9
MotorB_speed = 10

#Set the gpio ports
GPIO.setmode(GPIO.BCM) # Use Gpio pin numbering
GPIO.setwarnings(False)
GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)

#set the functions
# switch Driving Motor on backwards
def drive_backwards():
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)

# switch Driving Motor on forwards
def drive_forwards():
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)

# switch Driving Motor off
def drive_stop():
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 0)

# switch Steering Motor left
def steering_left():
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)

# switch Steering Motor right
def steering_right():
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)

# switch Steering Motor off
def steering_stop():
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 0)

try:
    while True:
        drive = 1
        steering = 0
        direction = drive
        #set driving
        if ( GPIO.input(Button_right) == False and GPIO.input(Button_left) != False and direction == 1 ):
            drive_forwards()
            time.sleep(0.1)
        else:
            drive_stop()
        if ( GPIO.input(Button_left) == False and GPIO.input(Button_right) != False and direction == 1 ):
            drive_backwards()
            time.sleep(0.1)
        else:
            drive_stop()
        # set steering
        if ( GPIO.input(Button_right) == False and GPIO.input(Button_left) != False and direction == 0 ):
            steering_right()
            time.sleep(0.1)
        else:
            steering_stop()
        if ( GPIO.input(Button_left) == False and GPIO.input(Button_right) != False and direction == 0 ):
            steering_left()
            time.sleep(0.1)
        else:
            steering_stop()
                    
    time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()