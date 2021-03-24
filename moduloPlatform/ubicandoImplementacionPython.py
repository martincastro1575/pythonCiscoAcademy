#Si necesitas saber qué versión de Python está ejecutando tu código, puedes verificarlo utilizando una serie de funciones dedicadas, aquí hay dos de ellas:

#    python_implementation() → devuelve una cadena que denota la implementación de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
#    python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
#        la parte mayor de la versión de Python.
#        la parte menor,
#        el número de nivel del patch.


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
