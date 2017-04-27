import meArm
import time

def main():
    arm = meArm.meArm()
    arm.begin()

    while True:
        arm.openGripper()
        time.sleep(5)
        arm.closeGripper()

        arm.gotoPoint(0,100,50)
    return 0

if __name__ == '__main__':
    main()