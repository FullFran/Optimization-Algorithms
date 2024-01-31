import numpy as np

def generador_congruencial_lineal(a, b, M, n:int, x0 = 1):
    '''
    Generador congruencial lineal
    x_i = (a * x_{i-1} + b) mod M / M
    '''
    # Creamos el vector para los valores y de paso
    # Iniciamos el primer valor a la semilla.
    # Nota: lo inicializamos a n+1 porque vamos a quitar la semilla
    # de los números resultantes y queremos hacer n números
    x = x0 * np.ones(n+1)
    # Generamos los valores con el algoritmo
    for i in range(1, n+1):
        x[i] = ((a * x[i - 1] + b) % M)
    # Normalizamos los valores 
    # Y quitamos el valor referente a la semilla
    x = x[1:]/M 
    return x

def Fibonacci(a, b, M, n:int, mu:int=1, nu:int=2, x0 = 1, x1 = 1):
    '''
    Generador de Fibonacci
    x_i = (a * x_{i-mu} + b * x_{i-nu}) mod M / M
    '''
    # primero generamos un array para introducir los valores en el.
    x = x0 * np.ones(n+max(mu,nu)) # Le añadimos valores adicionales 
    # para cogerlos para generar los primeros números.
    x[1] = x1 # Inicializamos el segundo valor a la semilla.
    for i in range(max(mu,nu), n+max(mu,nu)): 
        # En el bucle recorremos los n ultimos valores del array para generar n números.
        x[i] = ((a * x[i - mu] + b * x[i - nu]) % M)
    x = x[max(mu,nu):] / M# Nos quedamos solo con los n valores generados y los normalizamos.
    return x
