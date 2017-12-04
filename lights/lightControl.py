from pyHS100 import SmartPlug, SmartBulb, Discover
from colorConvertion import *

def get_bulbs():
	#get bulb ips.
	for dev in Discover.discover().values():
	    print(dev)
	#validate if they exist.
	#save insert bulbs in db.

def update_bulb(bulb):
	smartBulb = SmartBulb(bulb.ipAddr)
	if bulb.onOff:
		smartBulb.turn_on()
	else:
		smartBulb.turn_off()

	hsv = rgb2hsv(int(bulb.rgbColor[0:2], 16),int(bulb.rgbColor[2:4], 16),int(bulb.rgbColor[4:6], 16))

        

    
