import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision = 2)   # 2 cifras decimales
np.set_printoptions(suppress = True) # sin formato exponencial

def aprox1(f, g, a, b, n):
    # Calcula el poli de aprox de grado g para n ptos equiespaciados
    # de la función f en [a, b]
    x = np.linspace(a, b, n)
    y = f(x)
    
    V = np.ones((n, g+1))
    for i in range(1, g+1):
        V[:, i] = V[:, i-1] * x
    C = np.dot(V.T, V) # matriz de coeficientes
    print('\nMatriz del sistema\n', C)
    d = np.dot(V.T, y) # matriz de términos independientes
    print('\nTérminos independientes\n', d)
    
    p = np.linalg.solve(C, d)
    
    p = p[::-1]
    print('\nSolución del sistema\n', p)
    
    xp = np.linspace(a, b)  # 50 puntos en [a, b]
    yp = np.polyval(p, xp)  # valor del polinomio p en esos puntos    
    plt.figure()
    plt.plot(xp, yp)
    plt.plot(x, y, 'o')
    plt.show()

f = lambda x: np.sin(x) ; a = 0.; b = 2.; n = 5; g = 2 
aprox1(f, g, a, b, n)

f = lambda x: np.cos(np.arctan(x)) - np.log(x+5)
a = -2.; b = 0.; n = 10; g = 4 
aprox1(f, g, a, b, n)

x = np.linspace(0, 2, 5)
y = np.sin(x)
# Coeficientes del poli aprox con polyfit, 2 = grado poli aprox
pol = np.polyfit(x, y, 2)
print('\nPol: ', pol)
