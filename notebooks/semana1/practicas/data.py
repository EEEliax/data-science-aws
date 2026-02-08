personas = [
    {"nombre": "Ana", "edad": 20, "ciudad": "BA", "compras": 5},
    {"nombre": "Juan", "edad": 30, "ciudad": "BA", "compras": 2},
    {"nombre": "Lucia", "edad": 25, "ciudad": "Córdoba", "compras": 8},
    {"nombre": "Pedro", "edad": 40, "ciudad": "BA", "compras": 1},
    {"nombre": "Sofia", "edad": 35, "ciudad": "Córdoba", "compras": 6}
]

def filtrar_por_BA(personas):
    personas_BA = [p for p in personas if p["ciudad"] == "BA"] # si se pone p atras del for indica q solo se pase el p, es decir la persona completa q cumple la condicion
    for persona in personas_BA:
        print("nombre:", persona["nombre"], 
              ", edad:", persona["edad"], 
              ", ciudad:", persona["ciudad"], 
              ", compras:", persona["compras"])
        
filtrar_por_BA(personas)

def promedio_edad(personas):
    total_edad = sum(p["edad"] for p in personas) #aca se obtiene la suma de todas las edades 
    return total_edad / len(personas) # len lo q hace es obtener la cantidad de elementos en la lista

print("Promedio de edad:", promedio_edad(personas))

def persona_mas_compras(personas):
    persona= max(personas, key=lambda p: p["compras"]) # max obtiene el elemento con el valor maximo, 
    # segun la key q dice cual es el criterio de comparacion en este caso una funcion lambda con parametro p y a su vez p["compras"]
    # Para cada persona (p), usá el valor de p["compras"] como criterio de comparación
    print("Persona con mas compras:", persona["nombre"],
          "con", persona["compras"], "compras")
    
persona_mas_compras(personas)

def lista_solo_nombres(personas):
    nombres = [p["nombre"] for p in personas] # crea una nueva lista con solo los nombres, indica q solo se pase el p["nombre"]
    print("Lista de nombres:")
    for nombre in nombres:
        print(nombre)

lista_solo_nombres(personas)

def cantidad_personas_por_ciudad(personas):
    ciudades = {} # diccionario vacio
    for p in personas:
        ciudad = p["ciudad"]
        if ciudad in ciudades: # el diccionario se va completando a medidad que se recorren las personas
            ciudades[ciudad] += 1 # si la ciudad ya esta en el diccionario, se incrementa su contador
        else:
            ciudades[ciudad] = 1 # si no esta, se crea la clave y se inicializa en 1
    print("Cantidad de personas por ciudad:")
    for ciudad, cantidad in ciudades.items(): # items() devuelve una lista de tuplas (clave, valor)
        print(ciudad + ":", cantidad) # imprime la clave y el valor asociado

cantidad_personas_por_ciudad(personas)

def persona_con_menor_edad(personas):
    persona = min(personas, key=lambda p: p["edad"])
    print("Persona con menor edad:", persona["nombre"], "con una edad de", persona["edad"])

persona_con_menor_edad(personas)

def ordear_por_edad(personas):
    ordenadas = sorted(personas, key=lambda p: p["edad"])
    for p in ordenadas:
        print("nombre:", p["nombre"], ", edad:", p["edad"])

ordear_por_edad(personas)

def ordenar_por_compras_desc(personas):
    ordenadas = sorted(personas, key=lambda p: p["compras"], reverse=True) # reverse=True para ordenar de mayor a menor
    for p in ordenadas:
        print("nombre:",p["nombre"],", compras:", p["compras"])

ordenar_por_compras_desc(personas)