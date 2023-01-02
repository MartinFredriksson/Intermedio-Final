from django import forms


class sorteo(forms.Form):
    nombre = forms.CharField(30)
    apellido = forms.CharField(50)
    edad = forms.IntegerField()