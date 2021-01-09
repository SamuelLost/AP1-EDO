#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4(5)
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    dydx = -((y**2) * np.cos(x) + 3*(x**2)*y + 2*x)/(2*y * np.sin(x) + (x**3) + np.log(y))
    return dydx
#c = 1
y0 = [1,1.5,2,2.5,3]

x = np.linspace(1,1.3,100)
y = odeint(modelo, y0, x,)
plt.plot(x,y,linewidth=3, label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x",)
plt.ylabel("y (x)")
plt.show()