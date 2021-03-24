
#    e → una constante con un valor que es una aproximación del número de Euler (e).
#    exp(x) → encontrar el valor de ex.
#    log(x) → el logaritmo natural de x.
#    log(x, b) → el logaritmo de x con base b.
#    log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
#    log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).


#La funcion pow(x,y) no es necesario importarla

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
