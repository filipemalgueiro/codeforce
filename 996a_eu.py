def notas2(valor):
    contador = 0
    while (valor >= 100):
        valor -= 100
        contador += 1
    while (valor >= 20):
        valor -= 20
        contador += 1
    while (valor >= 10):
        valor -= 10
        contador += 1
    while (valor >= 5):
        valor -= 5
        contador += 1
    while (valor >= 1):
        valor -= 1
        contador += 1
    return contador
 
print(notas2(int(input())))