import numpy as np

# Más eficiente para grandes conjuntos de datos
def varianza(*numeros):
    return np.var(numeros)

# Con 10,000 números, numpy es significativamente más rápido
grandes_datos = range(10000)
print(varianza(*grandes_datos))  # Cálculo eficiente
