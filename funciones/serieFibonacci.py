def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

n = int(input("Ingrese un valor entero para generar la serie Fibonacci: "))
for i in range(1, n + 1): # probando
    print(i, "->", fib(i))
