__counter = 0


def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some test for you")
    l = [i + 1 for i in range(5)]
    print(sum1(l) == 15)
    print(prodl(l) == 120)
else:
    print("I like to be a module")


