#!/usr/bin/env python
import os
import datetime
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

DEBUG = 1
GPIO.setmode(GPIO.BOARD)

 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
 
while True:                                     
    	GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        LDRReading = RCtime(13) #Gpio21 or Board21
        print RCtime(13) #Gpio1 or Board21

		# Open a file
        fo = open("/usr/share/adafruit/webide/repositories/my-pi-projects/test_scripts/Rapsberry_robot/ldr.txt", "wb")
        fo.write (GetDateTime)
        LDRReading = str(LDRReading)
        fo.write ("\n")
        fo.write (LDRReading)
		
		# Close opend file
        fo.close()
        time.sleep(1)