miLista = [1, 2, 4, 6, 6, 3, 3, 4, 4, 1, 4, 2, 6, 2, 9, 9, 2, 2]
listaAux=[]
#
# coloca tu código aquí
#

for i in range(len(miLista)):
    
    if miLista[i] in miLista:
        if miLista[i] not in listaAux:
            listaAux.append(miLista[i])
            

miLista = listaAux[:]
print("La lista solo con elementos únicos:")
print(miLista)

