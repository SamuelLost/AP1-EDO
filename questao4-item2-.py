#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4(2)
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    dydx = (x+3*y)/(x-y)
    return dydx
#c=1
y0 = [0,0.5,1,1.5,2,2.5,3]

x = np.linspace(0,3,100)
y = odeint(modelo, y0, x)
plt.plot(x,y,linewidth=3, label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y(x)")
plt.show()