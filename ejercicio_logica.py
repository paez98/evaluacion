from collections import Counter


def numeros_unicos(lista):
    # Paso 1: Aca cuento cuantas veces aparece cada número en la lista
    contador = Counter(lista)

    # Paso 2: Aqui filtro los números que aparecen solo una vez y se crea la lista de resultados
    resultado = [num for num in lista if contador[num] == 1]

    # Paso 3: Retorno la lista de números únicos
    return resultado


entrada = [4, 5, 4, 6, 7, 5, 8]
salida = numeros_unicos(entrada)
print("Numeros unicos:", salida)
