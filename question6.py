
#!/usr/bin/env python3
# -- coding: utf-8 --
"""
 Question 6
"""
 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Função que retorna dq/dt
def modelo(S,t):
    r = 0.0575
    dSdt = r*S
    return dSdt
 
# Condição inicial
y0 = [5000, 4000, 2000]
 
# Intervalo de tempo
t = np.linspace(0,14,100)
    
# Resolve EDO
y = odeint(modelo, y0, t)
    
# Plota os resultados
plt.plot(t,y,linewidth=3, label="S(t)")
plt.legend()
plt.xlabel('t')     
plt.ylabel('S(t)')
plt.grid()
plt.show()