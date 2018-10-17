# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Отрисовка одной зависимости
def plotF(f,tit='',xl='x',yl='y',lim=None,ylim=None,flag=True):
    plt.close(2)
    plt.title(tit)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)


    if lim or ylim:
        axes = plt.gca()
        if ylim:
            axes.set_ylim([ylim[0], ylim[1]])
        if lim:
            axes.set_xlim([lim[0], lim[1]])

    plt.plot(f.x, f.y, linewidth=1,alpha=0.7, color='b')
    if flag:
        plt.show()

# Отрисовка n зависимостей
def subplotFs(funcs,h,w,lim=None,ylim=None):

    plt.rcParams.update({'font.size': 12})
    plt.figure(figsize=(10, 50))
    for i in range(1,len(funcs)+1):
            plt.subplot(h, w, i)
            plotF(funcs[i-1],funcs[i-1].title,lim=lim,ylim=ylim, flag=False)
    plt.subplots_adjust(hspace=0.4)
    plt.show()

def Barf(f,bins=100,notmy=True,tit='Плотность вероятности',xl='x',yl='y'):

    plt.close(2)

    plt.rcParams.update({'font.size': 11})
    plt.figure(figsize=(10, 50))
    plt.xlabel('Значение')
    plt.ylabel('Количество')
    plt.title(tit)

    if notmy:
        plt.hist(f, bins, range=(-1,1), facecolor='blue', alpha=0.5,edgecolor='white', linewidth=0.5)
    else:
        plt.bar(f[1],f[0], alpha=0.8,width=0.02,edgecolor='white', linewidth=0.5)

    plt.subplots_adjust(left=0.15)

    plt.show()