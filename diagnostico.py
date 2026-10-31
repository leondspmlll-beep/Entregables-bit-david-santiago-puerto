import pandas as pd
df = pd.read_csv("animal_data_dirty1.csv", sep=";")
print("---1. FILAS Y COLUMNAS ---")
print(f"Total de filas y columnas (filas, columnas):{df.shape}")
print("\n--- 2. TIPOS DE DATOS POR COLUMNAS ---")
print(df.dtypes)
print("\n--- 3. VALORES FALTANTES (NaN) POR COLUMNA ---")
print(df.isnull().sum())
print("\n---4. REGISTROS DUPLICADOS ---")
print("Total de filas duplicadas:", df.duplicated().sum() )
print("\n--- 5. Categorias en 'Animal type´(valores inconsistentes) ---")
print(df["Animal type"].value_counts(dropna=False))

#Despues de analizar y hacer el diagnostico del dataset en python se pueden ver 3 problemas principales en la calidad de los datos.
#Varias columnas presencian auscencia de datos debido a lo cual se puede tener fallas al momento de realizar calculos estadisticos.
#Exiten variedad de filas repetidas, lo cual puede aumentar datos artificialmente y por esto deben ser eliminados
#La columna Type tiene variaciones por ortografia y caracteres extraños, debido a esto se pueden interpretar categorias iguales como categorias distintas 