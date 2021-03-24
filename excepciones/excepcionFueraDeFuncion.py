def badFun(n):
    return 1 / n

try:
    badFun(0)
except ZeroDivisionError:
    print("¿Que pasó? ¡Se lanzo una excepción!")

print("FIN.")
