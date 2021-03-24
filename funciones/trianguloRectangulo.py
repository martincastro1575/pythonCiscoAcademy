def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

#Valores de prueba para determinar si es triangulo rectangulo
# 5,3,4 -> True
# 6,3,4 -> False

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

texto = "Pero no es Triangulo rectangulo."
if esUnTriangulo(a, b, c):
    if esUnTrianguloRectangulo(a,b,c):
        texto = "Y es Triangulo rectangulo."
        
    print("Felicidades, puede ser un triángulo. ", texto)
    
else:
    print("Lo siento, no puede ser un triángulo.")

