from django.shortcuts import render, redirect, get_object_or_404
from random import randint

from .models import *
from .forms import *
from .lightControl import *

def home(request):
	get_bulbs()
	zones = Zone.objects.all()
	bulbs = Bulb.objects.all()
	bulbsNoZone = Bulb.objects.exclude(zone__isnull=False)
	return render(request, 'home.html', {'bulbs': bulbs, 'bulbsNoZone': bulbs, 'zones': zones})

def new_zone(request):
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
    if request.method == 'POST':
        print("-------------------POST ENTERED---------------------")
        form = CustomBulb(request.POST)
        print(form['brightness'])
        print(form['rgbColor'])
        print(form['onOff'])
        print(form['zone'].value)
        if form.is_valid():
            print("------------------------VALID-----------------")
            bulb = Bulb.objects.get(pk=pk)
            bulbForm = form.save(commit=False)
            bulb.onOff = bulbForm.onOff
            bulb.rgbColor = bulbForm.rgbColor
            bulb.brightness = bulbForm.brightness
            bulb.zone = bulbForm.zone
            bulb.save()
            #update_bulb(bulb)
            return redirect('home')
        else:
            print (form['onOff'])
            return redirect('home')

    else:
        form = CustomBulb()
        bulb = get_object_or_404(Bulb, pk=pk)
        print(bulb.zone)
        zones = Zone.objects.all()
        return render(request, 'edit_bulb.html', {'bulb': bulb, 'form': form, 'zones': zones })

def control_zone(request):
    zones = Zone.objects.all()
    bulbs = Bulb.objects.all()
    return render(request, 'control_zone.html',{'zones': zones, 'bulbs': bulbs})

def stats(request):
	bulbs = Bulb.objects.all()
	randNum = randint(1,100)
	return render(request, 'stats.html', {'bulbs': bulbs, 'randNum': randNum})
