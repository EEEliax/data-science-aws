nombre = input("cual es tu nombre?")
edad = int(input("cual es tu edad?"))
ciudad = input("cual es tu ciudad?")

if edad >= 18:
    print("Hola",nombre,"vivis en",ciudad,"y eres mayor de edad (tienes",edad,"años)")
else:
    print("Hola",nombre,"vivis en",ciudad,"y eres menor de edad (tienes",edad,"años)")
    