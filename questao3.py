#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 3
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    r = 1; k = 1
    dydx = (r*y)-k*(y**2)
    return dydx
#c = 1
y0 = [1.58, 2.08, 2.58,3.08]

x = np.linspace(-5,2,100)
y = odeint(modelo, y0, x)
plt.plot(x,y,linewidth=2,label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x",)
plt.ylabel("y (x)")
plt.show()