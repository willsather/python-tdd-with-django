from django.test import TestCase

from ..models import Penguin
from ..serializer import PenguinSerializer
from ..service import predict


class ServiceTest(TestCase):

    @staticmethod
    def test_predict_penguin_adelie():
        # Create Penguin to use to predict
        serializer = PenguinSerializer(data={'bill_length_mm': 39.1, 'bill_depth_mm': 18.7, 'flipper_length_mm': 181.0,
                                             'body_mass_g': 3750.0, 'island': 'Torgersen', 'sex': 'male'})
        serializer.is_valid(raise_exception=True)
        penguin = Penguin.objects.create(**serializer.validated_data)

        # Make prediction
        prediction = predict(penguin)

        assert prediction == "Adelie"

    @staticmethod
    def test_predict_penguin_gentoo():
        # Create Penguin to use to predict
        serializer = PenguinSerializer(data={'bill_length_mm': 46.1, 'bill_depth_mm': 13.2, 'flipper_length_mm': 211,
                                             'body_mass_g': 4500.0, 'island': 'Biscoe', 'sex': 'female'})
        serializer.is_valid(raise_exception=True)
        penguin = Penguin.objects.create(**serializer.validated_data)

        # Make prediction
        prediction = predict(penguin)

        assert prediction == "Gentoo"

    @staticmethod
    def test_predict_penguin_chinstrap():
        # Create Penguin to use to predict
        serializer = PenguinSerializer(data={'bill_length_mm': 46.5, 'bill_depth_mm': 17.9, 'flipper_length_mm': 192,
                                             'body_mass_g': 3500.0, 'island': 'Dream', 'sex': 'female'})
        serializer.is_valid(raise_exception=True)
        penguin = Penguin.objects.create(**serializer.validated_data)

        # Make prediction
        prediction = predict(penguin)

        assert prediction == "Chinstrap"
