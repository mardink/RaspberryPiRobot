#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import SocketServer
import os
import time

import RPi.GPIO as GPIO

import LCD_driver_drivingpi as LCD # beacuase this is for the old PI other adress
import ipadres

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

#load the LCD driver
LCD.lcd_init()

#define GPIO ports
MotorA_dir = 26
MotorA_speed = 24
MotorB_dir = 21
MotorB_speed = 19
Buzzer = 15
LED_blue = 7
LED_red = 11
Switch_shutdown = 16

#Setup the GPIO ports
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.setup(LED_blue, GPIO.OUT)
GPIO.setup(LED_red, GPIO.OUT)
GPIO.setup(Switch_shutdown, GPIO.IN)

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

# other functions
def BuzzerOn():
    GPIO.output(Buzzer, 1)

def BuzzerOff():
    GPIO.output(Buzzer, 0)

def shutdown():
    LCD.lcd_string("System is shutting down", LCD.LCD_LINE_1)
    LCD.lcd_string("In 3 seconds", LCD.LCD_LINE_2)
    time.sleep(3)
    os.system("sudo shutdown -h now")

def reboot():
    LCD.lcd_string("System is rebooting", LCD.LCD_LINE_1)
    LCD.lcd_string("In 3 seconds", LCD.LCD_LINE_2)
    time.sleep(3)
    os.system("sudo reboot")

# Settings for the RemoteKeyBorg server
portListen = 9038                       # What messages to listen for (LEDB on an LCD)

# Class used to handle UDP messages
class PicoBorgHandler(SocketServer.BaseRequestHandler):
    # Function called when a new message has been received
    def handle(self):
        global isRunning
        request, socket = self.request          # Read who spoke to us and what they said
        #print request
        request = request.upper()               # Convert command to upper case
        driveCommands = request.split(',')      # Separate the command into individual drives
        #lcd_data =  str(request)
        #lcd_data = lcd_data.replace(',', '')
        #print lcd_data
        #driveCommands = request
        #print driveCommands[0] # for debugging
        LCD.lcd_string("Recieving data", LCD.LCD_LINE_1)
        LCD.lcd_string(lcd_data, LCD.LCD_LINE_2)
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
        #if driveCommands[10] == "1":
        #    BuzzerOn()
        #else:
        #    BuzzerOff()
        if driveCommands[4] == "1":
            pan_left()
        if driveCommands[5] == "1":
            pan_right()
        if driveCommands[6] == "1":
            tilt_up()
        if driveCommands[7] == "1":
            tilt_down()
        if driveCommands[8] == "1":
            pan_neutral()
        if driveCommands[9] == "1":
            tilt_neutral()

try:
    global isRunning

    # Start by turning all drives off
    MotorOff()
    raw_input('You can now turn on the power, press ENTER to continue')
    LCD.lcd_string("Ready to recieve data on", LCD.LCD_LINE_1)
    LCD.lcd_string(ipadres.ipadres_lookup(), LCD.LCD_LINE_2)
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
    LCD.lcd_byte(0x01, LCD.LCD_CMD)