#!/usr/bin/python
#--------------------------------------
# This script reads data from a
# MCP3008 ADC device using the SPI bus.
#
# Analogue joystick version!
#
# Author : Matt Hawkins
# Date   : 17/04/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# SOMS WERKT HET NIET TYP DAN IN TERMINAL sudo modprobe spi-bcm2708
import spidev
import time
import os
 
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
# (channels 3 to 7 unused)
swt_channel = 2
vrx_channel = 1
vry_channel = 0
potmeter_channel = 3
 
# Define delay between readings (s)
delay = 0.5
 
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