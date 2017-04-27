import wiringpi2 as wiringpi  
from time import sleep  
  
pin_base = 65       # lowest available starting number is 65  
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND  
  
wiringpi.wiringPiSetup()                    # initialise wiringpi  
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address  

MCP_LED_WHITE = 65
MCP_LED_GREEN = 66
MCP_LED_RED = 67


wiringpi.pinMode(MCP_LED_WHITE, 1)         # sets GPA0 to output  
wiringpi.digitalWrite(MCP_LED_WHITE, 0)    # sets GPA0 to 0 (0V, off)
wiringpi.pinMode(MCP_LED_GREEN, 1)
wiringpi.digitalWrite(MCP_LED_GREEN, 0)
wiringpi.pinMode(MCP_LED_RED, 1)
wiringpi.digitalWrite(MCP_LED_RED, 0)
sleep(1)
wiringpi.digitalWrite(MCP_LED_WHITE, 1)
sleep(1)
wiringpi.digitalWrite(MCP_LED_GREEN, 1)
sleep(1)
wiringpi.digitalWrite(MCP_LED_RED, 1)
sleep(1)
wiringpi.digitalWrite(MCP_LED_WHITE, 0)
wiringpi.digitalWrite(MCP_LED_GREEN, 0)
wiringpi.digitalWrite(MCP_LED_RED, 0)



wiringpi.pinMode(72, 0)         # sets GPA7 to input  
wiringpi.pullUpDnControl(72, 2) # set internal pull-up   
  


