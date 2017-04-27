#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_BLUE = 3
LED_RED = 5

GPIO.setwarnings(False)
GPIO.setup(LED_BLUE,GPIO.OUT)
GPIO.setup(LED_RED,GPIO.OUT)
#Turn LEDs on
GPIO.output(LED_BLUE,GPIO.HIGH)
GPIO.output(LED_RED,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(LED_BLUE,GPIO.LOW)
GPIO.output(LED_RED,GPIO.LOW)
time.sleep(1)
#Turn LEDs on
GPIO.output(LED_BLUE,GPIO.HIGH)
GPIO.output(LED_RED,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(LED_BLUE,GPIO.LOW)
GPIO.output(LED_RED,GPIO.LOW)
GPIO.cleanup