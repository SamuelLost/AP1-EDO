#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4(9)
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    dydx = (y*np.log(x*y))/(x)
    return dydx
#c = 1
y0 = [1,2,3,4]

x = np.linspace(1,3,100)
y = odeint(modelo, y0, x)
plt.plot(x,y,linewidth=3, label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x",)
plt.ylabel("y (x)")
plt.show()