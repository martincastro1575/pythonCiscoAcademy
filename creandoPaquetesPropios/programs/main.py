from sys import path

path.append('modules')

#import module

from module import sum1, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
l = [i +1 for i in range(5)]

print(sum1(zeroes))
print(prodl(ones))
print(sum1(l))
print(prodl(l))