import numpy as np
import matplotlib.pyplot as plt

# Creamos un array de puntos en el rango [-5, 5] con incrementos de 0.1
x = np.arange(-5, 5, 0.1)

# Creamos una línea horizontal en y = 5
y = np.ones_like(x) * 5

# Creamos una figura y un eje
fig, ax = plt.subplots()

# Graficamos la línea horizontal en el eje y
ax.plot(x, y, label='y = 5')

# Rellenamos la región debajo de la línea con un color gris claro
ax.fill_between(x, 0, y, where=y >= 0, interpolate=True, color='lightgray')

# Agregamos etiquetas a los ejes y un título
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graficar y ≤ 5')

# Mostramos la leyenda y el gráfico
ax.legend()
plt.show()
