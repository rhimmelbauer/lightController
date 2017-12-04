from django import forms
from .models import * 

class CustomBulbForm(forms.Form):
    

    def clean(self):
        cleaned_data = super(CustomBulbForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

class CustomBulb(forms.ModelForm):
	class Meta:
		model = Bulb
		fields = ['onOff',
		'rgbColor',
		'brightness',
        'zone']

class NewZone(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['name',
        'description']