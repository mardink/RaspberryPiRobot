#!/usr/bin/env python
# copyright martijn Hiddink

# Load library functions we want
import socket
import time
#import pygame
import RPi.GPIO as GPIO
import spidev
import os
import wiringpi2 as wiringpi

# Settings for the Client
broadcastIP = '192.168.2.25'           # IP address to send to, 255 in one or more positions is a broadcast / wild-card
broadcastPort = 9038                    # What message number to send with
interval = 0.1                          # Time between updates in seconds, smaller responds faster but uses more processor time
regularUpdate = True                    # If True we send a command at a regular interval, if False we only send commands when keys are pressed or released

# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)       # Create the socket
sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)                        # Enable broadcasting (sending to many IPs based on wild-cards)
sender.bind(('0.0.0.0', 0))                                                         # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)

GPIO.setmode(GPIO.BOARD) #Use the pinnumbers easier for different RPI
GPIO.setwarnings(False)

#define MCP23017 and Wiringpi parameters
pin_base = 65       # lowest available starting number is 65
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND
wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address

#define GPIO ports
Button_Left_up = 26 #gpio input
Button_Left_down = 7 #gpio input
Button_Right_down = 11 #gpio input
Button_Right_up = 13 #gpio input
MCP_LED_White = 65 #MCP WiringPI port GPIOA0
MCP_LED_Green = 66 #MCP WiringPI port GPIOA1
MCP_LED_Red = 67 #MCP WiringPI port GPIOA2
MCP_Switch = 72  #MCP WiringPI port GPIOA7

#Setup the GPIO ports
GPIO.setup(Button_Left_up, GPIO.IN)
GPIO.setup(Button_Left_down, GPIO.IN)
GPIO.setup(Button_Right_up, GPIO.IN)
GPIO.setup(Button_Right_down, GPIO.IN)

#setup the MCP23017 ports
wiringpi.pinMode(MCP_LED_White, 1) #set as output
wiringpi.pinMode(MCP_LED_Green, 1) #set as output
wiringpi.pinMode(MCP_LED_Red, 1) #set as output
wiringpi.pinMode(MCP_Switch, 0) #set as input
wiringpi.digitalWrite(MCP_LED_White, 0)    # sets GPA0 to 0 (0V, off)
wiringpi.digitalWrite(MCP_LED_Green, 0)    # sets GPA0 to 0 (0V, off)
wiringpi.digitalWrite(MCP_LED_Red, 0)    # sets GPA0 to 0 (0V, off)

# If this program starts running, so working then turn on the green LED
wiringpi.digitalWrite(MCP_LED_Green, 1)    # Indication that program is running

# Setup Variables
global hadEvent
global moveLeftForward
global LeftStop
global moveLeftBackward
global moveRightForward
global RightStop
global moverightBackward
global TiltUp
global TiltDown
global TiltNeutral
global PanLeft
global PanRight
global PanNeutral
global speed
global ledBlue
global LedRed
global Buzzer
global StepperStop
global StepperRight
global Stepperleft
global Photo
global moveQuit

hadEvent = True
moveLeftForward = False
LeftStop = False
moveLeftBackward = False
moveRightForward = False
RightStop = False
moverightBackward = False
TiltUp = False
TiltDown = False
TiltNeutral = False
PanLeft = False
PanRight = False
PanNeutral = False
speed = False
ledBlue = False
LedRed = False
Buzzer = False
StepperStop = False
StepperRight = False
Stepperleft = False
Photo = False
moveQuit = False

def handler():
    # Variables accessible outside this function
    global hadEvent
    global moveLeftForward
    global LeftStop
    global moveLeftBackward
    global moveRightForward
    global RightStop
    global moverightBackward
    global TiltUp
    global TiltDown
    global TiltNeutral
    global PanLeft
    global PanRight
    global PanNeutral
    global speed
    global ledBlue
    global LedRed
    global Buzzer
    global StepperStop
    global StepperRight
    global Stepperleft
    global Photo
    global moveQuit
    #driving commands
    if ( GPIO.input(Button_Left_up) == False ):
        moveLeftForward = True
    else:
        moveLeftForward = False
    if ( GPIO.input(Button_Left_down) == False ):
        moveLeftBackward = True
    else:
        moveLeftBackward = False
    if ( GPIO.input(Button_Right_up) == False ):
        moveRightForward = True
    else:
        moveRightForward = False
    if ( GPIO.input(Button_Right_down) == False ):
        moverightBackward = True
    else:
        moverightBackward = False
    #Pan and Tilt commands

'''
#Define MCP3008 analog to digital converter
# SOMS WERKT HET NIET TYP DAN IN TERMINAL sudo modprobe spi-bcm2708
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Define sensor channels
swt_channel = 2 #Button function joystick
vrx_channel = 1 #horizontal movement joystick
vry_channel = 0 # vertical movement joystick
potmeter_channel = 3 #Potmeter for speed adjustment


#reading all the inputs

# Define delay between readings (s)
delay = 0.1  #standard setting 0.5

while True:

  # Read the joystick position data
  vrx_pos = ReadChannel(vrx_channel)
  vry_pos = ReadChannel(vry_channel)

  # Read switch state
  swt_val = ReadChannel(swt_channel)

  #Read potmeter
  speed = ReadChannel(potmeter_channel)

  # Print out results
  print "--------------------------------------------"
  print("X : {}  Y : {}  Switch : {} Speed : {}".format(vrx_pos,vry_pos,swt_val,speed))

  # Wait before repeating loop
  time.sleep(delay)
'''



#Send the instructions to the Robot
try:
    #print "Press [ESC] to quit"
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        handler()
        if hadEvent or regularUpdate:
            # Keys have changed, generate the command list based on keys

            driveCommands = ['0', '0', '0', '0']                    # Default to do not change
            if moveQuit:
                break
            elif moveLeftForward:
                driveCommands[0] = '1'
            elif moveLeftBackward:
                driveCommands[1] = '1'
            elif moveRightForward:
                driveCommands[2] = '1'
            elif moverightBackward:
                driveCommands[3] = '1'
            else:
                # None of our expected keys, stop
                driveCommands[0] = '0'
                driveCommands[1] = '0'
                driveCommands[2] = '0'
                driveCommands[3] = '0'
            # Send the drive commands
            command = ''
            for driveCommand in driveCommands:
                command += driveCommand + ','
            command = command[:-1]                                  # Strip the trailing comma
            print (command)                                         #For debugging see what the command is
            sender.sendto(command, (broadcastIP, broadcastPort))
        # Wait for the interval period
        time.sleep(interval)
    # Inform the server to stop
    sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
    # CTRL+C exit, inform the server to stop
    sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
    wiringpi.digitalWrite(MCP_LED_Green, 0)    # Indication that program is stopping
    wiringpi.digitalWrite(MCP_LED_Red, 1)    # Indication that program is stopping
    time.sleep(1)
    wiringpi.digitalWrite(MCP_LED_Red, 0)    # Indication that program is stopping
