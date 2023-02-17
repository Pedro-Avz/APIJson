from rest_framework import serializers
from .models import Avaliacao 
from .models import Curso


class AvaliacaoSerializer (serializers.ModelSerializer):

    class Meta:

        extra_kargs = {
            'email' : {'write_only': True}
        }

        model = Avaliacao

        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields =  '__all__'
            