import matplotlib.pyplot as plt
import numpy as np

# Función para graficar la recta 2x + 3y = 60
def plot_line():
    x = np.linspace(0, 30, 100)
    y = (60 - 2*x)/3
    plt.plot(x, y, 'b-', label='2x + 3y = 60')

# Función para graficar la región sombreada
def plot_region():
    x = np.linspace(0, 20, 100)
    y1 = np.zeros_like(x)
    y2 = (60 - 2*x)/3
    plt.fill_between(x, y1, y2, where=(y2 >= y1), alpha=0.5)

# Configuración del gráfico
plt.figure(figsize=(8, 6))
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Graficar la recta y la región sombreada
plot_line()
plot_region()

# Mostrar la leyenda y el gráfico
plt.legend(loc='upper right')
plt.show()
