def badFun(n):
    try:
        return 1 / n
    except ZeroDivisionError:
        print("¡Problema de divion entre cero (0)")
    return None

badFun(0)

print("FIN.")
