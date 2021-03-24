miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 100
Encontrado = False

for i in miLista:
    Encontrado = i == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
