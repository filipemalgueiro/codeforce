def notas(valor):
    contador = 0
    for nota in [100, 20, 10, 5, 1]:
        if valor >= nota:
            quantidade = valor // nota
            contador += quantidade
            valor -= quantidade * nota
    return contador
 
print(notas(int(input())))