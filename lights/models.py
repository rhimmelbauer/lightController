from django.db import models

class Zone(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, blank=True, null=True)
    def __str__(self):
        return self.name

    
class Bulb(models.Model):
    name = models.CharField(max_length = 100)
    bulb_type = models.CharField(max_length = 100, blank=True, null=True)
    zone_id = models.ForeignKey(Zone, related_name = 'b_zone_id', blank=True, null=True)
    onOff = models.BooleanField(default = False)
    rgbColor = models.IntegerField(default = 0)
    brightness = models.IntegerField(default = 0)
    def __str__(self):
        return self.name
