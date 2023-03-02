import os
import joblib
import pandas as pd


def predict(data):
    # Initialize data to lists.
    new_data = [data]

    # Creates DataFrame for new data.
    new_df = pd.DataFrame(new_data)

    # Load model
    dirname = os.path.dirname(__file__)
    loaded_model = joblib.load(
        os.path.join(os.path.dirname(__file__), '../Predict_PenguinSpecies_DecisionTree_Model.sav'))

    # Create new prediction with dataframe
    return loaded_model.predict(new_df)
