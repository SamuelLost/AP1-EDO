#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 4(7)
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dy/dt
def modelo(y,t):
    dydt = (2*t*y*(y**3 - 1))/(3*(1+t**2))
    return dydt
 
# Condição inicial
y0 = [0,1,2]
 
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