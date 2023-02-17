from rest_framework import serializers
from .models import Penguin


class PenguinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penguin
        fields = ('island', 'body_mass_g', 'sex', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm')

    def validate(self, data):
        if data['bill_length_mm'] <= 0:
            raise serializers.ValidationError("Bill Length (mm) must be greater than zero")

        if data['bill_depth_mm'] <= 0:
            raise serializers.ValidationError("Bill Depth (mm) must be greater than zero")

        if data['flipper_length_mm'] <= 0:
            raise serializers.ValidationError("Flipper Length (mm) must be greater than zero")

        if data['body_mass_g'] <= 0:
            raise serializers.ValidationError("Body Mass (g) must be greater than zero")

        return data
