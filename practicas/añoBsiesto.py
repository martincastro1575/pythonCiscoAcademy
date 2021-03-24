año = int(input("Introduzca un año:"))

#
# Coloca tu código aquí.
#

if año >= 1582:
    if (año % 4 != 0):
        tipo_año = "común"
    elif (año % 100 != 0):
        tipo_año = "bisiesto"
    elif (año % 400 != 0):
        tipo_año = "comun"
    else:
        tipo_año = "bisiesto"
else:
    print("El año ", año, "no se encuentra dentro del periodo gregoriano")

print(año, "es", tipo_año)
