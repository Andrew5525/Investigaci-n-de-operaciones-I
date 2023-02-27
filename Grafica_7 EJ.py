from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Crear problema de maximización
prob = LpProblem("Maximización de beneficios", LpMaximize)

# Variables de decisión
A = LpVariable("A", lowBound=0) # Cantidad de producto A a fabricar
B = LpVariable("B", lowBound=0) # Cantidad de producto B a fabricar

# Función objetivo
prob += 8*A + 10*B, "Beneficio total"

# Restricciones
prob += A + 2*B <= 40, "Restricción de trabajo"
prob += 2*A + B <= 80, "Restricción de material"

# Resolver el problema
prob.solve()

# Imprimir la solución
print("Cantidad óptima de producto A a fabricar: ", value(A))
print("Cantidad óptima de producto B a fabricar: ", value(B))
print("Beneficio total máximo: $", value(prob.objective))

# Crear la gráfica
x = np.linspace(0, 50, 100)
y1 = 20 - 0.5 * x # Restricción de trabajo
y2 = 80 - 2 * x # Restricción de material
plt.plot(x, y1, label='Restricción de trabajo')
plt.plot(x, y2, label='Restricción de material')
plt.fill_between(x, 0, y1, where=y1<=20, color='gray', alpha=0.5)
plt.fill_between(x, 0, y2, where=y2<=40, color='gray', alpha=0.5)
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.xlabel('Cantidad de producto A')
plt.ylabel('Cantidad de producto B')
plt.legend(loc='upper right')

# Agregar punto de solución
plt.scatter(value(A), value(B), s=100, marker='*', color='r', label='Solución óptima')
plt.legend()

# Mostrar la gráfica
plt.show()
