#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import os
import sys
import time
import pygame
import SocketServer
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM) #used for chip numbering
GPIO.setmode(GPIO.BOARD) #used for board numbering, better when using multiple types of pi
GPIO.setwarnings(False)
GPIO.cleanup()

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

#Set the gpio ports

GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)
GPIO.setup(Led_blue, GPIO.OUT)
GPIO.setup(Led_red, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)


# Function to set all drives off
def MotorOff():
    GPIO.output(MotorA_dir, GPIO.LOW)
    GPIO.output(MotorA_speed, GPIO.LOW)
    GPIO.output(MotorB_dir, GPIO.LOW)
    GPIO.output(MotorB_speed, GPIO.LOW)
    
# switch Driving Motor on backwards
def drive_backward():
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)

# switch Driving Motor on forwards
def drive_forward():
    #check_front()
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)    

# switch Driving Motor off
def drive_stop():
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 0)

# switch Steering Motor left
def steering_left():
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    
# switch Steering Motor right
def steering_right():
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    
# switch Steering Motor off
def steering_stop():
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 0)

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

def tilt_up():
    cmd = 'echo 6=-10 > /dev/servoblaster'
    os.system(cmd)

def tilt_down():
    cmd = 'echo 6=+10 > /dev/servoblaster'
    os.system(cmd)
        
def tilt_neutral():
    cmd = 'echo 6=150 > /dev/servoblaster'
    os.system(cmd)

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

def Server_Ready():
    LedBlue_on()
    Buzzer_on()
    time.sleep(0.5)
    LedBlue_off()
    Buzzer_off()
    time.sleep(0.5)
    LedBlue_on()
    Buzzer_on()
    time.sleep(0.5)
    LedBlue_off()
    Buzzer_off()
    time.sleep(0.5)

#Define sonar functions for avoiding objects
def sonar():
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
    distance = elapsed * 34029
    # That was the distance there and back so halve the value
    distance = distance / 2
    return distance

def sonarAlarm():
    LedBlue_on()
    Buzzer_on()
    LedRed_off()
    time.sleep(0.5)
    LedBlue_off()
    Buzzer_off()
    LedRed_on()
    time.sleep(0.5)
    LedBlue_on()
    Buzzer_on()
    LedRed_off()
    time.sleep(0.5)
    LedBlue_off()
    Buzzer_off()
    LedRed_on()
    time.sleep(0.5)
    LedBlue_off()
    Buzzer_off()
    LedRed_off()

def sonarAvoid():
    drive_backward()
    steering_right()
    time.sleep(2)
    steering_stop()
    drive_stop()

def check_front():
    dist = sonar()
    safe_distance = 15 # Keep this distance in cm to objects
    if dist < safe_distance:
        sonarAvoid()
        dist = sonar()
        if dist < safe_distance:
            print('Too close, ',dist)
            sonarAlarm()

# Settings for the RemoteKeyBorg server
portListen = 9038                       # What messages to listen for (LEDB on an LCD)

# Class used to handle UDP messages
class PicoBorgHandler(SocketServer.BaseRequestHandler):
    # Function called when a new message has been received
    def handle(self):
        global isRunning

        request, socket = self.request          # Read who spoke to us and what they said
        request = request.upper()               # Convert command to upper case
        driveCommands = request.split(',')      # Separate the command into individual drives
        #Get joystick signals 
        moveForward = driveCommands[0]
        moveForwardLeft = driveCommands[1]
        moveForwardRight = driveCommands[2]
        moveBackward = driveCommands[3]
        moveBackwardRight = driveCommands[4]
        moveBackwardLeft = driveCommands[5]
        moveLeft = driveCommands[6]
        moveRight = driveCommands[7]
        hatUp = driveCommands[8]
        hatDown = driveCommands[9]
        hatLeft = driveCommands[10]
        hatRight = driveCommands[11]
        speedUp = driveCommands[12]
        speedDown = driveCommands[13] 
        joyButton1 = driveCommands[14]
        joyButton2 = driveCommands[15]
        joyButton3 = driveCommands[16]
        joyButton4 = driveCommands[17]
        joyButton5 = driveCommands[18]
        joyButton6 = driveCommands[19]
        joyButton7 = driveCommands[20]
        joyButton8 = driveCommands[21]
        joyButton9 = driveCommands[22]
        joyButton10 = driveCommands[23]
        joyButton11 = driveCommands[24]
        joyButton12 = driveCommands[25]
        
        #Assign Joystick input to functions
        if moveForward == 'ON':
            check_front()
            drive_forward()
        elif moveBackward == 'ON':
            drive_backward()
        elif moveLeft == 'ON':
            steering_left()
        elif moveRight == 'ON':
            steering_right()        
        elif hatUp == 'ON':
            tilt_up()
        elif hatDown == 'ON':
            tilt_down()
        elif hatRight == 'ON':
            pan_right()
        elif hatLeft == 'ON':
            pan_left()
        elif joyButton1 == 'ON':
            print "Knop 1"
            print (sonar())
        elif joyButton2 == 'ON':
            print "Knop 2"
        elif joyButton3 == 'ON':
            print "Knop 3"
            pan_neutral()
        elif joyButton4 == 'ON':
            print "Knop 4"            
        elif joyButton5 == 'ON':
            print "Knop 5"
            tilt_neutral()
        elif joyButton6 == 'ON':
            print "Knop 6, Program stops"
            #sys.exit()
        else:
            MotorOff()

try:
    global isRunning

    # Start by turning all drives off
    MotorOff()
    #raw_input('You can now turn on the power, press ENTER to continue')
    Server_Ready()
    # Setup the UDP listener
    remoteKeyBorgServer = SocketServer.UDPServer(('', portListen), PicoBorgHandler)
    # Loop until terminated remotely
    isRunning = True
    while isRunning:
        remoteKeyBorgServer.handle_request()
    # Turn off the drives and release the GPIO pins
    print 'Finished'
    MotorOff()
    #raw_input('Turn the power off now, press ENTER to continue')
    GPIO.cleanup()
except KeyboardInterrupt:
    # CTRL+C exit, turn off the drives and release the GPIO pins
    print 'Terminated'
    MotorOff()
    raw_input('Turn the power off now, press ENTER to continue')
    GPIO.cleanup()