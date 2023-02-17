import joblib
import pandas as pd

from penguins.models import Penguin


def predict(penguin: Penguin) -> str:
    # Load Decision Tree Model from Joblib export
    loaded_model = joblib.load('Predict_PenguinSpecies_DecisionTree_Model.sav')

    # Create Pandas DataFrame using a formatted penguin object
    df = pd.DataFrame([penguin.formatted_data()])

    # Predict species using the model and the dataframe
    prediction = loaded_model.predict(df)

    return prediction
