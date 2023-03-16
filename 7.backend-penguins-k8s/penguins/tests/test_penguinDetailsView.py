import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Penguin
from ..serializer import PenguinSerializer

client = APIClient()


class PenguinDetailsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Penguin.objects.create(island='fakeIsland1', body_mass_g=10, sex='female', bill_length_mm=10.0,
                               bill_depth_mm=10.0, flipper_length_mm=10)
        Penguin.objects.create(island='fakeIsland2', body_mass_g=10, sex='male', bill_length_mm=10.0,
                               bill_depth_mm=10.0, flipper_length_mm=10)

    @pytest.mark.django_db
    def test_delete_penguin(self):
        # Assert two penguins already exist
        penguins = Penguin.objects.all()
        assert penguins.count() == 2

        # call `POST` with new Penguin object
        response = client.delete('/api/penguins/1/', format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # Assert only 1 penguin exists now
        assert Penguin.objects.all().count() == 1

    @pytest.mark.django_db
    def test_get_specific_penguin(self):
        primary_key = 1
        penguin = Penguin.objects.get(pk=primary_key)
        expected_data = PenguinSerializer(penguin).data

        # call `GET` with primary key
        response = client.get(f'/api/penguins/{primary_key}/', format='json')
        assert response.status_code == status.HTTP_200_OK

        # Assert penguins are equal
        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data

    @pytest.mark.django_db
    def test_update_penguin(self):
        primary_key = 2
        new_penguin = {'island': 'fakeIsland1', 'body_mass_g': 10, 'sex': 'female', 'bill_length_mm': 10.0,
                       'bill_depth_mm': 10.0, 'flipper_length_mm': 10}
        expected_data = PenguinSerializer(new_penguin).data

        # call `PUT` with new Penguin object
        response = client.put(f'/api/penguins/{primary_key}/', new_penguin, format='json')

        # Assert response is successful and penguin data is updated
        assert response is not None
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_data
