# VARIABLES

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Hola", nombre)
print("Tu edad es:", edad)


# LISTA (ARREGLO)

numeros = [10, 20, 30, 40, 50]

print("Números de la lista:")

for n in numeros:
    print(n)


# FUNCION

def promedio(lista):
    suma = 0

    for numero in lista:
        suma = suma + numero

    resultado = suma / len(lista)

    return resultado


# LLAMAR FUNCION

resultado = promedio(numeros)

print("El promedio es:", resultado)