from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Penguin
from .serializer import PenguinSerializer
from .service import predict


class PenguinController(ListCreateAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer


class PenguinDetailController(RetrieveUpdateDestroyAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer


class PenguinPredictController(GenericAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer

    def post(self, request, format=None):
        serializer = PenguinSerializer(data=request.data)

        if serializer.is_valid():
            penguin = Penguin.objects.create(**serializer.validated_data)
            prediction = predict(penguin)

            return Response(prediction, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
