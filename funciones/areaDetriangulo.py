def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

#Valores de prueba para determinar el area
# 1. , 1. , 2. -> True
def areaTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)


a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

#calculo la media raiz de c
c **= .5
if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo", end =", ")
    print("Y su Area es: ", areaTriangulo(a, b, c))
else:
    print("Lo siento, no puede ser un triángulo.")
