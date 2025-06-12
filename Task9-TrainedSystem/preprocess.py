import pandas as pd
import ast

# Load your raw dataset
df = pd.read_csv('Season2024Dataset .csv')  # Make sure PitStops is stringified JSON/dict list

flat_rows = []

for _, row in df.iterrows():
    circuit = row['Circuit']
    position = row['Position']
    pitstops = ast.literal_eval(row['PitStops'])  # convert string to list of dicts

    # Label assignment based on final race position
    if position <= 7:
        label = 2  # Good
    elif position <= 13:
        label = 1  # so-so
    else:
        label = 0  # Bad

    for i, pit in enumerate(pitstops):
        flat_rows.append({
            'Circuit': circuit,
            'Lap': pit['Lap'],
            'PitstopNumber': i + 1,  # 1-based indexing
            'Label': label
        })

# Final cleaned dataset
flat_df = pd.DataFrame(flat_rows)
flat_df.to_csv('pitstop_learning_data.csv', index=False)
print(flat_df.head())
