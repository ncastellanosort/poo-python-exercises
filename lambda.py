#funciones anonimas

mult = lambda x: x * 2

print(mult(2))

#con filter, devuelve true o false

numeros = [1,2,3,4,5,6,7,8,9]

def pares(num):
    if num % 2 == 0:
        return True

#ahora usando filter
#numeros_pares = filter(pares, numeros)

#misma forma

numeros_pares = filter(lambda numero : numero % 2 == 0, numeros)
print(list(numeros_pares))
