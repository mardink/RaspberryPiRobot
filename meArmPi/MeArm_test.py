import meArm

def main():
    arm = meArm.meArm()
    arm.begin()

    while True:
        arm.openGripper()
        arm.closeGripper()
        arm.openGripper()
        arm.closeGripper()
        arm.openGripper()

        #Go up and left to grab something
        #arm.gotoPoint(-80,100,140)
        #arm.closeGripper()
        #Go down, forward and right to drop it
        #arm.gotoPoint(70,200,10)
        #arm.openGripper()
        #Back to start position
        arm.gotoPoint(0,100,50)
    return 0

if __name__ == '__main__':
    main()