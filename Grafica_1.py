import matplotlib.pyplot as plt
import numpy as np

# Definimos la función y(x) que representa la línea 2x + y = 5
def y(x):
    return 5 - 2*x

# Generamos un arreglo de 100 valores de x en el rango de -5 a 5 utilizando la función linspace de NumPy
x = np.linspace(-5, 5, 100)

# Calculamos los valores de y correspondientes a cada valor de x utilizando la función y(x)
y_values = y(x)

# Creamos una figura y un conjunto de ejes utilizando la función subplots de Matplotlib
fig, ax = plt.subplots()

# Agregamos la línea que representa la función y(x) en los ejes ax utilizando la función plot de Matplotlib,
# y añadimos una etiqueta a la leyenda
ax.plot(x, y_values, label='2x + y < 5')

# Llenamos el área bajo la curva de la línea utilizando la función fill_between de Matplotlib,
# estableciendo el límite inferior como -5 y el límite superior como los valores de y_values donde y_values es mayor que -5.
# Añadimos transparencia y un color gris a la zona sombreada.
ax.fill_between(x, y_values, -5, where=y_values>-5, color='gray', alpha=0.3)

# Agregamos líneas de referencia horizontal y vertical en el origen utilizando las funciones axhline y axvline de Matplotlib.
# Establecemos el grosor de las líneas a 1 y el color a negro.
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

# Establecemos los límites de los ejes x e y utilizando las funciones set_xlim y set_ylim de Matplotlib.
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Agregamos una leyenda a la figura utilizando la función legend de Matplotlib.
ax.legend()

# Mostramos la figura
plt.show()

