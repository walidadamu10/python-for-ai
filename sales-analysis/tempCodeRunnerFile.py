import pandas as pd
import json
import os

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")