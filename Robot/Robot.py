#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) #used for chip numbering
GPIO.setmode(GPIO.BOARD) #used for board numbering, better when using multiple types of pi
GPIO.setwarnings(False)

# Settings 
Led_blue = 13        #Pin 13 on the board or 21 BCM rev1
Led_red = 11         #Pin 11 on the board or 17 BCM rev1
Buzzer = 15          #Pin 15 on the board or 22 BCM rev1
Button_left = 7      #Pin 7 on the board or 4 BCM rev1
Button_right = 12    #Pin 12 on the board or 18 BCM rev1
Servo_pan = 22       #Pin 22 on the board or 25 BCM rev1
Servo_tilt = 18      #Pin 18 on the board or 24 BCM rev1
Sonar = 8           #Pin 8 on the board or 14 BCM rev1
MotorA_dir = 26       #Pin 26 on the board or 7 BCM rev1
MotorA_speed = 24     #Pin 24 on the board or 8 BCM rev1
MotorB_dir = 21       #Pin 21 on the board or 9 BCM rev1
MotorB_speed = 19    #Pin 19 on the board or 10 BCM rev1

#Set ports OUT
GPIO.setup(Servo_pan, GPIO.OUT)
GPIO.setup(Servo_tilt, GPIO.OUT)
GPIO.setup(Led_red,GPIO.OUT) 
GPIO.setup(Led_blue,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)

#Set ports In
GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)

#Read position Servos
def Read_Servo():
    # Open a file
    file = open("position.txt", "r+")
    pan_value = file.readline()
    tilt_value =file.readline()
    # Close opend file
    file.close()
    return (pan_value, tilt_value)
    
    
#Write position Servos
def Write_Servo(pan, tilt):
    # Open a file
    file = open("position.txt", "wb")
    if pan < 50:
        pan = 50
    elif pan >250:
        pan = 250
    else:
        pan = pan
    if tilt < 50:
        tilt = 50
    elif tilt >250:
        tilt = 250
    else:
        tilt = tilt
    file.write(str(pan) + '\n')
    file.write(str(tilt) + '\n')
    # Close opend file
    file.close()

#Functions Driving
def Stop():
    GPIO.output (MotorA_speed,GPIO.LOW)
    GPIO.output (MotorA_dir,GPIO.LOW)
    GPIO.output (MotorB_speed,GPIO.LOW)
    GPIO.output (MotorB_dir,GPIO.LOW)
    
def Forward():
    # switch MotorA on forwards
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    # switch MotorB on forwards
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)
    
def Forward_right():
    # switch MotorA on backwards
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    # switch MotorB on forwards
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)
    
def Forward_left():
    # switch MotorA on forwards
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    # switch MotorB on backwards
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)

def Backwards():
    # switch MotorA on backwards
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    # switch MotorB on backwards
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)    
    
def Backwards_right():
    # switch MotorA on forwards
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    # switch MotorB on backwards
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)
    
def Backwards_left():
    # switch MotorA on backwards
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    # switch MotorB on forwards
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)
    
#Function Pan and Tilt
def pan_left():
    cmd = 'echo 7=+10 > /dev/servoblaster'
    os.system(cmd)

def pan_right():
    cmd = 'echo 7=-10 > /dev/servoblaster'
    os.system(cmd)

def pan_neutral():
    cmd = 'echo 7=150 > /dev/servoblaster'
    os.system(cmd)

def pan_set_value(pan):
    pan = repr(pan)
    cmd = 'echo 7=' + pan + '> /dev/servoblaster'
    os.system(cmd)

def tilt_up():
    cmd = 'echo 6=-10 > /dev/servoblaster'
    os.system(cmd)

def tilt_down():
    cmd = 'echo 6=+10 > /dev/servoblaster'
    os.system(cmd)

def tilt_neutral():
    cmd = 'echo 6=150 > /dev/servoblaster'
    os.system(cmd)
    
def tilt_set_value(tilt):
    tilt = repr(tilt)
    cmd = 'echo 6=' + tilt + '> /dev/servoblaster'
    os.system(cmd)

#Function Sonor
def Sonar(): 
       while True:
           GPIO.setup(14, GPIO.OUT)
           GPIO.output(14, True)
           time.sleep(0.00001)
           GPIO.output(14, False)
           start = time.time()
           count = time.time()
           GPIO.setup(14, GPIO.IN)
           while GPIO.input(14)==0 and time.time()-count<0.1:
               start = time.time()
           stop=time.time()
           while GPIO.input(14)==1:
               stop = time.time()
           # Calculate pulse length
           elapsed = stop-start
           # Distance pulse travelled in that time is time
           # multiplied by the speed of sound (cm/s)
           distance = elapsed * 34000
           # That was the distance there and back so halve the value
           distance = distance / 2
           return distance
           time.sleep(1)

#Function LEDS and Buzzer
def LedBlue_on():
    GPIO.output(Led_blue,GPIO.HIGH)

def LedBlue_off():
    GPIO.output(Led_blue,GPIO.LOW)

def LedRed_on():
    GPIO.output(Led_red,GPIO.HIGH)

def LedRed_off():
    GPIO.output(Led_red,GPIO.LOW)

def Buzzer_on():
    GPIO.output(Buzzer,GPIO.HIGH)

def Buzzer_off():
    GPIO.output(Buzzer,GPIO.LOW)
   
#Emergency function to stop all output   
def Emergency():
    GPIO.output(Buzzer,GPIO.LOW)
    GPIO.output(Led_red,GPIO.LOW)
    GPIO.output(Led_blue,GPIO.LOW)
    GPIO.output (MotorA_speed,GPIO.LOW)
    GPIO.output (MotorA_dir,GPIO.LOW)
    GPIO.output (MotorB_speed,GPIO.LOW)
    GPIO.output (MotorB_dir,GPIO.LOW)
    GPIO.cleanup()
    
# Do something
#try:
#    LedBlue_on()
 #   time.sleep(1)
  #  LedBlue_off()
  #  time.sleep(1)
  #  LedRed_on()
  #  time.sleep(1)
  #  LedRed_off()
 #   time.sleep(1)
   # #Buzzer_on()
    #time.sleep(1)
    #Buzzer_off()
    #time.sleep(1)
    #Forward()
    #time.sleep(3)
    #Backwards()
    #time.sleep(3)
    #pan_right()
   # Emergency()
    
    
    #run the sonar
    #if (Sonar() > 10 ):
   #     LedBlue_on()
#except KeyboardInterrupt:
   # Emergency()
   # GPIO.cleanup()
test_pan = 200
test_tilt = 100
Write_Servo(test_pan, test_tilt)
pan_value, tilt_value = Read_Servo()
print pan_value
#pan_value1 = repr(pan_value)
print tilt_value
pan_neutral()
tilt_neutral()
time.sleep(1)
pan_set_value(pan_value)
tilt_set_value(tilt_value)