import numpy as np
import matplotlib.pyplot as plt

# Definir los límites de los ejes x e y
x_min, x_max = -5, 5
y_min, y_max = -5, 5

# Crear una malla de puntos en el plano xy
x, y = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))

# Evaluar cada desigualdad en cada punto de la malla
z1 = 2*x + y
z2 = 2*y - 1
z3 = x - y

# Graficar cada desigualdad por separado
plt.contourf(x, y, z1, levels=[3, np.inf], colors=['blue'])
plt.contourf(x, y, z2, levels=[0, np.inf], colors=['green'])
plt.contourf(x, y, z3, levels=[-np.inf, 0], colors=['red'])

# Configurar los ejes y agregar etiquetas
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('x')
plt.ylabel('y')

# Mostrar la gráfica
plt.show()

# Evaluar las tres desigualdades simultáneamente
z = (z1 > 3) & (z2 > 0) & (z3 >= 0)

# Graficar la región que satisface las tres desigualdades
plt.contourf(x, y, z, levels=[0, 1], colors=['blue'])

# Graficar las rectas correspondientes a cada desigualdad
plt.contour(x, y, z1, levels=[3], colors=['black'])
plt.contour(x, y, z2, levels=[0], colors=['black'])
plt.plot(np.linspace(-5, 5), np.linspace(-5, 5), color='black')

# Configurar los ejes y agregar etiquetas
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('x')
plt.ylabel('y')

# Mostrar la gráfica
plt.show()
