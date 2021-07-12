from . models import Task
from django import forms
class TOdoforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']