#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import time
import pygame
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Settings 
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

#Set the gpio ports

GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)
GPIO.setup(Led_blue, GPIO.OUT)
GPIO.setup(Led_red, GPIO.OUT)

axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
SmallaxisUpDown = 6                          # Joystick axis to read for up / down position
SmallaxisUpDownInverted = False              # Set this to True if up and down appear to be swapped
SmallaxisLeftRight = 5                       # Joystick axis to read for left / right position
SmallaxisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time

# Function to set all drives off
def MotorOff():
    GPIO.output(MotorA_dir, GPIO.LOW)
    GPIO.output(MotorA_speed, GPIO.LOW)
    GPIO.output(MotorB_dir, GPIO.LOW)
    GPIO.output(MotorB_speed, GPIO.LOW)


# Setup pygame and key states
global hadEvent
global moveUp
global moveDown
global moveLeft
global moveRight
global moveQuit
hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("JoyBorg - Press [ESC] to quit")

# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global moveUp
    global moveDown
    global moveLeft
    global moveRight
    global moveQuit
    # Handle each event individually
    for event in events:
        if event.type == pygame.QUIT:
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = True
        elif event.type == pygame.KEYUP:
            # A key has been released, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = False
        elif event.type == pygame.JOYAXISMOTION:
            # A joystick has been moved, read axis positions (-1 to +1)
            hadEvent = True
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            # Invert any axes which are incorrect
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
            # Determine Up / Down values
            if upDown < -0.1:
                moveUp = True
                moveDown = False
            elif upDown > 0.1:
                moveUp = False
                moveDown = True
            else:
                moveUp = False
                moveDown = False
            # Determine Left / Right values
            if leftRight < -0.1:
                moveLeft = True
                moveRight = False
            elif leftRight > 0.1:
                moveLeft = False
                moveRight = True
            else:
                moveLeft = False
                moveRight = False
try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent:
            # Keys have changed, generate the command list based on keys
            hadEvent = False
            if moveQuit:
                break
            elif moveLeft:
                leftState = GPIO.LOW
                rightState = GPIO.HIGH
            elif moveRight:
                leftState = GPIO.HIGH
                rightState = GPIO.LOW
            elif moveUp:
                leftState = GPIO.HIGH
                rightState = GPIO.HIGH
            else:
                leftState = GPIO.LOW
                rightState = GPIO.LOW
            GPIO.output(Led_blue, leftState)
            GPIO.output(Led_red, rightState)
        # Wait for the interval period
        time.sleep(interval)
    # Disable all drives
    MotorOff()
except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    GPIO.cleanup()