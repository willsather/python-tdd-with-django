import pandas as pd
import joblib


"""
Logic for Service.py ##
Use anywhere (REST Endpoint in this example)
"""

# Initialize data to lists.
new_data = [{'bill_length_mm': 39.1, 'bill_depth_mm': 18.7, 'flipper_length_mm': 181.0, 
            'body_mass_g': 3750.0, 'island_Dream': 0, 'island_Torgersen': 1, 'sex_male': 1}]
  
# Creates DataFrame for new data.
new_df = pd.DataFrame(new_data)

loaded_model = joblib.load('finalizedDecisionTree.sav')
new_pred = loaded_model.predict(new_df)

print(f'Predicted Species: {new_pred}')
