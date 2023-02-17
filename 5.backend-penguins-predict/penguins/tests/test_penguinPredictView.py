import pytest
from django.test import TestCase
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from ..serializer import PenguinSerializer

client = APIClient()


class PenguinPredictViewTest(TestCase):

    @pytest.mark.django_db
    def test_predict_penguin_empty(self):
        with pytest.raises(ValidationError):
            # Create Penguin to use to predict
            serializer = PenguinSerializer(data={})

            # Invalid data response throws exception
            serializer.is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_post_predict_penguin_invalid(self):
        # call `POST` with Penguin object
        response = client.post('/api/penguins/predict/',
                               {'bill_length_mm': -5, 'bill_depth_mm': -10, 'flipper_length_mm': -15,
                                'body_mass_g': -2000, 'island': 'someFakeIslandName', 'sex': 'NA'},
                               format='json')

        assert response is not None
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.django_db
    def test_post_predict_penguin_adelie(self):
        # call `POST` with Penguin object
        response = client.post('/api/penguins/predict/',
                               {'bill_length_mm': 39.1, 'bill_depth_mm': 18.7, 'flipper_length_mm': 181.0,
                                'body_mass_g': 3750.0, 'island': 'Torgersen', 'sex': 'male'},
                               format='json')

        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ["Adelie"]

    @pytest.mark.django_db
    def test_post_predict_penguin_gentoo(self):
        # call `POST` with Penguin object
        response = client.post('/api/penguins/predict/',
                               {'bill_length_mm': 46.1, 'bill_depth_mm': 13.2, 'flipper_length_mm': 211,
                                'body_mass_g': 4500, 'island': 'Biscoe', 'sex': 'female'},
                               format='json')

        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ["Gentoo"]

    @pytest.mark.django_db
    def test_post_predict_penguin_chinstrap(self):
        # call `POST` with Penguin object
        response = client.post('/api/penguins/predict/',
                               {'bill_length_mm': 46.5, 'bill_depth_mm': 17.9, 'flipper_length_mm': 192,
                                'body_mass_g': 3500, 'island': 'Dream', 'sex': 'female'},
                               format='json')

        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == ["Chinstrap"]
