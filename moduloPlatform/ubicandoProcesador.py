
#A veces, es posible que solo se desee conocer el nombre genérico del procesador que ejecuta el sistema operativo junto con Python y el código, una función llamada #machine() te lo dirá. Como anteriormente, la función devuelve una cadena.

from platform import machine

print(machine())
