from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

def home(request):
    zones = Zone.objects.all()
    bulbs = Bulb.objects.all()
    bulbsNoZone = Bulb.objects.exclude(zone__isnull=False)
    return render(request, 'home.html', {'bulbs': bulbs, 'bulbsNoZone': bulbsNoZone, 'zones': zones})

def new_zone(request):
    
    return render(request, 'new_component.html')

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

def control_zone(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    return render(request, 'new_component.html',{'zone': zones})

def stats(request):
    return render(request, 'stats.html')
