import pandas as pd
df = pd.read_csv("animal_data_dirty1.csv", sep=";")
df['Weight kg'] = pd.to_numeric(df['Weight kg'], errors='coerce')
df['Body Length cm'] = pd.to_numeric(df['Body Length cm'], errors='coerce')
print("=" * 60)
print("PUNTO 4: ANALISIS CON GROUPBY")
print("="*60)
#1. analisis por tipo de animal
print(r"\n---1. Numero de observaciones por  tipo de animal---")
observacion_por_animal = df.groupby('Animal type'). size()
print(observacion_por_animal)
#2. promedio por peso segun el animal
print(r"\n---2. Promedio por peso(Weight kg) segun el tipo de animal---")
promedio_peso_animal = df.groupby('Animal type')['Weight kg'].mean()
print(promedio_peso_animal)
#3. promedio de peso segun el pais
print(r"n\---3. Promedio de peso(Weight kg)segun el pais---")
promedio_peso_pais = df.groupby('Country')['Weight kg'].mean()
print(promedio_peso_pais)
#4. promedio de longitud
print(r"n\---4. Promedio de longitud (Body Length cm) segun el animal ---")
promedio_longitud_animal = df.groupby('Animal type')['Body Length cm'].mean()
print(promedio_longitud_animal)
print("="*60)