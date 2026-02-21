# Import data

# Building the path instead of giving it as a string to solve backslash-related 
# incompatibilities between systems

import pandas as pd
import os

def load_cases_rates(filename="cases_by_group.csv"):
    # path relative to app root (WORKDIR)
    path = os.path.join("data", filename)
    return pd.read_csv(path, delimiter=";")