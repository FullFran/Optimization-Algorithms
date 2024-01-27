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
        self.weights /= self.size
    
    def update(self, state: np.ndarray, steps: int=1, activation_function=np.sign)->np.ndarray:
        '''
        Actualiza el estado de la red de Hopfield
        state: estado inicial de la red
        steps: número de pasos de actualización
        activation_function: función de activación
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

def preprocesar(imagen, umbral=128)->np.ndarray:
    imagen = Image.open(imagen)
    imagen = imagen.resize((75, 75))
    imagen = imagen.convert('L')
    imagen = imagen.point(lambda x: -1 if x < umbral else 1)
    imagen = np.array(imagen)
    imagen = np.where(imagen == 0, -1, imagen)
    return imagen