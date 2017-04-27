#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Led_blue = 21 
Led_red = 17
Buzzer = 22
Button_left = 18 #Pin 12 on the board
Button_right = 4 #Pin 7 on the board
Servo_pan = 25 #Pin 22 on the board
Servo_tilt = 24 #Pin 18 on the board
Sonar = 8
MotorA_dir = 7
MotorA_speed = 8
MotorB_dir = 9
MotorB_speed = 10

#Set the servo port
GPIO.setmode(GPIO.BCM) # Use Gpio pin numbering
#GPIO.setmode(GPIO.BOARD) Use the board numbering
GPIO.setup(Servo_pan, GPIO.OUT)
GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)

p = GPIO.PWM(Servo_pan,50)
p.start(7.5) # Go to neutral at start

try:
    while True:
       if ( GPIO.input(Button_right) == False ):
          #180
            p.ChangeDutyCycle(12.5)
            time.sleep(1)
            
       if ( GPIO.input(Button_left) == False ):
          #0
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
            
       if ( GPIO.input(Button_right) == False  and GPIO.input(Button_left) == False ):
          #neutral
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            
    time.sleep(0.1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

