import pandas as pd
import matplotlib as plt

df = pd.read_csv("3.2.4 Bee_Data_Analysis.CSV")
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)
print(df['Value'])