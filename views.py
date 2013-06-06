from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
#
from apiv1.models import Plantilla
#
from apiv1.serializers import PlantillaSerializer

# Create your views here.

class RetrievePlantillaView(APIView):
	"""
	Mostrar datos operativos del personal de plantilla activa

	* Se requieren permisos para la operacion (not implemented yet)
	"""
	#serializer_class = PlantillaSerializer

	def get(self, request, format=None):
		"""
		Recupera la infomacion de un determinado trabajador
		"""
		emp = Plantilla.objects.all()
		print "---------"
		print emp,
		print "---------"
		serializer = PlantillaSerializer(emp, many=True)
		#print "--", serializer.data,"--"
		return Response(serializer.data)
