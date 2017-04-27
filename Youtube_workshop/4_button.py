#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Led_blue = 21 
Led_red = 17
Buzzer = 22
Button_left = 18 #Pin 12 on the board
Button_right = 4 #Pin 7 on the board
Button = 10 #youtube tutorial

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(Button, GPIO.IN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print GPIO.input(Button)
while True:
   if ( GPIO.input(Button) == False ):
      print("Button Pressed")
      os.system('date')
      print GPIO.input(Button)
      time.sleep(5)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
time.sleep(1)
