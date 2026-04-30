import pandas as pd

df = pd.read_csv("data/sales.csv")

required_columns = ["date", "region", "sales"]

for col in required_columns:
    if col not in df.columns:
        raise Exception(f"Missing column: {col}")

if df.isnull().sum().sum() > 0:
    raise Exception("Dataset contains null values")

print("Dataset validation successful!")
