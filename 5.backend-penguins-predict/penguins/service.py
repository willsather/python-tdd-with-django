import joblib
import pandas as pd

from penguins.models import Penguin


def predict(penguin):
    loaded_model = joblib.load('Predict_PenguinSpecies_DecisionTree_Model.sav')

    print(penguin)

    formatted_data = {'bill_length_mm': penguin.bill_length_mm, 'bill_depth_mm': penguin.bill_depth_mm,
                      'flipper_length_mm': penguin.flipper_length_mm, 'body_mass_g': penguin.body_mass_g,
                      'island_Dream': penguin.island == 'Dream', 'island_Torgersen': penguin.island == 'Torgersen',
                      'sex_male': penguin.sex == 'MALE'}

    df = pd.DataFrame([formatted_data])

    print(df.head())

    prediction = loaded_model.predict(df)
    # prediction = "This is a prediction"

    return prediction
