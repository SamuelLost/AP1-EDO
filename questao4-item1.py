#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4(1)
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    dydx = -(3*(x**2) + 2*x*y + (y**3))/(x**2 + y**2)
    return dydx
#Vetor de condições inicias
y0 = [0.5,1,1.5,2,2.5,3,3.5,4,4.5] 

x = np.linspace(0,4,100)
y = odeint(modelo, y0, x)
plt.plot(x,y,linewidth=3, label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x",)
plt.ylabel("y (x)")
plt.show()