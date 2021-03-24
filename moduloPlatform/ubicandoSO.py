#El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

#Existe también una función que puede mostrar todas las capas subyacentes en un solo vistazo, llamada platform. Simplemente devuelve una cadena que describe el entorno; #por lo tanto, su salida está más dirigida a los humanos que al procesamiento automatizado (lo veremos pronto).

#Así es como se puede invocar: platform(aliased = False, terse = False).

#Ahora:

#    aliased → cuando se establece a True (o cualquier valor distinto de cero) puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar #de los comunes.
#    terse → cuando se establece a True (o cualquier valor distinto de cero) puede convencer a la función de presentar una forma más breve del resultado (si lo fuera #posible).


from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))
