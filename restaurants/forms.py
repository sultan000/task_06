from django import forms
from .models import Restaurant

class RestaurantForm (forms.ModelForm) :
    class Meta :
        model = Restaurant
        fields = ['name','description','opening_time','closing_time']

        #widgets = {
         #       'opening_time' : forms.TimeField(attr={'type':'time'})
          #      'closing_time' : forms.TimeField(attr={'type':'time'})
          # }