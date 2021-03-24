def isPrime(num):
    
    if num < 1:
        return False
    
    for n in range(2,int(num ** 0.5 + 1)):
        if num % n == 0:
            return False
    
    return True

for i in range(1, 50):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
