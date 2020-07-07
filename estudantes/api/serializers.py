from rest_framework import serializers
from estudantes.models import Estudante

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'