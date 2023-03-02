import pandas as pd
import joblib


def predict(data):
    # Initialize data to lists.
    new_data = [data]

    # Creates DataFrame for new data.
    new_df = pd.DataFrame(new_data)

    # Load model
    loaded_model = joblib.load('../Predict_PenguinSpecies_DecisionTree_Model.sav')

    # Create new prediction with dataframe
    return loaded_model.predict(new_df)
