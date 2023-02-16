from rest_framework import serializers
from .models import Penguin


class PenguinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penguin
        fields = ('island', 'body_mass_g', 'sex', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm')
