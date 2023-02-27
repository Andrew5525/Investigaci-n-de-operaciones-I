import matplotlib.pyplot as plt
import numpy as np

# Definir las restricciones
x = np.linspace(0, 200, 1000)
y1 = 180 - 2*x
y2 = 160 - x/2
y3 = 100 - x

# Definir las áreas que satisfacen las restricciones
y4 = np.minimum(y1, y2)
y5 = np.minimum(y4, y3)

# Graficar las restricciones y la región factible
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y1, label='2X + Y = 180')
ax.plot(x, y2, label='X + 2Y = 160')
ax.plot(x, y3, label='X + Y = 100')
ax.fill_between(x, y5, 0, where=(y5 > 0), alpha=0.2)
ax.set_xlim(0, 150)
ax.set_ylim(0, 120)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(loc='upper right')
ax.set_title('Región Factible')
plt.show()
