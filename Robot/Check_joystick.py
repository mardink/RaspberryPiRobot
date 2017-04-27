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

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("JoyBorg - Press [ESC] to quit")

Buttons = joystick.get_numbuttons()
print Buttons
Hat = joystick.get_numhats()
print Hat

hatvalue = joystick.get_hat(0)
print hatvalue

numaxis = joystick.get_numaxes()
print numaxis
ax1 = joystick.get_axis(0)
ax2 = joystick.get_axis(1)
ax3 = joystick.get_axis(2)
ax4 = joystick.get_axis(3)
ax5 = joystick.get_axis(4)


print ax1, ax2, ax3, ax4, ax5


