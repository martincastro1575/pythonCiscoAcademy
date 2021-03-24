#En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.
#No será algo difícil. La función tendrá tres parámetros - uno para cada lado.
#Regresará True si todos los lados pueden formar un triángulo, y False de lo contrario. En este caso, esUnTringulo es un buen nombre para dicha función.

def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

