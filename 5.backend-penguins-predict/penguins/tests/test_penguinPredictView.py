import pytest
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


class PenguinPredictViewTest(TestCase):

    @pytest.mark.django_db
    def test_post_predict_penguin(self):
        # call `POST` with Penguin object
        response = client.post('/api/penguins/predict',
                               {'bill_length_mm': 39.1, 'bill_depth_mm': 18.7, 'flipper_length_mm': 181.0,
                                'body_mass_g': 3750.0, 'island': 'Torgersen', 'sex': 'male'},
                               format='json')

        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'species': "Adelie"}
