#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

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

GPIO.setup(Button_right, GPIO.IN)
GPIO.setup(Button_left, GPIO.IN)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)
GPIO.setup(Led_blue, GPIO.OUT)
GPIO.setup(Led_red, GPIO.OUT)

#set the functions
# switch Driving Motor on backwards
def drive_backwards():
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)

#set the safety distance for obstacles
safety_distance = 10

# switch Driving Motor on forwards
def drive_forwards():
    try:    
        while True:
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
            distance = elapsed * 34000
            # That was the distance there and back so halve the value
            distance = distance / 2
                        
            if safety_distance<distance:
                GPIO.output (Led_blue, 1)
                GPIO.output (Led_red, 0)
                GPIO.output (MotorB_speed, 0)
                GPIO.output (MotorB_dir, 1)
            else:
                GPIO.output (Led_blue, 0)
                GPIO.output (Led_red, 1)
                drive_stop()
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
    

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

def drive_avoid():
    steering_left()
    drive_backwards()
    time.sleep(1)
    drive_stop()
    steering_stop()
    

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.refresh()
    if key == curses.KEY_UP: 
        drive_forwards()
        time.sleep(0.1)
    elif key == curses.KEY_DOWN:
        drive_backwards()
        time.sleep(0.1)
    elif key == curses.KEY_RIGHT:
        steering_right()
        time.sleep(0.1)
    elif key == curses.KEY_LEFT:
        steering_left()
        time.sleep(0.1)
    elif key == curses.KEY_HOME:
        drive_stop()
        steering_stop()
        time.sleep(0.1)
    
curses.endwin()
