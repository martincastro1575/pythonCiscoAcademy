#La instrucción raise también se puede utilizar de la siguiente manera (toma en cuenta la ausencia del nombre de la excepción):
# raise

#Existe una seria restricción: esta variante de la instrucción raise puede ser utilizada solamente dentro de la rama except; usarla en cualquier otro contexto causa un error.

#La instrucción volverá a generar la misma excepción que se maneja actualmente.

#Gracias a esto, puedes distribuir el manejo de excepciones entre diferentes partes del código.

#Observa el código en el editor. Ejecútalo, lo veremos en acción.

#La excepción ZeroDivisionError es generada dos veces:

#    Primero, dentro del try debido a que se intentó realizar una división entre cero.
#    Segundo, dentro de la parte except por la instrucción raise.



def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")
