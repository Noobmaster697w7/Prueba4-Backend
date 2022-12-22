from django import forms
from NASHEAPP.models import Alumnos

class FormAlumnos(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'