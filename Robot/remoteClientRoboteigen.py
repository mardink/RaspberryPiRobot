#!/usr/bin/env python


# Load library functions we want
import socket
import time
import pygame

# Settings for the RemoteJoyBorg client
broadcastIP = '192.168.1.25'           # IP address to send to, 255 in one or more positions is a broadcast / wild-card
broadcastPort = 9038                    # What message number to send with
leftDrive = 1                           # Drive number for left motor
rightDrive = 4                         # Drive number for right motor
interval = 0.1                          # Time between updates in seconds, smaller responds faster but uses more processor time
regularUpdate = True                    # If True we send a command at a regular interval, if False we only send commands when keys are pressed or released
axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped

# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)       # Create the socket
sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)                        # Enable broadcasting (sending to many IPs based on wild-cards)
sender.bind(('0.0.0.0', 0))                                                         # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)

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
global hatUp
global hatDown
global hatLeft
global hatRight
global speedUp
global speedDown 
global joyButton1
global joyButton2
global joyButton3
global joyButton4
global joyButton5
global joyButton6
global joyButton7
global joyButton8
global joyButton9
global joyButton10
global joyButton11
global joyButton12
global allButtons
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
hatUp = False
hatDown = False
hatLeft = False
hatRight = False
speedUp = False
speedDown  = False
joyButton1 = False
joyButton2 = False
joyButton3 = False
joyButton4 = False
joyButton5 = False
joyButton6 = False
joyButton7 = False
joyButton8 = False
joyButton9 = False
joyButton10 = False
joyButton11 = False
joyButton12 = False
allButtons = False
moveQuit = False

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("RemoteKeyBorg - Press [ESC] to quit")

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
    global hatUp
    global hatDown
    global hatLeft
    global hatRight
    global speedUp
    global speedDown 
    global joyButton1
    global joyButton2
    global joyButton3
    global joyButton4
    global joyButton5
    global joyButton6
    global joyButton7
    global joyButton8
    global joyButton9
    global joyButton10
    global joyButton11
    global joyButton12
    global allButtons
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
                moveForward = True
                moveBackward = False
            elif upDown > 0.1:
                moveForward = False
                moveBackward = True
            else:
                moveForward = False
                moveBackward = False
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
        elif event.type == pygame.JOYHATMOTION:
            # A joystick has been moved, read hat positions (-1 to +1)
            hadEvent = True
            getHat = joystick.get_hat(0)
            panLeftRight = getHat[0] #First position is x coordinate right left movement
            tiltUpdown = getHat[1] #Second position is y coordinate. UP down movement
            tiltUpdown = - tiltUpdown
            panLeftRight = - panLeftRight
            
            # Determine Tilt values
            if tiltUpdown < -0.1:
                hatUp = True
                hatDown = False
                    
            elif tiltUpdown > 0.1:
                hatUp = False
                hatDown = True
                
            else:
                hatUp = False
                hatDown = False
                
            # Determine Left / Right value    
            if panLeftRight > 0.1:
                hatLeft = True
                hatRight = False
            
            elif panLeftRight < -0.1:
                hatLeft = False
                hatRight = True
            else:
                hatLeft = False
                hatRight = False
                   
        elif event.type == pygame.JOYBUTTONDOWN: #Determine button state button pressed
            if joystick.get_button(0):
                joyButton1 = True
            elif joystick.get_button(1):
                joyButton2 = True
            elif joystick.get_button(2):
                joyButton3 = True
            elif joystick.get_button(3):
                joyButton4 = True
            elif joystick.get_button(4):
                joyButton5 = True
            elif joystick.get_button(5):
                joyButton6 = True
            else:
                joyButton1 = False
                joyButton2 = False
                joyButton3 = False
                joyButton4 = False
                joyButton5 = False
                joyButton6 = False

        elif event.type == pygame.JOYBUTTONUP: #determin button released
            if joystick.get_button(0):
                joyButton1 = False
            elif joystick.get_button(1):
                joyButton2 = False
            elif joystick.get_button(2):
                joyButton3 = False
            elif joystick.get_button(3):
                joyButton4 = False
            elif joystick.get_button(4):
                joyButton5 = False
            elif joystick.get_button(5):
                joyButton6 = False
            else:
                joyButton1 = False
                joyButton2 = False
                joyButton3 = False
                joyButton4 = False
                joyButton5 = False
                joyButton6 = False
        

try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent or regularUpdate:
            # Keys have changed, generate the command list based on keys
            hadEvent = False
            driveCommands = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']   # Default to do not change
            if moveQuit:
                break
            elif moveLeft:
                driveCommands[6] = 'ON'
            elif moveRight:
                driveCommands[7] = 'ON'
            elif moveForward:
                driveCommands[0] = 'ON'
            elif moveBackward:
                driveCommands[3] = 'ON'
            elif hatUp:
                driveCommands[8] = 'ON'
            elif hatDown:
                driveCommands[9] = 'ON'
            elif hatLeft:
                driveCommands[10] = 'ON'
            elif hatRight:
                driveCommands[11] = 'ON'
            elif joyButton1:
                driveCommands[14] = 'ON'
            elif joyButton2:
                driveCommands[15] = 'ON'
            elif joyButton3:
                driveCommands[16] = 'ON'
            elif joyButton4:
                driveCommands[17] = 'ON'
            elif joyButton5:
                driveCommands[18] = 'ON'
            elif joyButton6:
                driveCommands[19] = 'ON'
            elif allButtons:
                driveCommands[14] = 'OFF'
                driveCommands[15] = 'OFF'
            else:
                # None of our expected keys, stop
                driveCommands[6] = 'OFF'
                driveCommands[7] = 'OFF'
                driveCommands[0] = 'OFF'
                driveCommands[3] = 'OFF'
                driveCommands[14] = 'OFF'
                driveCommands[15] = 'OFF'
# Send the drive commands
            command = ''
            for driveCommand in driveCommands:
                command += driveCommand + ','
            command = command[:-1]                                  # Strip the trailing comma
            sender.sendto(command, (broadcastIP, broadcastPort))
        # Wait for the interval period
        time.sleep(interval)
    # Inform the server to stop
    sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
    # CTRL+C exit, inform the server to stop
    sender.sendto('ALLOFF', (broadcastIP, broadcastPort))