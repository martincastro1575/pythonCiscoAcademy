#Es una función con el nombre de - choice:

#    choice(secuencia)
#    sample(secuencia, elementos_a_elegir=1)

#La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.

#El segundo crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) "sorteado" de la secuencia de entrada.

#En otras palabras, la función elige algunos de los elementos de entrada, devolviendo una lista con la elección. Los elementos de la muestra se colocan en orden #aleatorio. Nota que elementos_a_elegir no debe ser mayor que la longitud de la secuencia de entrada.


from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))
