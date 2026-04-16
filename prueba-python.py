# VARIABLES

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Hola", nombre)
print("Tu edad es:", edad)


# LISTA (ARREGLO)

numeros = [5, 10, 15, 20]

print("Números en la lista:")

for n in numeros:
    print(n)


# FUNCION

def calcular_promedio(lista):
    suma = 0

    for numero in lista:
        suma = suma + numero

    promedio = suma / len(lista)

    return promedio


# LLAMAR FUNCION

resultado = calcular_promedio(numeros)

print("El promedio es:", resultado)