#!/usr/bin/env python
# copyright martijn Hiddink 2016
# get the ipadres from your raspberry

# Load library functions we want
import socket
import fcntl
import struct

def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except IOError:
        return False # in case the adapter has no ipadres

# Check if eth0 is availble or Wifi
def ipadres_lookup():
    ipadres_cable = get_ip_address('eth0')
    ipadres_wifi = get_ip_address('wlan0')
    if ipadres_cable != False:
        return ipadres_cable
    elif ipadres_wifi != False:
        return ipadres_wifi
    else:
        return "No network available"

#print get_ip_address('eth0') #only for debugging
#print get_ip_address('wlan0') #only for debugging
#print ipadres_lookup() #only for debugging