#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Button_up = 12 #Pin 12 on the board, 18 BCM
Button_down = 7 #Pin 7 on the board, 4 BCM


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setwarnings(False)
GPIO.setup(Button_up, GPIO.IN)
GPIO.setup(Button_down, GPIO.IN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

print GPIO.input(Button_up)
while True:
   if ( GPIO.input(Button_up) == False ):
      print("Button Up Pressed")
      os.system('date')
      print GPIO.input(Button_up)
      time.sleep(5)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
   if ( GPIO.input(Button_down) == False ):
      print("Button Down Pressed")
      os.system('date')
      print GPIO.input(Button_down)
      time.sleep(5)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
time.sleep(1)