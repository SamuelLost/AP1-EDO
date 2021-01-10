#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 4(6)
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dy/dx
def modelo(y,x):
    dydx = -(x**2 + 2*x*y - y**2)/(y**2 + 2*x*y - x**2)
    return dydx
 
# Condição inicial
y0 = [.5,1,1.5,2,2.5,3,3.5]
 
# Intervalo de tempo
t = np.linspace(0,.5,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y,linewidth=3, label="P(t)")
plt.legend()
plt.xlabel('t')     
plt.ylabel('P(t)')
plt.grid()
plt.show()