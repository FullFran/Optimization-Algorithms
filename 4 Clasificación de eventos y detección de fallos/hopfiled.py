import numpy as np 
from PIL import Image

class HopfieldNet:
    def __init__(self, image_shape: tuple):
        self.image_shape = image_shape
        self.size = image_shape[0] * image_shape[1]
        self.weights = np.zeros((self.size, self.size))
    
    def train(self, patterns: list):
        '''
        Entrena la red de Hopfield con los patrones de entrenamiento
        Siguiendo la regla de actualización: W = (sum(p_i * p_i^T) - I)/N
        patterns: lista de patrones de entrenamiento

        Como sabemos, los pesos de la red de Hopfield nos indican la correlación
        entre las neuronas. Esto es que si dos neuronas (pixeles en la imagen en nuestro caso)
        están correlacionadas, cuando una de ellas cambie de estado, la otra también lo hará.
        Es decir que si un pixel vale 1, el otro también valdrá 1 y si uno vale -1, el otro también.

        Dando la matriz de pesos una matriz de 1 y -1 de N x N, donde N es el número de neuronas, en nuestro caso el número de pixeles de la imagen. 
        
        '''
        for pattern in patterns:
            # Aplanamos el patrón para que sea un vector
            pattern = np.array(pattern)
            pattern = pattern.flatten()
            # Actualizamos los pesos utilizando el producto externo
            self.weights += np.outer(pattern, pattern)
        
        # Ponemos los pesos de la diagonal a 0 (no hay conexiones de una neurona consigo misma)
        # Esta condición es como restar la matriz identidad
        np.fill_diagonal(self.weights, 0)
        # Normalizamos los pesos dividiendo por el tamaño (dividir por N)
        self.weights /= len(patterns)
    
    def update(self, state: np.ndarray, steps: int=1, activation_function=np.sign)->np.ndarray:
        '''
        Actualiza el estado de la red de Hopfield
        state: estado inicial de la red
        steps: número de pasos de actualización
        activation_function: función de activación


        Como sabemos, la red de Hopfield es como un algoritmo de metropolis Hasting con temperatura 0 en este caso, es decir que solo acepta estados que disminuyan la energía de la red. 
        Así la dinámica consiste en elegir una neurona al azar y actualizarla, invirtiendo su valor si esto disminuye la energía de la red, que está contenida en la matriz de pesos.
        '''
        state = state.flatten() # Aplanamos el estado inicial
        for _ in range(steps):
            # Elegimos una neurona al azar para actualizar
            unit_to_update = np.random.randint(self.size)
            # Calculamos la activación de la neurona
            # como a_i = sum(w_ij * s_j) sin bias
            a = np.dot(self.weights[unit_to_update, :], state)
            # Actualizamos la neurona con la función de activación
            state[unit_to_update] = activation_function(a)
        return state # Devolvemos el estado como un vector (aplanado)
    
    def energy(self, state: np.ndarray)->float:
        '''
        Calculamos la energía del estado con:
        E = -1/2 * sum(w_ij * s_i * s_j) - sum(b_i * s_i)
        Siendo b el bias (en nuestro caso no hay bias)

        state: estado de la red

        Aquí vemos como el parámetro que usamos para actualizar la red en la función anterior, es la energía de la red sin bias.
        '''
        state = state.flatten()
        # Calculamos la energía de la red
        E = -0.5 * np.dot(np.dot(state.T, self.weights), state)
        # Devolvemos la energía como un escalar
        return E
    
    def print_state(self, state: np.ndarray):
        '''
        Devuelve el estado como una matriz de la forma de la imagen
        '''
        state = state.reshape((self.image_shape[0], self.image_shape[1]))
        return state

def preprocesar(imagen, umbral=128, shape=(75,75))->np.ndarray:
    imagen = Image.open(imagen)
    imagen = imagen.resize(shape)
    imagen = imagen.convert('L')
    imagen = imagen.point(lambda x: -1 if x < umbral else 1)
    imagen = np.array(imagen)
    imagen = np.where(imagen == 0, -1, imagen)
    return imagen

