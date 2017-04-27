import RPi.GPIO as GPIO, sys, threading, time

Led_blue = 21 
Led_red = 17
Buzzer = 22
Button_left = 4 #Pin 7 on the board
Button_right = 18 #Pin 12 on the board
Servo_pan = 25 #Pin 22 on the board
Servo_tilt = 24 #Pin 18 on the board
Sonar = 14
MotorA_dir = 7
MotorA_speed = 8
MotorB_dir = 9
MotorB_speed = 10
#use physical pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


try:
   while True:
       GPIO.setup(Sonar, GPIO.OUT)
       GPIO.setup(Led_blue, GPIO.OUT)
       GPIO.setup(Led_red, GPIO.OUT)
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

