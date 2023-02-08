from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Penguin
from .serializer import PenguinSerializer

class PenguinController(GenericAPIView):
    queryset = Penguin.objects.all()

    def get(self, request, format=None):
        penguins = Penguin.objects.all()
        serializer = PenguinSerializer(penguins, many=True)
        return Response(serializer.data)