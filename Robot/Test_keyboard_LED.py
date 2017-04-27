#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

Led_blue = 21 
Led_red = 17
Buzzer = 22


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Led_red,GPIO.OUT) 
GPIO.setup(Led_blue,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.refresh()
    if key == curses.KEY_UP: 
        GPIO.output(Led_red,GPIO.HIGH)
        time.sleep(1)
    elif key == curses.KEY_DOWN: 
        GPIO.output(Led_blue,GPIO.HIGH)
        time.sleep(1)
    elif key== curses.KEY_HOME:
        GPIO.output(Led_red,GPIO.LOW)
        GPIO.output(Led_blue,GPIO.LOW)
        time.sleep(1)

curses.endwin()