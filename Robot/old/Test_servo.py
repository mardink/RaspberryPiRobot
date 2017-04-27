#!/usr/bin/python


#NIET GEBRUIKEN IS NIET MEER UP TO DATE









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

#Set the servo port
GPIO.setmode(GPIO.BCM) # Use Gpio pin numbering
#GPIO.setmode(GPIO.BOARD) Use the board numbering
GPIO.setup(Servo_pan, GPIO.OUT)
p = GPIO.PWM(Servo_pan,50)
p.start(7.5)

# Run a test script
try:
    while True:
        #Neutral
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        #180
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        #0
        p.ChangeDutyCycle(2.5)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()