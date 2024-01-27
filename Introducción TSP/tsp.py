import numpy as np
from itertools import permutations
from time import time


def dist(xi, xj):
    return np.linalg.norm(xi - xj)

# Definimos la distancia total para un camino
def H(x):
    d=0
    for i, elem in enumerate(x):
        try:
            d += dist(elem, x[i+1])
        except:
            d += dist(elem, x[0])
    return d


# Función para resolver de forma exacta
def TSP(x):
    # Eliminamos el primer elemento
    perm = x[1:]
    caminos = list(permutations(perm))
    optimo = None
    dist_optima = float('inf')
    for i, c in enumerate(caminos):
        c = np.vstack([x[0], c, x[0]])
        d = H(c)
        if d < dist_optima:
            optimo = c
            dist_optima = d
    return optimo, dist_optima

def vmc(punto, puntos_restantes):
    dist_min = float('inf')
    vecino_mas_cercano = None
    for i, punto_restante in enumerate(puntos_restantes):
        distancia = dist(punto, punto_restante)
        if distancia < dist_min:
            j = i
            dist_min = distancia
            vecino_mas_cercano = punto_restante


    return vecino_mas_cercano, j


# Vamos a programar un método del vecino más cercano
def metodo_vecino_cercano(y):
    puntos_restantes = list(y)
    dist_menor = float('inf')
    camino_menor = None
    inicio = time()
    for i, elem in enumerate(puntos_restantes):
        # Empezamos en el primer punto:
        camino_aprox = [elem]
        restantes = puntos_restantes.copy()
        restantes.pop(i) # una vez visitado lo quitamos de la lista de puntos restantes

        # Vamos a hacer un bucle para ir avanzando en el camino
        while restantes:
            punto_actual = camino_aprox[-1]
            vecino_cercano, i = vmc(punto_actual, restantes)
            camino_aprox.append(vecino_cercano)
            restantes.pop(i)

        # Añadimos el punto de inicio al final para acabar el camino:
        camino_aprox.append(camino_aprox[0])
        camino_aprox = np.array(camino_aprox)
        # Calculamos la distancia total:
        distancia_total = H(camino_aprox)
        if distancia_total < dist_menor:
            dist_menor = distancia_total
            camino_menor = camino_aprox
    fin = time()
    tiempo = fin-inicio
    return dist_menor, camino_menor, tiempo
