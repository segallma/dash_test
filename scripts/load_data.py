# Import data

# Building the path instead of giving it as a string to solve backslash-related 
# incompatibilities between systems

import pandas as pd
import os

def load_cases_rates(filename="cases_by_group.csv"):

    base_dir = os.path.dirname(__file__)
    
    path = os.path.join(base_dir, "..", "data", filename)
    
    df0 = pd.read_csv(path, delimiter=";")
    
    return df0