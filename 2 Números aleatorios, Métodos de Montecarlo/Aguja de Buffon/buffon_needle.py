import numpy as np


def pi_buffon_needle(d: float, l: float, n: int):
    '''
    Función para calcular el valor de pi mediante el método de la aguja de Buffon
    creando en cada iteración una aguja nueva, hasta llegar a n agujas.

    d = longitud de la aguja
    l = distancia entre las rectas
    n = número de agujas
    '''
    # Creamos los parámetros de la aguja
    x = np.random.uniform(0, l, n)
    theta = np.random.uniform(0, np.pi/2, n)

    # Calculamos la posición superior de la aguja
    y = x + d * np.sin(theta)

    # Comprobamos si la aguja se sale de la zona de la recta
    y_out = y > l # Esto nos devuelve booleanos True si se sale y False si no
    m = np.sum(y_out) # Contamos el número de veces que se sale
    m_acum = y_out.cumsum() # Acumulamos los valores booleanos
    # Calculamos la probabilidad
    p = m/n 
    p_acum = m_acum/len(m_acum)
    # Con esto calculamos el valor de pi
    pi = 2 * d / (p * l) 
    pi_acum = 2 * d / (p_acum * l)
    err = np.abs(np.pi - pi)
    err_acum = np.abs(np.pi - pi_acum)
    return pi, err, pi_acum, err_acum

def buffon_needle_random(d: float,l: float,n: int):
    ''' 
    Función para calcular el valor de pi mediante el método de la aguja de Buffon
    pero creando en cada iteración n agujas nuevas en vez de una a una.

    d = longitud de la aguja
    l = distancia entre las rectas
    n = número de agujas
    '''
    pi = []
    err = []
    for i in range(1,n+1):
        x = np.random.uniform(0, l, i)
        theta = np.random.uniform(0, np.pi/2, i)
        y = x + d * np.sin(theta)
        y_out = y > l
        m = np.sum(y_out)
        p = m/i
        pi_aux = 2 * d / (p * l)
        pi.append(pi_aux)
        err.append(np.abs(np.pi - pi_aux))

    return pi, err



