import RPi.GPIO as GPIO, sys, threading, time


Sonar = 8

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


try:
   while True:
       GPIO.setup(Sonar, GPIO.OUT)
       GPIO.output(Sonar, True)
       time.sleep(0.00001)
       GPIO.output(Sonar, False)
       start = time.time()
       count = time.time()
       GPIO.setup(Sonar, GPIO.IN)
       while GPIO.input(Sonar)==0 and time.time()-count<0.1:
           start = time.time()
       stop=time.time()
       while GPIO.input(Sonar)==1:
           stop = time.time()
       # Calculate pulse length
       elapsed = stop-start
       # Distance pulse travelled in that time is time
       # multiplied by the speed of sound (cm/s)
       distance = elapsed * 34000
       # That was the distance there and back so halve the value
       distance = distance / 2
       print 'Distance:', distance
       time.sleep(1)

except KeyboardInterrupt:
       GPIO.cleanup()
