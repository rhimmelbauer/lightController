from django.shortcuts import render, redirect, get_object_or_404
from random import randint
from django.db.models import Sum
from .models import *
from .forms import *
from .lightControl import *

def home(request):
	log_consumption()
	get_bulbs()
	zones = Zone.objects.all()
	bulbs = Bulb.objects.all()
	bulbsNoZone = Bulb.objects.exclude(zone__isnull=False)
	return render(request, 'home.html', {'bulbs': bulbs, 'bulbsNoZone': bulbs, 'zones': zones})

def new_zone(request):
	log_consumption()
	if request.method == 'POST':
		form = NewZone(request.POST)
		if form.is_valid():
			zone = form.save(commit=False)
			zone.save()
			return redirect('home')
	else:
		form = NewZone()
		return render(request, 'new_zone.html', {'form': form})

def edit_bulb(request, pk):
	log_consumption()
	if request.method == 'POST':
		form = CustomBulb(request.POST)
		if form.is_valid():
			bulb = Bulb.objects.get(pk=pk)
			bulbForm = form.save(commit=False)
			bulb.onOff = bulbForm.onOff
			bulb.rgbColor = bulbForm.rgbColor
			bulb.brightness = bulbForm.brightness
			bulb.zone = bulbForm.zone
			bulb.save()
			update_bulb(bulb)
			return redirect('home')
		else:
			return redirect('home')

	else:
		form = CustomBulb()
		bulb = get_object_or_404(Bulb, pk=pk)
		zones = Zone.objects.all()
		return render(request, 'edit_bulb.html', {'bulb': bulb, 'form': form, 'zones': zones })

def control_zone(request):
	log_consumption()
	if request.method == "POST":
		print("Post entered")
		for zone in Zone.objects.all():
			try:
				if request.POST["onOff_" + str(zone.pk)] == 'on':
					for bulb in Bulb.objects.filter(zone=zone):
						bulb_turn_on(bulb)
			except:
				for bulb in Bulb.objects.filter(zone=zone):
					bulb_turn_off(bulb)
				print("Zone: %s is off" % zone)
		return redirect('control_zone')
	else:
		zones = Zone.objects.all()
		bulbs = Bulb.objects.all()
		form = ControlZoneForm()
		return render(request, 'control_zone.html',{'zones': zones, 'bulbs': bulbs, 'form': form})

def stats(request):
	log_consumption()
	if request.method == "POST":
		get_bulbs()
		return redirect('home')	
	else:
		bulbs = Bulb.objects.all()
		if len(bulbs) > 0:
			randNum = get_consumption()
		else:
			randNum = 0
		return render(request, 'stats.html', {'bulbs': bulbs, 'randNum': randNum})

def dashboard(request):
	pythonData = []
	pythonData.append(['Bulb','Watts'])
	for bulb in Bulb.objects.all():
		totalMilliwatts = LogBulb.objects.filter(bulb=bulb).aggregate(Sum('consumption'))
		pythonData.append([bulb.name, (totalMilliwatts['consumption__sum']/1000)])
	print(pythonData)
	return render(request, 'dashboard.html', {'pythonData': pythonData })
