#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import os
import time
import pygame
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

#Joystick information

axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time

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

# Setup pygame and key states
global hadEvent
global moveForward
global moveForwardLeft
global moveForwardRight
global moveBackward
global moveBackwardRight
global moveBackwardLeft
global moveLeft
global moveRight
global tiltUp
global tiltNeutral
global tiltDown
global panLeft
global panNeutral
global panRight
global ledBlueOn
global ledBlueOff
global ledRedOn
global ledRedOff
global buzzerOn
global buzzerOff
global moveQuit
hadEvent = True
moveForward = False
moveForwardLeft = False
moveForwardRight = False
moveBackward = False
moveBackwardRight = False
moveBackwardLeft = False
moveLeft = False
moveRight = False
tiltUp = False
tiltNeutral = False
tiltDown = False
panLeft = False
panNeutral = False
panRight = False
ledBlueOn = False
ledBlueOff = False
ledRedOn = False
ledRedOff = False
buzzerOn = False
buzzerOff = False
moveQuit = False

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("Press control C to quit")

# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global moveForward
    global moveForwardLeft
    global moveForwardRight
    global moveBackward
    global moveBackwardRight
    global moveBackwardLeft
    global moveLeft
    global moveRight
    global tiltUp
    global tiltNeutral
    global tiltDown
    global panLeft
    global panNeutral
    global panRight
    global ledBlueOn
    global ledBlueOff
    global ledRedOn
    global ledRedOff
    global buzzerOn
    global buzzerOff
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
            
            # Determine forward / backward and left right values
            '''if upDown < -0.1 and leftRight > 0.1: #ForwardRight
                moveForward = False
                moveForwardRight = True
                moveForwardLeft = False
                moveBackward = False
                moveBackwardRight = False
                moveBackwardLeft = False
                
            elif upDown < -0.1 and leftRight < -0.1: #ForwardLeft
                moveForward = False
                moveForwardRight = False
                moveForwardLeft = True
                moveBackward = False
                moveBackwardRight = False
                moveBackwardLeft = False
            
            elif upDown > 0.1 and leftRight > 0.1: #BackwardRight
                moveForward = False
                moveForwardRight = False
                moveForwardLeft = False
                moveBackward = False
                moveBackwardRight = True
                moveBackwardLeft = False
            
            elif upDown > 0.1 and leftRight < -0.1: #BackwardLeft
                moveForward = False
                moveForwardRight = False
                moveForwardLeft = False
                moveBackward = False
                moveBackwardRight = False
                moveBackwardLeft = True    
            else:
                moveForward = False
                moveForwardRight = False
                moveForwardLeft = False
                moveBackward = False
                moveBackwardRight = False
                moveBackwardLeft = False
            '''
            # Determine forward / backward values
            if upDown < -0.1:
                moveForward = True
                moveForwardRight = False
                moveForwardLeft = False
                moveBackward = False
                moveBackwardRight = False
                moveBackwardLeft = False
                
            elif upDown > 0.1:
                moveForward = False
                moveForwardRight = False
                moveForwardLeft = False
                moveBackward = True
                moveBackwardRight = False
                moveBackwardLeft = False
                
            else:
                moveForward = False
                moveForwardRight = False
                moveForwardLeft = False
                moveBackward = False
                moveBackwardRight = False
                moveBackwardLeft = False
                
            # Determine Left / Right value    
            if leftRight > 0.1:
                moveForwardRight = False
                moveForwardLeft = False
                moveBackwardRight = False
                moveBackwardLeft = False
                moveLeft = False
                moveRight = True
            
            elif leftRight < -0.1:
                moveForwardRight = False
                moveForwardLeft = False
                moveBackwardRight = False
                moveBackwardLeft = False
                moveLeft = True
                moveRight = False
            else:
                moveLeft = False
                moveRight = False
                moveForwardRight = False
                moveForwardLeft = False
                moveBackwardRight = False
                moveBackwardLeft = False
                
        elif event.type == pygame.JOYHATMOTION:
            # A joystick has been moved, read hat positions (-1 to +1)
            hadEvent = True
            getHat = joystick.get_hat(0)
            panLeftRight = getHat[0] #First position is x coordinate right left movement
            tiltUpdown = getHat[1] #Second position is y coordinate. UP down movement
            
            # Determine Tilt values
            if tiltUpdown < -0.1:
                tiltUp = True
                tiltDown = False
                    
            elif tiltUpdown > 0.1:
                tiltUp = False
                tiltDown = True
                
            else:
                tiltUp = False
                tiltDown = False
                
            # Determine Left / Right value    
            if panLeftRight > 0.1:
                panLeft = True
                panRight = False
            
            elif panLeftRight < -0.1:
                panLeft = False
                panRight = True
            else:
                panLeft = False
                panRight = False
                   
           
        elif event.type == pygame.JOYBUTTONDOWN:
            # A joystick button has been pressed
            hadEvent = True
            Button1 = joystick.get_button(0)
            Button2 = joystick.get_button(1)
            
            if Button1:
                print "knop is 1 ingdrukt"
                LedBlue_on()
                panNeutral = True
            elif Button2:
                print "knop is 2 ingdrukt"
                LedBlue_off()
                tiltNeutral = True
        
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
            elif moveForwardLeft:
                steering_left()
                drive_forward()
            elif moveForwardRight:
                steering_right()
                drive_forward()
            elif moveBackwardLeft:
                steering_left()
                drive_backward()
            elif moveBackwardRight:
                steering_right()
                drive_backward()
            elif moveLeft:
                drive_forward()
                steering_left()
                time.sleep(1)
            elif moveRight:
                drive_forward()
                steering_right()
            elif moveForward:
                drive_forward()
            elif moveBackward:
                drive_backward()
            elif tiltUp:
                #tilt_up()
                LedBlue_on()
            elif tiltDown:
                #tilt_down()
                LedBlue_off()
            elif tiltNeutral:
                tilt_neutral()
            elif panRight:
                #pan_right()
                LedRed_on()
            elif panLeft:
                #pan_left()
                LedRed_off()
            elif panNeutral:
                pan_neutral()
            else:
                drive_stop()
                steering_stop()           
        # Wait for the interval period
        time.sleep(interval)
    # Disable all drives
    MotorOff()
except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    GPIO.cleanup()