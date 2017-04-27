#!/usr/bin/env python
import time
import os

# define direction functions

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
    
pan_neutral()
time.sleep(1)
pan_left()
time.sleep(1)
pan_neutral()
time.sleep(1)
pan_right()
time.sleep(1)
pan_neutral()
tilt_neutral()
time.sleep(1)
tilt_up()
time.sleep(1)
tilt_neutral()
time.sleep(1)
tilt_down()
time.sleep(1)
tilt_neutral()