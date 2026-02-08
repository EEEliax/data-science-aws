import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos.csv") # Lee el archivo CSV y lo carga en un DataFrame de pandas

print("Dataframe cargado:")
print(df)
print(df.info())

# limpieza de datos
df_cleaned = df.dropna() # elimina filas con valores nulos
df_cleaned = df_cleaned.drop_duplicates() # elimina filas duplicadas
print("Dataframe limpio:")
print(df_cleaned)
print(df_cleaned.info())

# visualización de datos

# gráfico histograma de edades
plt.hist(df_cleaned["edad"], bins=range(10, 40, 2), edgecolor='black')
plt.title("Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Cantidad de Personas")
plt.show()

# gráfico de barras de cantidad de alumnos por carrera
plt.bar(df_cleaned["carrera"].value_counts().index, df_cleaned["carrera"].value_counts().values)
plt.title("Cantidad de Alumnos por Carrera")
plt.xlabel("Carrera")
plt.ylabel("Cantidad de Alumnos")
plt.xticks(rotation=10)
plt.show()

"""df_cleaned["carrera"].value_counts().plot(kind="bar")
plt.title("Cantidad de alumnos por carrera")
plt.xlabel("Carrera")
plt.ylabel("Cantidad")
plt.show()
"""
# gráfico de dispersión edad vs id
plt.scatter(df_cleaned["edad"], df_cleaned["id"])
plt.xlabel("Edad")
plt.ylabel("ID")
plt.title("Relación edad - id")
plt.show()

# boxplot de edades
plt.boxplot(df_cleaned["edad"])
plt.title("Boxplot de edades")
plt.ylabel("Edad")
plt.show()
