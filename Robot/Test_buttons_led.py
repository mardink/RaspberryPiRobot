#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) #used for chip numbering
GPIO.setmode(GPIO.BOARD) #used for board numbering, better when using multiple types of pi
GPIO.setwarnings(False)

# Settings 
Led_blue = 13        #Pin 13 on the board or 21 BCM rev1
Led_red = 11         #Pin 11 on the board or 17 BCM rev1
Buzzer = 15          #Pin 15 on the board or 22 BCM rev1
Button_left = 7      #Pin 7 on the board or 4 BCM rev1
Button_right = 12    #Pin 12 on the board or 18 BCM rev1
Servo_pan = 22       #Pin 22 on the board or 25 BCM rev1
Servo_tilt = 18      #Pin 18 on the board or 24 BCM rev1
Sonar = 8           #Pin 8 on the board or 14 BCM rev1
MotorA_dir = 26       #Pin 26 on the board or 7 BCM rev1
MotorA_speed = 24     #Pin 24 on the board or 8 BCM rev1
MotorB_dir = 21       #Pin 21 on the board or 9 BCM rev1
MotorB_speed = 19    #Pin 19 on the board or 10 BCM rev1
GPIO.setwarnings(False)
GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)
GPIO.setup(Led_red,GPIO.OUT) 
GPIO.setup(Led_blue,GPIO.OUT)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print GPIO.input(Button_right)
while True:
   if ( GPIO.input(Button_right) == False ):
      GPIO.output(Led_red,GPIO.HIGH)
      time.sleep(1)
   else:
      os.system('clear')
      GPIO.output(Led_red,GPIO.LOW)
      GPIO.output(Led_blue,GPIO.LOW)
      print ("Waiting for you to press a button")
   if ( GPIO.input(Button_left) == False ):
      GPIO.output(Led_blue,GPIO.HIGH)
      time.sleep(1)
   else:
      os.system('clear')
      GPIO.output(Led_red,GPIO.LOW)
      GPIO.output(Led_blue,GPIO.LOW)
      print ("Waiting for you to press a button")
time.sleep(0.1)
