#Escenario

#En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

#    1.- Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
#    2.- Si es par, evalúa un nuevo c0 como c0 ÷ 2.
#    3.- De lo contrario, si es impar, evalúe un nuevo  c0 como 3 × c0 + 1.
#    4.- Si c0 ≠ 1, salta al punto 2.

#La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
#Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para #lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.


c0 = int(input("Ingrese una valor numerico: "))
pasos = 0

#El if evalua que no ingresen un numero negativo
if c0 > 0:
    
    while c0 != 1:
        #El if evalua si el numero es para o impar
        if not (c0 % 2):
            c0 /= 2
        else:
            c0 = 3 * c0 +1
        print(int(c0))
        
        pasos += 1
        
        if c0 == 1:
            break
        
print("Cantidad de pasos para llegar al objetivo: ", pasos)
