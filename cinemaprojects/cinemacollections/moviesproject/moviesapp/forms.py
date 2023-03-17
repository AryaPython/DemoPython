from django import forms
from .models import movie


class movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','des','year','img']

class newform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','des','year','img']