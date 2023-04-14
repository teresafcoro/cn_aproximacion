import numpy as np
import matplotlib.pyplot as plt

# Para poder leer cars.csv
import pandas as pd

# Leer datos (separados por comas)
data = pd.read_csv('cars.csv', sep=',')

# Extraer variables
x = data['weight']
y = data['horsepower']

# Calcular pol de grado 1 con x e y
p = np.polyfit(x, y, 1)

# Estimar la potencia (y) de un coche con peso 3000 libras
peso = 3000
sol1 = np.polyval(p, peso)
print(np.int(sol1), 'horsepower')

# Dibujo del polinomio
xp = np.linspace(min(x), max(x))
yp = np.polyval(p, xp)
plt.figure()
plt.plot(x, y, 'o')
plt.plot(xp, yp, 'r-')
plt.xlabel('weight')
plt.ylabel('horsepower')
plt.plot(peso, sol1, 'ro')
plt.show()

# Nuevas variables extraidas
x = data['horsepower']
y = data['mpg']

# Polinomio de grado 2
p = np.polyfit(x, y, 2)

# Estimar con el valor anterior
sol2 = np.polyval(p, sol1)
print(np.int(sol2), 'mpg')

# Dibujo del polinomio
xp = np.linspace(min(x), max(x))
yp = np.polyval(p, xp)
plt.figure()
plt.plot(x, y, 'o')
plt.plot(xp, yp, 'r-')
plt.xlabel('horsepower')
plt.ylabel('mpg')
plt.plot(sol1, sol2, 'ro')
plt.show()
