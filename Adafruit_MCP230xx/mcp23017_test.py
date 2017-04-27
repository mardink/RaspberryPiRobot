# Use busnum = 0 for older Raspberry Pi's (pre 512MB)
#mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)
 
# Use busnum = 1 for new Raspberry Pi's (512MB)
mcp = Adafruit_MCP230xx(busnum = 1, address = 0x20, num_gpios = 16)



# Set pin 7 to input with the pullup resistor enabled
mcp.pullup(7, 1)

# Read pin 3 and display the results
print "%d: %x" % (3, mcp.input(3) >> 3)

# Set pin 0 to output (you can set pins 0..15 this way)
mcp.config(0, OUTPUT)

# Set pin 0 High
mcp.output(0, 1)  

# Set pin 0 Low
mcp.output(0, 0)