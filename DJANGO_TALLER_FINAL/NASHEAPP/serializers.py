from rest_framework import serializers
from .models import Alumnos, Institucion

class InstitucionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'


class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = '__all__'