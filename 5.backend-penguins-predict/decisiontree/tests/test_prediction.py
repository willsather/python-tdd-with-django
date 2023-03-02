from django.test import TestCase

from decisiontree.model.predict import predict


class PenguinPredictTest(TestCase):

    @staticmethod
    def test_predict_adelie():
        prediction = predict({'bill_length_mm': 39.1, 'bill_depth_mm': 18.7, 'flipper_length_mm': 181.0,
                              'body_mass_g': 3750.0, 'island_Dream': 0, 'island_Torgersen': 1, 'sex_male': 1})

        assert True
        assert prediction == ["Adelie"]
