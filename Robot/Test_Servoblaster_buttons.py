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
GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)

#Set the pan and Tilt Functions
# define direction functions

def pan_left():
    cmd = 'echo 7=+10 > /dev/servoblaster'
    os.system(cmd)

def pan_right():
    cmd = 'echo 7=-10 > /dev/servoblaster'
    os.system(cmd)

def pan_neutral():
    cmd = 'echo 7=150 > /dev/servoblaster'
    os.system(cmd)

def tilt_up():
    cmd = 'echo 6=-10 > /dev/servoblaster'
    os.system(cmd)

def tilt_down():
    cmd = 'echo 6=+10 > /dev/servoblaster'
    os.system(cmd)

def tilt_neutral():
    cmd = 'echo 6=150 > /dev/servoblaster'
    os.system(cmd)

try:
    while True:
       if ( GPIO.input(Button_right) == False and GPIO.input(Button_left) != False ):
            pan_right()
            time.sleep(0.5)
            
       if ( GPIO.input(Button_left) == False and GPIO.input(Button_right) != False ):
            pan_left()
            time.sleep(0.5)
            
       if ( GPIO.input(Button_right) == False  and GPIO.input(Button_left) == False ):
            pan_neutral()          
            time.sleep(0.5)
            
    time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
