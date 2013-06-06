from rest_framework import serializers
from apiv1.models import Genero, Marital, Nacionalidad
from apiv1.models import Personal
from apiv1.models import Programa, Autoridad, Codigos, Adscripcion
from apiv1.models import Plantilla


class GeneroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genero
class MaritalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Marital
class NacionalidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nacionalidad
class PersonalSerializer(serializers.ModelSerializer):
	genero 		= GeneroSerializer()
	marital 	= MaritalSerializer()
	nacionalidad= NacionalidadSerializer()
	
	class Meta:
		model = Personal
		
class PlantillaSerializer(serializers.Serializer):
	class Meta:
		model = Plantilla
