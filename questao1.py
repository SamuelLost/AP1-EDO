#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 1
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dy/dx
def modelo(y,t):
    a = 10
    b = 10
    r = 1
    dydt = -(np.pi * r**2 * 44.27 * np.sqrt(y))/(a*b)
    return dydt
 
# Condição inicial
y0 = [0, 1, 2, 3]
 
# Intervalo de tempo
t = np.linspace(0,3,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y, linewidth=2, label="y(x)")
plt.legend()
plt.xlabel('t')     
plt.ylabel('y(t)')
plt.grid()
plt.show()