import pandas as pd
df = pd.read_csv("animal_data_dirty1.csv", sep=";")
print("---ESTADO INICIAL---")
print("Filas y columnas previas a limpieza:", df.shape)
#VALORES FALTANTES(NaN)
#SE ELIMINA O RELLENA FILAS SEGUN CORRESPONDA
df = df.dropna(subset=['Animal type'])
#ELIMINAR REGISTROS DUPLICADOS
df = df.drop_duplicates()
#CONVERTIR DATOS INCORRECTOS, YA SEA A NUMEROS O TEXTO
#ESTANDARIZAR VARIABLES CON INCONSISTENCIAS
df['Animal type'] = df['Animal type'].str.lower().str.strip()
#CORRECCION DE ERRORES
df['Animal type'] = df['Animal type'].replace({'red squirrel': 'red squirel', 'european bisson': 'european bison'})
print("\n--- 5 LIMPIEZA REALIZADA ---")
print("Total de filas y columnas:", df.shape)
print("\nValores nulos actuales:\n", df.isnull().sum())
print("\nTotal de duplicados restantes:", df.duplicated().sum())
print("n\Categorias de 'Animal type' estandarizadas:\n", df['Animal type']. value_counts(dropna=False))