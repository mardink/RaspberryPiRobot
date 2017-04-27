#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import SocketServer
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

#define GPIO ports
LED_blue = 7 #simulates reboot
LED_red = 11 # simaulates shutdown
Switch_shutdown = 16


#Setup the GPIO ports
GPIO.setup(LED_blue, GPIO.OUT)
GPIO.setup(LED_red, GPIO.OUT)
GPIO.setup(Switch_shutdown, GPIO.IN)

#Define the functions
def shutdown():
    os.system("sudo shutdown -h now")

def reboot():
    os.system("sudo reboot")


while True:
    time.sleep(0.1) # do not use all the cpu power
    # make a loop to test for the button being pressed
    if ( GPIO.input(Switch_shutdown) == True ):
        when_pressed = time.time()
        while GPIO.input(Switch_shutdown) == True :
            # wait until the button is not pressed any more
            time.sleep(0.001) # do not use all the cpu power
        # measure the time
        time_pressed = time.time() - when_pressed
        print time_pressed
        if time_pressed < 1:
            continue # pressed too short do not use the other cases
        if 1 < time_pressed < 3:  # Reboot
            GPIO.output(LED_blue, GPIO.HIGH)
            time.sleep(1)
            reboot()
        if 3 < time_pressed < 6: #Shutdown
            GPIO.output(LED_red, GPIO.HIGH)
            time.sleep(1)
            shutdown()
        GPIO.output(LED_blue, GPIO.LOW)
        GPIO.output(LED_red, GPIO.LOW)