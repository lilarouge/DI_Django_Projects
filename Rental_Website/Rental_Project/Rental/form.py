from django import forms

class Add_Rental(forms.Form):
      customer_id = forms.CharInteger()
      vehicle_id = forms.CharInteger()  
