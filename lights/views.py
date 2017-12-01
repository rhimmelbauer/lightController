from django.shortcuts import render

from .models import *

def home(request):
    zones = Zone.objects.all()
    bulbs = Bulb.objects.all()
    bulbsNoZone = Bulb.objects.exclude(zone_id__isnull=False)
    return render(request, 'home.html', {'bulbs': bulbs, 'bulbsNoZone': bulbsNoZone, 'zones': zones})

def new_zone(request):
    
    return render(request, 'new_component.html')

def edit_bulb(request, pk):
    bulb = get_object_or_404(Bulb, pk=pk)
    return render(request, 'new_component.html',{'bulb': bulb})

def control_zone(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    return render(request, 'new_component.html',{'zone': zone})
