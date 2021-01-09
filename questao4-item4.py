#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4(4)
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    dydx = -(x+y)**2/(2*x*y + x**2 -1)
    return dydx
#c = 1
y0 = [0.1,0.2,0.3,0.4,0.5,0.6]

x = np.linspace(0,.3,100)
y = odeint(modelo, y0, x)
plt.plot(x,y,linewidth=3, label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x",)
plt.ylabel("y (x)")
plt.show()