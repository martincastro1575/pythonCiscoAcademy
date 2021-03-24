from sys import path

path.append('packages')

#import extra.iota
# import extra.good.best.sigma
# import extra.good.best.tau

from extra.iota import FunI
from extra.good.best.sigma import FunS
from extra.good.best.tau import FunT

#print(extra.iota.FunI())
# print(extra.good.best.sigma.FunS())
# print(extra.good.best.tau.FunT())

print(FunI())
print(FunS())
print(FunT())
