import pandas as pd

def load_cases_rates(path = ".\data\cases_by_group.csv"):
    df0 = pd.read_csv(
    path,
    delimiter = ";")
    return df0


