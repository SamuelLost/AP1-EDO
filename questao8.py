#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 8
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dq/dt
def modelo(P,t):
    k = 1
    dPdt = k*P
    return dPdt
 
# Condição inicial
y0 = [100,150,200]
 
# Intervalo de tempo
t = np.linspace(0,2,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y,linewidth=3, label="P(t)")
plt.legend()
plt.xlabel('t')     
plt.ylabel('P(t)')
plt.grid()
plt.show()