import pandas as pd
import matplotlib as plt

df = pd.read_csv("3.2.4 Bee_Data_Analysis.CSV")
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)
print(df['Value'])

# get a list unique states
unique_states = df['Value'].unique()

for state in unique_states:
  honey_data = df[df['State'] == state]['Value']

honey_sums = honey_data.sum()

years = honey_sums.keys()

honey_data = df[df['State'] == state].groupby('Year')['Value']

all_honey = []
all_states = []

'''# without grouping
for state in unique_states:
  honey_data = df[df['State'] == state]['Value']
  print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)'''
  
# with grouping
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  #print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)

for i in range((len(all_states))-1):
  honey = all_honey[i]
  state = all_states[i]
  years = honey.keys()
  plt.plot(years, honey)