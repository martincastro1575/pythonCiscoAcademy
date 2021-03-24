
#Aleatorios enteros
#    randrange(fin)x
#    randrange(inico, fin)
#    randrange(inicio, fin, incremento)
#    randint(izquierda, derecha)

#Las primeras tres invocaciones generarán un número entero tomado (pseudoaleatoriamente) del rango:

#   range(fin)
#    range(inicio, fin)
#    range(inicio, fin, incremento)

#Toma en cuenta la exclusión implícita del lado derecho.

#La última función es equivalente a randrange(izquierda, derecha+1) - genera el valor entero i, el cual cae en el rango [izquierda, derecha] (sin exclusión en el lado derecho).

#Observa el código en el editor. Este programa generará una línea que consta de tres ceros y un cero o un uno en el cuarto lugar.


from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
