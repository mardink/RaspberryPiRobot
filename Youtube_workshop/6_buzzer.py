#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Led_blue = 21 
Led_red = 17
Buzzer = 22
Button_left = 18 #Pin 12 on the board
Button_right = 4 #Pin 7 on the board

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)

loop_count = 0

def morsecode ():

	#Dot Dot Dot
	GPIO.output(Buzzer,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(Buzzer,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(Buzzer,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(Buzzer,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(Buzzer,GPIO.HIGH)
	time.sleep(.1)

	#Dash Dash Dah
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)

	#Dot Dot Dot
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.7)
	
os.system('clear')
print "Morse Code"
loop_count = input("How many times would you like SOS to loop?: ")
while loop_count > 0:
	loop_count = loop_count - 1
	morsecode ()