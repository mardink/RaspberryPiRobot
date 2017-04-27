import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


coil_A_1_pin = 7 #BCM gpio4 
coil_A_2_pin = 11 #BCM gpio17
coil_B_1_pin = 16 #BCM gpio23
coil_B_2_pin = 10 #BCM gpio15


GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)



def forward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)

def backwards(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)

  
def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

try:
    while True:
    
        delay = raw_input("Delay between steps (milliseconds)?") #seems 2 ms is minimum for motor
        steps = raw_input("How many steps forward? ") #512 steps is one turn
        forward(int(delay) / 1000.0, int(steps))
        steps = raw_input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))
except KeyboardInterrupt:
  print "  Quit" 
  setStep(0,0,0,0)
  # Reset GPIO settings
  GPIO.cleanup()
