#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import os
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

# Set which GPIO pins the drive outputs are connected to
DRIVE_1 = 13 #ledBlue
DRIVE_2 = 11 #ledRed
DRIVE_3 = 13 #ledBlue
DRIVE_4 = 11 #ledRed

# Map of drives to pins
lDrives = [DRIVE_1, DRIVE_2, DRIVE_3, DRIVE_4]

# Function to set all drives off
def MotorOff():
    GPIO.output(DRIVE_1, GPIO.LOW)
    GPIO.output(DRIVE_2, GPIO.LOW)
    GPIO.output(DRIVE_3, GPIO.LOW)
    GPIO.output(DRIVE_4, GPIO.LOW)

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
        tiltUp = driveCommands[0]
        tiltDown = driveCommands[1]
        panRight = driveCommands[2]
        panLeft = driveCommands[3]
        
        if tiltUp == 'ON':
            tilt_up()
        elif tiltDown == 'ON':
            tilt_down()
        elif panRight == 'ON':
            pan_right()
        elif panLeft == 'ON':
            pan_left()

try:
    global isRunning

    # Start by turning all drives off
    MotorOff()
    raw_input('You can now turn on the power, press ENTER to continue')
    # Setup the UDP listener
    remoteKeyBorgServer = SocketServer.UDPServer(('', portListen), PicoBorgHandler)
    # Loop until terminated remotely
    isRunning = True
    while isRunning:
        remoteKeyBorgServer.handle_request()
    # Turn off the drives and release the GPIO pins
    print 'Finished'
    MotorOff()
    raw_input('Turn the power off now, press ENTER to continue')
    GPIO.cleanup()
except KeyboardInterrupt:
    # CTRL+C exit, turn off the drives and release the GPIO pins
    print 'Terminated'
    MotorOff()
    raw_input('Turn the power off now, press ENTER to continue')
    GPIO.cleanup()