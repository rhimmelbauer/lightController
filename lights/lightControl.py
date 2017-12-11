from pyHS100 import SmartPlug, SmartBulb, Discover
from colorConvertion import *
from .models import *

def get_bulbs():
	#get bulb ips.
	bulbs = Bulb.objects.all()
	for dev in Discover.discover().values():
		strBulb = str(dev).split()
		print(strBulb)
		if len(bulbs.filter(name=strBulb[3].strip('(),'))) < 1:
			print("new bulb")
			create_new_bulb(strBulb)
          
	#validate if they exist.
	#save insert bulbs in db.

def start_fresh():
	Bulb.objects.all().delete()
	for dev in Discover.discover().values():
		strBulb = str(dev).split()
		print(strBulb)
		create_new_bulb(strBulb)

def update_bulb(bulb):
	smartBulb = SmartBulb(bulb.ipAddr)
	if bulb.onOff:
		smartBulb.turn_on()
	else:
		smartBulb.turn_off()
	if smartBulb.is_color:
		hsv = rgb2hsv(int(bulb.rgbColor[0:2], 16),int(bulb.rgbColor[2:4], 16),int(bulb.rgbColor[4:6], 16))
		smartBulb.hsv = hsv

	smartBulb.brightness = bulb.brightness

def bulb_turn_on(bulb):
	smartBulb = SmartBulb(bulb.ipAddr)
	smartBulb.turn_on()
	bulb.onOff = True
	bulb.save()

def bulb_turn_off(bulb):
	smartBulb = SmartBulb(bulb.ipAddr)
	smartBulb.turn_off()
	bulb.onOff = False
	bulb.save()

def get_consumption():
	consumption = 0
	maxPerBulb = 8000
	numberOfBulbs = len(Bulb.objects.all())
	max = maxPerBulb*numberOfBulbs
	print("# bulbs: %s" % numberOfBulbs)
	bulbs = Bulb.objects.all()
	for bulb in bulbs:
		smartBulb = SmartBulb(bulb.ipAddr)
		print(str(smartBulb.get_emeter_realtime()))
		consumption = consumption + smartBulb.get_emeter_realtime()['power_mw']
	percent = int((consumption/max)*100)
	print(percent)
	return percent

def log_consumption():
	for bulb in Bulb.objects.all():
		smartBulb = SmartBulb(bulb.ipAddr)
		consumption = smartBulb.get_emeter_realtime()['power_mw']
		logBulb = LogBulb()
		logBulb.bulb = bulb
		logBulb.consumption = consumption
		logBulb.save()
		print(bulb)

def create_new_bulb(strBulb):
	newBulb = Bulb()
	name = strBulb[3].strip('(),')
	ipAddr = strBulb[2]
	if strBulb[5] == "True":
		onOff = True
	else:
		onOff = False
	rgbColor = "FFFFFF"
	brightness = int(strBulb[10].strip(','))
	if len(strBulb) > 14:
		is_color = True
	else:
		is_color = False
	
	newBulb.name = name
	newBulb.ipAddr = ipAddr
	newBulb.onOff = onOff
	newBulb.rgbColor = rgbColor
	newBulb.brightness = brightness
	newBulb.is_color = is_color
	newBulb.save()
