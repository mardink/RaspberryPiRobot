#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

Buzzer = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Buzzer,GPIO.OUT)

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

	
	
os.system('clear')
print "Morse Code"
loop_count = input("How many times would you like SOS to loop?: ")
while loop_count > 0:
	loop_count = loop_count - 1
	morsecode ()