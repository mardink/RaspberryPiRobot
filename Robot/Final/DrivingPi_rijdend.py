#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import SocketServer
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

#define GPIO ports
MotorA_dir = 26
MotorA_speed = 24
MotorB_dir = 21
MotorB_speed = 19
Buzzer = 15

#Setup the GPIO ports
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

# define  the functions
# driving
def MotorLeftForward():
    GPIO.output(MotorB_speed, 0)
    GPIO.output(MotorB_dir, 1)

def MotorLeftBackward():
    GPIO.output(MotorB_speed, 1)
    GPIO.output(MotorB_dir, 0)

def MotorLeftOff():
    GPIO.output(MotorB_speed, 0)
    GPIO.output(MotorB_dir, 0)

def MotorRightForward():
    GPIO.output(MotorA_speed, 1)
    GPIO.output(MotorA_dir, 0)

def MotorRightBackward():
    GPIO.output(MotorA_speed, 0)
    GPIO.output(MotorA_dir, 1)

def MotorRightOff():
    GPIO.output(MotorA_speed, 0)
    GPIO.output(MotorA_dir, 0)

# Function to set all drives off
def MotorOff():
    MotorLeftOff()
    MotorRightOff()

# Pan and Tilt functions
# other functions
def BuzzerOn():
    GPIO.output(Buzzer, 1)

def BuzzerOff():
    GPIO.output(Buzzer, 0)



    

# Settings for the RemoteKeyBorg server
portListen = 9038                       # What messages to listen for (LEDB on an LCD)

# Class used to handle UDP messages
class PicoBorgHandler(SocketServer.BaseRequestHandler):
    # Function called when a new message has been received
    def handle(self):
        global isRunning

        request, socket = self.request          # Read who spoke to us and what they said
        print request
        request = request.upper()               # Convert command to upper case
        driveCommands = request.split(',')      # Separate the command into individual drives
        #driveCommands = request
        print driveCommands[0] # for debugging
        if driveCommands[0] == "1":
            MotorLeftBackward()
        elif driveCommands[1] == "1":
            MotorLeftForward()
        else: # turn motors off if no signal
            MotorLeftOff()
        if driveCommands[2] == "1":
            MotorRightForward()
        elif driveCommands[3] == "1":
            MotorRightBackward()
        else:
            MotorRightOff()
        if driveCommands[4] == "1":
            BuzzerOn()
        else:
            BuzzerOff()


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