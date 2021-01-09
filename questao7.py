#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 7
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dq/dt
def modelo(q,t):
    E0 = 10
    C = 0.68
    k1 = 1
    k2 = 1
    dqdt = (E0*C - q)/(C*(k1+k2*t))
    return dqdt
 
# Condição inicial
y0 = [0,1,2]
 
# Intervalo de tempo
t = np.linspace(0,3,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y, linewidth=3, label="q(t)")
plt.legend()
plt.xlabel('t')     
plt.ylabel('q(t)')
plt.grid()
plt.show()