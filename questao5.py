#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 5
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dP/dt
def modelo(P,t):
    k = 0.13863
    dPdt = k*P
    return dPdt
 
# Condição inicial
y0 = [50,150,200]
 
# Intervalo de tempo
t = np.linspace(0,20,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y,linewidth=3, label="P(t)")
plt.legend()
plt.xlabel('t')     
plt.ylabel('P(t)')
plt.grid()
plt.show()