#Crea un programa con un bucle for y una declaración break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando #llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo: 

aux = ""
for ch in "martin.castro1575@gmail.com":
    
    if ch == "@":
        break
        # línea de código
    # línea de código
    
    aux += ch

print(aux, len(aux))
