from pyHS100 import SmartPlug, SmartBulb, Discover
from colorConvertion import *

def get_bulbs():
	#get bulb ips.
	for dev in Discover.discover().values():
		print(dev)
	#validate if they exist.
	#save insert bulbs in db.

def update_bull(bulb):
	smartBulb = SmartBulb(bulb.ipAddr)
	if bulb.onOff:
		smartBulb.turn_on()
	else:
		smartBulb.turn_off()

	hsv = rgb2hsv(int(bulb.rgb[0:2], 16),int(bulb.rgb[2:4], 16),int(bulb.rgb[4:6], 16))



    
