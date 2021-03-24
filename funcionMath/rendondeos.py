

# ceil(x) → devuelve el entero más pequeño mayor o igual que x.
# floor(x) → el entero más grande menor o igual que x.
# trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
# factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
# hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las longitudes de los catetos iguales a x e y (lo mismo que sqrt(pow(x, 2) + pow(y, # 2)) pero más preciso).


from math import ceil, floor, trunc

x = 1.4
y = 2.6
print("Valores ingresados: x = ",x, " y = ", y)
print("floor: ", floor(x), floor(y))
print("floor: ", floor(-x), floor(-y))
print("ceil: ",ceil(x), ceil(y))
print("ceil: ",ceil(-x), ceil(-y))
print("trunc: ",trunc(x), trunc(y))
print("trunc: ", trunc(-x), trunc(-y))
