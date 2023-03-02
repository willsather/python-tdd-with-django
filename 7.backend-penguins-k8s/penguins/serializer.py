from rest_framework import serializers
from .models import Penguin


class PenguinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penguin
        fields = ('island', 'body_mass', 'gender')
