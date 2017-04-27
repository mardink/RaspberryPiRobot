#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_i2c.py
#  LCD test script using I2C backpack.
#  Supports 16x2 and 20x4 screens.
#
# Author : Matt Hawkins
# Date   : 20/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------
import time
import LCD_driver

lcd_init = LCD_driver.lcd_init
lcd_byte = LCD_driver.lcd_byte
LCD_CMD = LCD_driver.LCD_CMD
lcd_string = LCD_driver.lcd_string
LCD_LINE_1 = LCD_driver.LCD_LINE_1
LCD_LINE_2 = LCD_driver.LCD_LINE_2

def main():
  # Main program block

  # Initialise display
  lcd_init()

  while True:

    # Send some test
    lcd_string("Driver Test",LCD_LINE_1)
    lcd_string("Hallo Lynn",LCD_LINE_2)

    time.sleep(3)

    # Send some more text
    lcd_string("Driver Test",LCD_LINE_1)
    lcd_string(">     Hallo Lynn",LCD_LINE_2)

    time.sleep(3)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
