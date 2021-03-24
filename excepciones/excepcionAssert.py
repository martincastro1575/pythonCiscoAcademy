#Ahora es un buen momento para mostrarte otra instrucción de Python, llamada assert (afirmar). Esta es una palabra reservada.
# assert expresión

#¿Como funciona?

#    Evalúa la expresión.
#    Si la expresión se evalúa como True (verdadero), o un valor numérico distinto de cero, o una cadena no vacía, o cualquier otro valor diferente de None, no hará nada más.
#    De lo contrario, automáticamente e inmediatamente genera una excepción llamada AssertionError (en este caso, decimos que la afirmación ha fallado).

#¿Cómo puede ser utilizada?

#    Puedes ponerlo en la parte del código donde quieras estar absolutamente a salvo de datos incorrectos, y donde no estés absolutamente seguro de que los datos hayan sido examinados cuidadosamente antes (por ejemplo, dentro de una función utilizada por otra persona).
#    El generar una excepción AssertionError asegura que tu código no produzca resultados no válidos y muestra claramente la naturaleza de la falla.
#    Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.

#Si las excepciones y la validación de datos son como conducir con cuidado, la aserción puede desempeñar el papel de una bolsa de aire.

import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)
