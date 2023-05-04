import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("3.2.4 Bee_Data_Analysis.CSV")
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Value'] = df['Value'].replace(-99, math.nan)
df.dropna(subset=['Value'], inplace=True)
print(df['Value'])
unique_states = df['State'].unique()

for state in unique_states:
  honey_data = df[df['State'] == state]['Value']
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  honey_sums = honey_data.sum()
  years = honey_sums.keys()

all_honey = []
all_states = []

for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(state)

for i in range((len(all_states))-1):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey, label=state)
plt.ylabel('Percentage of Honey Production')
plt.xlabel('Year')
plt.title('Percent of Honey production by state')
plt.legend(loc= 'lower left')
plt.show()