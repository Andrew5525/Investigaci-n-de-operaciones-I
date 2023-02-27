import numpy as np
import matplotlib.pyplot as plt

# Definir los límites de los ejes x e y
x_min, x_max = -10, 10
y_min, y_max = -10, 10

# Crear una malla de puntos en el plano xy
x, y = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))

# Evaluar la función en cada punto de la malla
z = y - x - 2

# Graficar la región donde la función es mayor que cero (y>x+2)
plt.contourf(x, y, z, levels=[0, np.inf], colors=['blue'])

# Configurar los ejes y agregar etiquetas
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('x')
plt.ylabel('y')

# Mostrar la gráfica
plt.show()
