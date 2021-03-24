dic = {}
lst = ['a','b','c','d']

for i in range(len(lst) - 1):
    dic[lst[i]] = (lst[i], )

for i in sorted(dic.keys()):
    k = dic[i]
    print(k)


def fun1(a):
    return a ** a

def fun2(a):
    return fun1(a) * fun1(a)

print(fun2(2))

def funa(x):
    if x % 2 == 0:
        return 1
    else:
        return

#print(funa(funa(2)) + 1) #Devuelve error

def funb(x):
    global y
    y = x * x
    return y

funb(2)
print(y)

def any():
    print(var  + 1, end='')

var = 1
any()
print(var)


print('==============================================')
dct = {'one':'two','three':'one','two':'three'}

v = dct['one']

for k in range(len(dct)):
    v = dct[v]

print(v)

print("*******************************************")
tup = 1,2,4,8,
tup = tup[1:-1]
tup = tup[0]

print(tup)