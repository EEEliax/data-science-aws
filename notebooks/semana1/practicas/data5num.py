import pandas as pd
import numpy as np

df = pd.read_csv("datos.csv") # Lee el archivo CSV y lo carga en un DataFrame de pandas

# limpiamos
df = df.dropna() # elimina filas con valores nulos
df = df.drop_duplicates() # elimina filas duplicadas
print("Dataframe limpio:")
print(df)

# creamos arrays
edades = df["edad"].to_numpy() # convierte la columna edad en un array de numpy
print("Array de edades:")
print(edades)

# operaciones con arrays
print("Edad promedio:")
print(np.mean(edades)) # calcula y muestra la edad promedio usando numpy
print("Edad máxima:")
print(np.max(edades)) # calcula y muestra la edad máxima usando numpy
print("Edad mínima:")
print(np.min(edades)) # calcula y muestra la edad mínima usando numpy
print("Desviación estándar de edades:")
print(np.std(edades)) # calcula y muestra la desviación estándar de las edades usando numpy
print("Edades ordenadas:")
print(np.sort(edades)) # muestra las edades ordenadas usando numpy

# filtros con arrays
print("Edades mayores a 25:")
mayores_25 = edades[edades > 25] # filtra las edades mayores a 25 usando numpy
print(mayores_25)
print("Edades pares:")
edades_pares = edades[edades % 2 == 0] # filtra las edades pares usando numpy
print(edades_pares)

# operaciones matemáticas con arrays
print("Edades más 5 años:")
edades_mas_5 = edades + 5 # suma 5 años a cada edad
print(edades_mas_5)
print("Edades multiplicadas por 2:")
edades_por_2 = edades * 2 # multiplica cada edad por 2
print(edades_por_2)

# creación de nuevas columnas
df["edad_en_meses"] = edades * 12 # crea una nueva columna 'edad
print("Dataframe con nueva columna 'edad_en_meses':")
print(df)

# normalización de edades
edades_normalizadas = (edades - np.min(edades)) / (np.max(edades) - np.min(edades)) # normaliza las edades entre 0 y 1
print("Edades normalizadas:")
print(edades_normalizadas)
df["edad_normalizada"] = edades_normalizadas # agrega la columna de edades normalizadas al DataFrame
print("Dataframe con columna 'edad_normalizada':")
print(df)

# estadísticas por carrera
print("Edad promedio por carrera:")
for carrera in df["carrera"].unique():
    edades_carrera = df[df["carrera"] == carrera]["edad"].to_numpy()
    print(f"{carrera}: {np.mean(edades_carrera)}")
print("Cantidad de alumnos por carrera:")
for carrera in df["carrera"].unique():
    count = np.sum(df["carrera"] == carrera)
    print(f"{carrera}: {count}")