"""nombre = input("cual es tu nombre?") 

edad = int(input("cual es tu edad?"))

if edad < 0:
    print("edad no valida")
elif edad < 18:
    print("eres menor de edad", nombre)
else:
    print("eres mayor de edad", nombre)"""

# por lo q se ve las variables toman el tipo de dato segun lo que se les asigne 

"""nombres = ["Elias","Renzo","Ana","Maria","Juana"]

for nombre in nombres:
    print("Hola", nombre)"""

def saludar(nombre,edad):
    print("Hola", nombre, "tienes", edad, "años")

# en la funcion se puede pasar un argumento de tipo string y otro de tipo entero, en este caso la edad
saludar("Elias",20)