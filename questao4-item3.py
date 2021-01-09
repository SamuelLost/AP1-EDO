#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questão 4(3)
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def modelo(y, x):
    dydx = y-y**3
    return dydx
#c = 1
y0 = [0.425,0.85,1.275,1.7,2.125,2.55,3]

x = np.linspace(0,4,100)
y = odeint(modelo, y0, x)
plt.plot(x,y,linewidth=3, label="y(x)")
plt.legend()
plt.grid()
plt.xlabel("x",)
plt.ylabel("y (x)")
plt.show()