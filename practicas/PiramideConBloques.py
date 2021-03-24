#Escenario

#Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

#Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. La pirámide se apila de acuerdo con un principio simple: cada capa #inferior contiene un bloque más que la capa superior

#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

#Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

#Datos de control
# al ingresar (6 bloques) la altura es de (3 capas)
# al ingresar (20 bloques) la altura es de (5 capas)
# al ingresar (1000 bloques) la altura es de (44 capas)


bloques = int(input("Ingrese el número de bloques:"))

capa = 0
while True:
    capa += 1
    bloques -= capa
    if capa >= bloques:
        altura = capa
        break
    
print("La altura de la pirámide:", altura)
