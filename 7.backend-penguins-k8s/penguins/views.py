from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Penguin
from .serializer import PenguinSerializer

# class PenguinController(GenericAPIView):
#     queryset = Penguin.objects.all()
#     serializer_class = PenguinSerializer

#     def get(self, request, format=None):
#         penguins = Penguin.objects.all()
#         serializer = PenguinSerializer(penguins, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = PenguinSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class PenguinController(ListCreateAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer
    
class PenguinDetailController(RetrieveUpdateDestroyAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer