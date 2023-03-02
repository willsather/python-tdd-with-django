from unittest import TestCase

from ..model.predict import predict


class PenguinPredictTest(TestCase):

    @staticmethod
    def test_predict_adelie():
        prediction = predict({'bill_length_mm': 39.1, 'bill_depth_mm': 18.7, 'flipper_length_mm': 181.0,
                              'body_mass_g': 3750.0, 'island_Dream': 0, 'island_Torgersen': 1, 'sex_male': 1})

        assert prediction == ["Adelie"]

    @staticmethod
    def test_predict_gentoo():
        prediction = predict({'bill_length_mm': 46.1, 'bill_depth_mm': 13.2, 'flipper_length_mm': 211,
                              'body_mass_g': 4500, 'island_Dream': 0, 'island_Torgersen': 0, 'sex_male': 0})

        assert prediction == ["Gentoo"]

    @staticmethod
    def test_predict_chinstrap():
        prediction = predict({'bill_length_mm': 46.5, 'bill_depth_mm': 17.9, 'flipper_length_mm': 192,
                              'body_mass_g': 3500, 'island_Dream': 1, 'island_Torgersen': 0, 'sex_male': 0})

        assert prediction == ["Chinstrap"]
