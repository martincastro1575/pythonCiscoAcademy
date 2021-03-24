def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254

def lbsakg(lb):
    return lb * 0.45359237
    
def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

#El primer print devuelve None
print(imc(352.5, 1.65))


#Este print devuelve el IMC, pero pasa argumentos en el sistema Europe directamento
print(imc(52.5, 1.65))


#Este print devuelve el IMC, pasa los argumentos en el sistema ingles (libras / pies,pulgadas)
#estos argumentos se convierten al sistema europeo y devuelven el IMC correcto
print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))
