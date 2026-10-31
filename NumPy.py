import numpy as np
import pandas as pd
df = pd.read_csv("animal_data_dirty1.csv", sep=";")
df['Weight kg'] = pd.to_numeric(df['Weight kg'], errors='coerce')
#creacion de variable por peso
df["clasificacion_por_peso"] = np.where(df['Weight kg']> 25, 'pesado', 'ligero')
peso_promedio = np.nanmean(df['Weight kg'])
print(f"peso promedio calculado con numpy: {peso_promedio:.2f} kg")
print(df[['Animal type', 'Weight kg', 'clasificacion_por_peso']].head())