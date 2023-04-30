# Importar la biblioteca PuLP
import pulp

# Crear el problema de maximización
prob = pulp.LpProblem('Producción', pulp.LpMaximize)

# Definir las variables
x1 = pulp.LpVariable('x1', lowBound=0, upBound=3, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, upBound=5, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, upBound=x1+x2, cat='Integer')

# Definir la función objetivo
prob += x1 + x2

# Agregar las restricciones
prob += x3 == x1 + x2 - 1  # Se requiere una hora de ensamblaje por unidad de producto
prob += x1 + x2 <= 8      # No se pueden exceder las 8 horas de producción en total

# Resolver el problema
prob.solve()

# Mostrar la solución
print('La producción óptima es:')
print('x1 =', pulp.value(x1))
print('x2 =', pulp.value(x2))
print('x3 =', pulp.value(x3))
print('Cantidad total de unidades producidas por hora =', pulp.value(x1 + x2))
