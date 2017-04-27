#!/usr/bin/python
import RPi.GPIO as GPIO

Led_blue = 21 
Led_red = 17
Buzzer = 22
Button_left = 18 #Pin 12 on the board
Button_right = 4 #Pin 7 on the board

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(Led_red,GPIO.OUT) 
GPIO.setup(Led_blue,GPIO.OUT)
print "Lights on"
GPIO.output(Led_red,GPIO.HIGH)
GPIO.output(Led_blue,GPIO.HIGH)