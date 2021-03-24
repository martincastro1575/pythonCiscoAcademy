from sys import path

path.append('packages/extrapack.zip')

#import extra.iota
# import extra.good.best.sigma
# import extra.good.best.tau

from extra.iota import FunI as fi
from extra.good.best.sigma import FunS as fu
from extra.good.best.tau import FunT as ft

#print(extra.iota.FunI())
# print(extra.good.best.sigma.FunS())
# print(extra.good.best.tau.FunT())

print(fi())
print(fu())
print(ft())
