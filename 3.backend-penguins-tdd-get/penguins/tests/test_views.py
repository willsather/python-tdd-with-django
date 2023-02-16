import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Penguin
from ..serializer import PenguinSerializer

client = APIClient()

class PenguinViewTest(TestCase):

    # Create two fake penguins
    @classmethod
    def setUpTestData(cls):
        Penguin.objects.create(
            island='fakeIslandName', body_mass=100, gender='female')
        Penguin.objects.create(
            island='fakeIslandName', body_mass=200, gender='male')

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
