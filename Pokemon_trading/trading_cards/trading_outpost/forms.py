from django.forms import ModelForm
from .models import *
 
class Change_Card_Id(ModelForm):
    class Meta:
        model= My_Card
        fields = ("profile",)