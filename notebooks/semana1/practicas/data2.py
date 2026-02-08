personas = []

with open("datos.txt", "r") as datos: # r se trata de q va a leer el archivo sino podemos poner w de escribir
    for fragmento in datos:
        nombre,edad,ciudad,id,carrera = fragmento.strip().split(",") # strip() elimina espacios en blanco y saltos de linea al inicio y final
         # split(",") separa el string en una lista de substrings usando la coma como separador
        personas.append({ # agrega un diccionario a la lista personas
            "nombre": nombre, 
            "edad": int(edad),
            "ciudad": ciudad,
            "id": int(id),
            "carrera": carrera
        })
        

def mostrar(personas):
    for persona in personas:
        print("nombre:", persona["nombre"], 
              ", edad:", persona["edad"], 
              ", ciudad:", persona["ciudad"], 
              ", id:", persona["id"], 
              ", carrera:", persona["carrera"])

mostrar(personas)

def promedio_edad(personas):
    total_edad = sum(p["edad"] for p in personas) #aca se obtiene la suma de todas las edades 
    return total_edad / len(personas) # len lo q hace es obtener la cantidad de elementos en la lista
    # return sum(p["edad"] for p in personas) / len(personas)

print("Promedio de edad:", promedio_edad(personas))

def personas_mardelplata(personas):
    personas_mdq = [p for p in personas if p["ciudad"] == "Mar del Plata"]
    for persona in personas_mdq:
        print("nombre:", persona["nombre"], 
              ", edad:", persona["edad"], 
              ", ciudad:", persona["ciudad"], 
              ", id:", persona["id"], 
              ", carrera:", persona["carrera"])

personas_mardelplata(personas)

def contar_alumnos_por_carrera(personas):
    carreras = {} # diccionario vacio
    for p in personas:
        carrera = p["carrera"]
        if carrera in carreras:
            carreras[carrera] += 1 # si la carrera ya esta en el diccionario, se incrementa su contador
        else:
            carreras[carrera] = 1 # si no esta, se crea la clave y se inicializa en 1

    print("Cantidad de alumnos por carrera:")
    for carrera, cantidad in carreras.items():
        print(carrera, ":", cantidad)

contar_alumnos_por_carrera(personas)
