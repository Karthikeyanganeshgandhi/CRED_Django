from django import forms
from .models import mydetails

class work(forms.ModelForm):
    class Meta:
        model=mydetails
        fields=['name','email','age','adress','phonenumber']