def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primos_entre(a,b):
    lista_primos = []
    for i in range(a,b+1):
        if es_primo(i):
            lista_primos.append(i)
    return lista_primos

print(primos_entre(5, 20))
