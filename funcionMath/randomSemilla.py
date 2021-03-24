# La función seed() es capaz de establecer la semilla del generador. Te mostraremos dos de sus variantes:

#    seed() - establece la semilla con la hora actual.
#    seed(int_value) - establece la semilla con el valor entero int_value.

from random import random, seed

seed(1)

for i in range(5):
    print(random())

