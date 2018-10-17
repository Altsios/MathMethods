# -*- coding: utf-8 -*-
import numpy as np
from random import uniform
from random import randint
import time

def GenRand(a, c, m, seed, N):
    while N > 0:
        N -= 1
        seed = (a * seed + c) % m
        yield seed

'''
s,e-пределы последовательности x
ss-шаг
'''

class Trend:

    def CopyShift(self,origin,sht=0):
        self.x=origin.x
        self.y=[yk+sht for yk in origin.y]
        self.title="Сдвиг"

    def Spikes(self,p1,p3,p4):

        p1=uniform(0,p1/100)
        pos = []
        while len(pos)!=int(p1*len(self.x)):

            #добавление рандомной позиции
            curpos=randint(0,len(self.x))
            if curpos in pos:
                continue
            pos.append(curpos)

            sign = randint(0, 1)

            if self.y[curpos] < 0:
                self.y[curpos] = self.y[curpos] - (p3 + uniform(-p4, p4))
            else:
                self.y[curpos] = self.y[curpos] + (p3 + uniform(-p4, p4))

        return self
#y=e^a
class LinearF(Trend):

    def __init__(self,x,k=1,b=0,tit='None'):
        self.x=x
        self.y= np.array([k * dx + b for dx in self.x])
        self.title=tit

#y=e^ax
class ExpF(Trend):

    def __init__(self,x,a,tit='None'):
        self.x = x
        self.y = np.exp(self.x * a)
        self.title = tit

class CmpsF(Trend):

    def __init__(self,x,s,e,k1,k2,
                 b1,b2,a1,a2,
                 c1,c2,c3,c4):
        self.x= x
        self.y = [self.myfuncc(dx, s, abs(s - e) / 4, k1, k2, b1, b2, a1, a2,
                     c1,c2,c3,c4) for dx in self.x]

    def myfuncc(self,x, s, N_4, k1, k2, b1, b2, a1, a2,
                c1,c2,c3,c4):
        if x <= s + N_4:
            return np.exp(x * a1)*c1
        elif x <= s + N_4 * 2:
            return (k1 * x + b1)*c2
        elif x <= s + N_4 * 3:
            return (k2 * x + b2)*c3
        else:
            return np.exp(x * a2) * c4

# встроенный генератор случайных чисел
class Rand(Trend):

    def __init__(self,x,S,tit="Встроенный генератор"):
        self.title = tit
        self.x=x
        self.y=[uniform(0, 1) for i in self.x]
        mxx = max(self.y)
        minx = min(self.y)
        self.y=[((xk - minx) / (mxx - minx) - 0.5) * 2 * S
                for xk in self.y]

# Последовательность цифр в числе Pi считается случайной
class SelfRandom(Trend):

    def __init__(self,x,S,tit="Свой генератор"):
        self.title=tit
        a = time.time() % 45
        c = time.time() % 21
        m = time.time() % 67
        seed = time.time() % 999

        self.x = x

        self.y = list(GenRand(a, c, m, seed, len(x)))
        mxx = max(self.y)
        minx = min(self.y)

        self.y = [((xk - minx) / (mxx - minx) - 0.5) * 2 * S
             for xk in self.y]

class Dummy(Trend):

    def __init__(self):
        self.x=None
        self.y=None
        self.title=None