#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 4(10)
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dy/dx
def modelo(v,x):
    dvdx = (32/v) - 1/v
    return dvdx
 
# Condição inicial
y0 = [1,1.5,2,2.5,3,3.5,4,5,6,7,9,10,11]
 
# Intervalo de tempo
t = np.linspace(0,25,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y, linewidth=2, label="y(x)")
plt.legend()
plt.xlabel('x')     
plt.ylabel('v(x)')
plt.grid()
plt.show()