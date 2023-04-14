import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad # para calcular el valor de una integral

np.set_printoptions(precision = 2)   # 2 cifras decimales
np.set_printoptions(suppress = True) # sin formato exponencial 

def aprox2(f, g, a, b):
    # Calcula el poli de aprox de grado g para la función f en [a, b]
    C = np.zeros((g + 1, g + 1)) # matriz de coeficientes
    d = np.zeros(g + 1) # matriz de términos independientes
    for i in range(g + 1):
        for j in range(g + 1):
            exp = i + j
            iC = lambda x: x**exp
            # quad devuelve el valor de la integral [0] y una cota del error [1]
            C[i, j] = quad(iC, a, b)[0]
        id = lambda x: (x ** i) * f(x)
        d[i] = quad(id, a, b)[0]
        
    print('\nMatriz del sistema\n', C)
    print('\nTérminos independientes\n', d)
    
    p = np.linalg.solve(C, d)
    p = p[::-1]
    print('\nSolución del sistema\n', p)
    
    xp = np.linspace(a, b)
    yp = np.polyval(p, xp)    
    plt.figure()
    plt.plot(xp, f(xp), 'r-', label = 'función')
    plt.plot(xp, yp, label = 'polinomio')
    plt.legend()
    plt.show()

g = 2; a = 0.; b = 2.
f1 = lambda x: np.sin(x)
aprox2(f1, g, a, b)

g = 4; a = -2.; b = 0.
f2 = lambda x: np.cos(np.arctan(x)) - np.log(x + 5) 
aprox2(f2, g, a, b)
