import pandas as pd
import ast

# Loading dataset
df = pd.read_csv('Season2024Dataset .csv')

flat_rows = []

for _, row in df.iterrows():
    circuit = row['Circuit']
    position = row['Position']
    pitstops = ast.literal_eval(row['PitStops'])

    # LABELING the positions into 3 categories
    if position <= 7:
        label = 2  # good
    elif position <= 13:
        label = 1  # so-so
    else:
        label = 0  # bad

    for i, pit in enumerate(pitstops):
        flat_rows.append({
            'Circuit': circuit,
            'Lap': pit['Lap'],
            'TotalPitStops': i + 1,
            'Label': label
        })

# Saving the final labeled and categorized data
flat_df = pd.DataFrame(flat_rows)
flat_df.to_csv('ready_data.csv', index=False)
print(flat_df.head())
