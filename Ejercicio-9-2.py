from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def funcionimpar(n):
    if n % 2 != 0:
        return True

    return False

def suma(a, b):
    return a + b

resultado = filter(funcionimpar, numeros)
resultado2 = reduce(suma, resultado)
print(resultado2)
