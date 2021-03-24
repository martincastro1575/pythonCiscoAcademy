#Escenario

#El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido #por cada 100 kilómetros.

#En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

#Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(milas por galón), y viceversa.

#Las funciones:

#    Se llaman l100kmampg y mpgal100km respectivamente.
#    Toman un argumento (el valor correspondiente a sus nombres).

#Complementa el código en el editor.

#Ejecuta tu código y verifica si tu salida es la misma que la nuestra.

#Aquí hay información para ayudarte:

#    1 milla = 1609.344 metros.
#    1 galón = 3.785411784 litros



def l100kmtompg(liters):
    km = 100
    millas = (km * 1000) / 1609.344
    galon = liters / 3.785411784
    
    return millas / galon


def mpgtol100km(miles):
    km = (miles * 1609.344) / 1000
    liter = 3.785411784 * 100
    
    return liter / km 


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
