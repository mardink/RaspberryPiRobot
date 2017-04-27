#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Button_Left_up = 26 #Pin 26 on the board, 07 BCM
Button_Left_down = 7 #Pin 7 on the board, 4 BCM
Button_Right_down = 11 #Pin 11 on the board, 17 BCM
Button_Right_up = 13 #Pin 13 on the board, 21 BCM


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setwarnings(False)
GPIO.setup(Button_Left_up, GPIO.IN)
GPIO.setup(Button_Left_down, GPIO.IN)
GPIO.setup(Button_Right_up, GPIO.IN)
GPIO.setup(Button_Right_down, GPIO.IN)

print("------------------")
print(" Button + GPIO ")
print("------------------")

#print GPIO.input(Button_Left_up)
while True:
   if ( GPIO.input(Button_Left_up) == False ):
      print("Button Left Up Pressed")
      os.system('date')
      print GPIO.input(Button_Left_up)
      time.sleep(1)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
   if ( GPIO.input(Button_Left_down) == False ):
      print("Button Left Down Pressed")
      os.system('date')
      print GPIO.input(Button_Left_down)
      time.sleep(1)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
   if ( GPIO.input(Button_Right_up) == False ):
      print("Button Right Up Pressed")
      os.system('date')
      print GPIO.input(Button_Right_up)
      time.sleep(1)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
   if ( GPIO.input(Button_Right_down) == False ):
      print("Button Right Down Pressed")
      os.system('date')
      print GPIO.input(Button_Right_down)
      time.sleep(1)
   else:
      os.system('clear')
      print ("Waiting for you to press a button")
time.sleep(1)