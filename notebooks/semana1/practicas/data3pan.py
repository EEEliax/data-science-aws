import pandas as pd

df = pd.read_csv("datos.csv") # Lee el archivo CSV y lo carga en un DataFrame de pandas

# print("Dataframe cargado:")
# print(df)

"""def mostrar_personas_MDP(df):
    personas_mdq = df[df["ciudad"] == "Mar del Plata"] 
    print("Personas de Mar del Plata:")
    print(personas_mdq)

mostrar_personas_MDP(df)

def promedio_edad(df):
    return df["edad"].mean() # el mean es una funcion de pandas que calcula el promedio de una columna

print("Promedio de edad:", promedio_edad(df))

def contar_alumnos_por_carrera(df):
    # conteo = df["carrera"].value_counts() # value_counts cuenta la cantidad de ocurrencias de cada valor en la columna
    conteo = df.groupby("carrera").size() # otra forma de contar por carrera usando groupby
    print("Cantidad de alumnos por carrera:")
    print(conteo)

contar_alumnos_por_carrera(df)

def persona_mas_grande(df):
    personaMayor = df.loc[df["edad"].idxmax()] # idxmax devuelve el indice del valor maximo en la columna edad, y loc accede a la fila correspondiente
    print("Persona más grande:")
    print(personaMayor)

persona_mas_grande(df)

def lista_nombres(df):
    nombres = df["nombre"].tolist() # convierte la columna nombre en una lista
    print("Lista de nombres:")
    print(nombres)

lista_nombres(df)
"""

# inspeccion de datos
def inspeccionar_datos(df):
    print("Primeras 5 filas del DataFrame:")
    print(df.head()) # muestra las primeras 5 filas del DataFrame, para enteder su estructura y no leer todo el archivo

    print("\nInformación del DataFrame:")
    print(df.info()) # muestra información sobre el DataFrame y detectar, como tipos de datos, valores nulos y columnas mal cargadas
    # el no-null count dice q cantidad de valores no nulos hay en cada columna y si hay menos filas q en otros columnas es pq hay valores nulos NaN

    print("\nEstadísticas descriptivas:")
    print(df.describe()) # muestra estadísticas descriptivas de las columnas numéricas, sirve para ver distribución de datos y detectar valores atípicos

    print("Ultimas 5 filas del DataFrame:")
    print(df.tail()) # muestra las ultimas 5 filas del DataFrame, para ver si hay algo raro al final del archivo y se cargo completo

    print("Tamaño del DataFrame:")
    print(df.shape) # muestra la cantidad de filas y columnas del DataFrame (filas, columnas)

    print("Tipos de datos por columna:")
    print(df.dtypes) # muestra los tipos de datos de cada columna, para verificar que se hayan cargado correctamente, detectar columnas numéricas como texto, fechas mal parceadas, etc.


# limpieza de datos
def limpiar_datos(df):
    print("Detectar valores nulos:")
    print(df.isna()) # muestra un DataFrame booleano indicando si hay valores nulos en cada celda tambien se puede poner df.isnull()

    print("Eliminar filas con valores nulos:")
    df_limpio = df.dropna() # elimina las filas que contienen valores nulos, ya que los valores nulos pueden afectar los análisis posteriores
    print(df_limpio)

    print("Rellenar valores nulos, ejemplo con la columna 'edad':")
    df["edad"] = df["edad"].fillna(df["edad"].mean()) # rellena los valores nulos en la columna 'edad' con el promedio de esa columna, para no perder datos
    print(df)
    
    print("Detectar duplicados:")
    print(df.duplicated()) # muestra un Series booleano (Una columna de pandas) indicando si hay filas duplicadas
    # df.duplicated(subset=["nombre", "edad"]) si queremos verificar duplicados solo en ciertas columnas

    print("Eliminar filas duplicadas:")
    df_sin_duplicados = df.drop_duplicates() # elimina las filas duplicadas ya q en los dataset grandes pueden haber muchas filas repetidas
    print(df_sin_duplicados)

# conversion de tipos de datos
def convertir_tipos(df):
    print("Convertir columna 'edad' a tipo entero:")
    df["edad"] = df["edad"].astype(int) # convierte la columna 'edad' a tipo entero, para asegurar que los datos sean del tipo correcto
    print(df.dtypes)

    print("Convertir columna 'nombre' a tipo cadena:")
    df["nombre"] = df["nombre"].astype(str) # convierte la columna 'nombre' a tipo cadena
    print(df.dtypes)

    print("Convertir columna 'precio' a tipo float:")
    df["precio"] = df["precio"].astype(float)

    print("Convertir columna 'fecha' a tipo datetime:")
    df["fecha"] = pd.to_datetime(df["fecha"])

# creacion de nuevas columnas
def crear_nuevas_columnas(df):
    print("Crear columna 'edad_en_dias':")
    df["edad_en_dias"] = df["edad"] * 365 # crea una nueva columna 'edad_en_dias' calculando la edad en días
    print(df)

    print("Crear columna 'nombre_mayusculas':")
    df["nombre_mayusculas"] = df["nombre"].str.upper() # crea una nueva columna con el nombre en mayúsculas
    print(df)

    print("Crear columna 'año_de_nacimiento':")
    current_year = pd.Timestamp.now().year
    df["año_de_nacimiento"] = current_year - df["edad"] # crea una nueva columna con el año de nacimiento estimado
    print(df)

    print("Crear columna 'mayor_edad':")
    df["mayor_edad"] = df["edad"] >= 18 # crea una nueva columna que indica si la persona es mayor de edad
    print(df)

# agregaciones
def agregaciones(df):
    print("Edad promedio:")
    print(df["edad"].mean()) # calcula y muestra la edad promedio

    print("Edad máxima:")
    print(df["edad"].max()) # calcula y muestra la edad máxima

    print("Edad mínima:")
    print(df["edad"].min()) # calcula y muestra la edad mínima

    print("Conteo de alumnos por carrera:")
    print(df["carrera"].value_counts()) # cuenta y muestra la cantidad de alumnos por carrera

    print("desviacion de edades:")
    print(df["edad"].std()) # calcula y muestra la desviación estándar de las edades

# por grupos
def por_grupos(df):
    print("Edad promedio por ciudad:")
    print(df.groupby("ciudad")["edad"].mean()) # calcula y muestra la edad promedio por ciudad

    print("Cantidad de alumnos por carrera:")
    print(df.groupby("carrera").size()) # cuenta y muestra la cantidad de alumnos por carrera usando groupby

    print("Edad máxima por ciudad:")
    print(df.groupby("ciudad")["edad"].max()) # calcula y muestra la edad máxima por ciudad

# ordenamiento y filtrado
def ordenamiento_filtrado(df):
    print("Ordenar por edad ascendente:")
    print(df.sort_values(by="edad")) # ordena y muestra el DataFrame por edad en orden ascendente

    print("Ordenar por ciudad y luego por edad descendente:")
    print(df.sort_values(by=["ciudad", "edad"], ascending=[True, False])) # ordena por ciudad ascendente y luego por edad descendente

    print("Filtrar personas mayores de 25 años:")
    print(df[df["edad"] > 25]) # filtra y muestra las personas mayores de 25 años

    print("Filtrar personas de 'Mar del Plata':")
    print(df[df["ciudad"] == "Mar del Plata"]) # filtra y muestra las personas de Mar del Plata

# seleccion avanzada
def seleccion_avanzada(df):
    print("Seleccionar nombres y edades de personas mayores de 30 años:")
    print(df.loc[df["edad"] >= 30, ["nombre", "edad"]]) # selecciona y muestra los nombres y edades de personas mayores de 30 años

    print("Seleccionar todas las columnas excepto 'id':")
    print(df.loc[:, df.columns != "id"]) # selecciona y muestra todas las columnas excepto 'id'

    print("Seleccionar fila con indice 2:")
    print(df.loc[2]) # selecciona la fila con indice 2, segun en realidad el index q este puesto puede ser el nombre o id

    print("Seleccionar primera fila por posición:")
    print(df.iloc[0]) # selecciona la primera fila por posicion

    print("Seleccionar personas mayores de 20 años que viven en 'BA':")
    print(df.loc[(df["edad"] > 20) & (df["ciudad"] == "BA")]) # selecciona personas mayores de 20 años que viven en BA
    
seleccion_avanzada(df)

