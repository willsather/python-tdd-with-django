import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Penguin
from ..serializer import PenguinSerializer

client = APIClient()


class PenguinViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Penguin.objects.create(island='fakeIsland1', body_mass_g=0, sex='female', bill_length_mm=0.0,
                               bill_depth_mm=0.0, flipper_length_mm=0)
        Penguin.objects.create(island='fakeIsland2', body_mass_g=0, sex='male', bill_length_mm=0.0,
                               bill_depth_mm=0.0, flipper_length_mm=0)

    @pytest.mark.django_db
    def test_get_all_penguins(self):
        # All penguins
        all_penguins = Penguin.objects.all()
        expected_data = PenguinSerializer(all_penguins, many=True).data

        # Make GET call to endpoint
        response = client.get('/api/penguins/', format='json')

        # Assert response is successful and matches all penguin data
        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data

    @pytest.mark.django_db
    def test_post_new_penguin(self):
        # Assert two penguins already exist
        penguins = Penguin.objects.all()
        assert penguins.count() == 2

        # call `POST` with new Penguin object
        post_response = client.post('/api/penguins/', {'island': 'fakeIslandName', 'body_mass': 300, 'gender': 'N/A'},
                                    format='json')
        assert post_response is not None
        assert post_response.status_code == status.HTTP_201_CREATED

        # `GET` all penguins from server
        get_response = client.get('/api/penguins/', format='json')

        # Get all penguins using REST endpoint and prepare
        dates = Penguin.objects.all()
        serializer = PenguinSerializer(dates, many=True)

        # Assert response is successful and new penguin data is created
        assert get_response.json() == serializer.data
        assert get_response.status_code == status.HTTP_200_OK
