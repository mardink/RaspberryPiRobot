#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DemoIK.py - York Hack Space May 2014
#  Simple demo of meArm library to walk through some points defined in Cartesian coordinates

import meArm
import PCA9685

pwm = PCA9685()

def main():
    arm = meArm.meArm()
    arm.begin()

    try:
        while True:
            arm.openGripper()
            arm.closeGripper()
            arm.openGripper()
            arm.closeGripper()
            arm.openGripper()

            arm.gotoPoint(0, 150, 50)
            arm.gotoPoint(0, 150, 0)
            arm.gotoPoint(0, 150, 150)
            arm.gotoPoint(0, 150, 50)
            arm.gotoPoint(-150, 150, 50)
            arm.gotoPoint(150, 150, 50)
            arm.gotoPoint(0, 150, 50)
            arm.gotoPoint(0, 100, 50)

    except KeyboardInterrupt:
    # CTRL+C exit, inform the server to stop
        pwm.set_pwm(0, 0, 0)  # switch off signal
        pwm.set_pwm(1, 0, 0)  # switch off signal
        pwm.set_pwm(2, 0, 0)  # switch off signal
        pwm.set_pwm(3, 0, 0)  # switch off signal
if __name__ == '__main__':
    main()
