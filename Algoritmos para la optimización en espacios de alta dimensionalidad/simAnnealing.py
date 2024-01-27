import numpy as np
import matplotlib.pyplot as plt

from IPython.display import clear_output
# Vamos a usar el algoritmo de simulated annealing para resolver el problema del viajante

# Definimos las ciudades:
def ciudades(N)->np.ndarray:
    '''Función para generar N ciudades aleatorias'''
    X = np.random.rand(N,2)
    return X

class simulatedAnnealing():
    '''Clase para resolver el problema del viajante con el algoritmo de simulated annealing'''
    def __init__(self, cities, T0=100, Tf = 0.001,  coolingRate=0.9999):
        '''
        cities: array con las coordenadas de las ciudades
        T0: temperatura inicial
        Tf: temperatura final
        coolingRate: factor de enfriamiento
        '''
        self.ciudades = cities
        self.N = len(self.ciudades)
        self.T = T0
        self.Tf = Tf
        self.coolingRate = coolingRate
        self.route = list(np.arange(self.N))+[0]
        self.dist_matrix = self.dist_matrix()
        self.total_dist = self.totalDistance(self.route)

        self.distances = [] 
        self.temperatures = []
        self.maxIter = -np.log(self.T/self.Tf)/np.log(self.coolingRate)

    def dist_matrix(self):
        '''
        Función para calcular la matriz de distancias
        '''
        d = np.zeros((self.N,self.N))
        for i in range(self.N):
            for j in range(self.N):
                d[i][j] = np.linalg.norm(self.ciudades[i]-self.ciudades[j])
        return d
    
    def totalDistance(self, route):
        '''
        Función para calcular la distancia total de una ruta.
        '''
        return np.sum(self.dist_matrix[route,np.roll(route,-1)])
    def newRoute(self, method='swap'):
        '''
        Función para generar una nueva ruta a partir de la actual.
        method: método para generar la nueva ruta. Puede ser 'swap' o 'inverse'
        '''
        if method not in ['swap','inverse']:
            # Si el método no es válido, se usa swap
            method = 'swap'
        new_route = np.copy(self.route)

        # Generamos la nueva ruta con un swap aleatorio:
        i,j = np.random.randint(1,self.N,2)
        while j==i:
            j = np.random.randint(1,self.N)
        if method == 'swap':
            new_route[i],new_route[j] = new_route[j],new_route[i]
        # Generamos la nueva ruta con un inverse aleatorio:
        if method == 'inverse':
            if i>j:
                i,j = j,i
            new_route[i:j+1] = new_route[i:j+1][::-1]
        return new_route
    
    def run(self, newRouteMethod='swap'):
        '''
        Función para simular el enfriamiento de un sistema.
        newRouteMethod: método para generar la nueva ruta. Puede ser 'swap' o 'inverse'
        '''
        # iteramos hasta que la temperatura sea menor que la temperatura final
        i = 0
        while self.T > self.Tf:
            # Guardamos la distancia y la temperatura en cada iteración
            self.distances.append(self.total_dist)
            self.temperatures.append(self.T)

            i += 1

            # Generamos una nueva ruta
            new_route = self.newRoute(method=newRouteMethod)
            new_dist = self.totalDistance(new_route)

            # Si la nueva distancia es menor, la aceptamos.
            if new_dist < self.total_dist:
                self.route = new_route
                self.total_dist = new_dist
            else:
                # Si la nueva distancia es mayor, la aceptamos con una probabilidad
                # que depende de la temperatura (arrhenius)
                if np.random.rand() < np.exp(-(new_dist-self.total_dist)/self.T):
                    self.route = new_route
                    self.total_dist = new_dist
            # Enfriamos el sistema
            self.T *= self.coolingRate
            if i % 10000 == 0:
                clear_output(wait=True)
                print(f'Iteración {i} de {self.maxIter:.0f}')

                print(f'Distancia total = {self.total_dist:.2f}, Temperatura = {self.T:.3f}')

        clear_output(wait=True)
        print(f'Iteración {i} de {self.maxIter:.0f}')

        print(f'Distancia total = {self.total_dist:.2f}, Temperatura = {self.T:.3f}')
        # Cuando acaba mostramos la solución.
        self.plotRoute()
        

    def graficAnnealing(self, newRouteMethod='swap'):
        '''
        Función para simular el enfriamiento de un sistema.
        newRouteMethod: método para generar la nueva ruta. Puede ser 'swap' o 'inverse'
        '''
        # iteramos hasta que la temperatura sea menor que la temperatura final
        i = 0
        while self.T > self.Tf:
            i += 1
            # Guardamos la distancia y la temperatura en cada iteración
            self.distances.append(self.total_dist)
            self.temperatures.append(self.T)

            # Generamos una nueva ruta
            new_route = self.newRoute(method=newRouteMethod)
            new_dist = self.totalDistance(new_route)

            # Si la nueva distancia es menor, la aceptamos.
            if new_dist < self.total_dist:
                self.route = new_route
                self.total_dist = new_dist
            else:
                # Si la nueva distancia es mayor, la aceptamos con una probabilidad
                # que depende de la temperatura (arrhenius)
                if np.random.rand() < np.exp(-(new_dist-self.total_dist)/self.T):
                    self.route = new_route
                    self.total_dist = new_dist
            # Enfriamos el sistema
            self.T *= self.coolingRate
        # mostramos la solución.
            if i%10000 == 0:
                self.plotRoute()
                clear_output(wait=True)
        self.plotRoute()
        
    def plotRoute(self):
        '''
        Función para mostrar la ruta y la evolución de la distancia.
        '''
        
        plt.figure(figsize=(10,5))
        plt.subplot(1,2,1)
        plt.plot(self.ciudades[self.route,0],self.ciudades[self.route,1],'o-')
        plt.title(f'Distancia total = {self.total_dist:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
        for i in range(self.N):
            plt.text(self.ciudades[i][0]*1.01, self.ciudades[i][1], i, fontsize=10)
        plt.subplot(1,2,2)
        plt.title('Evolución de la distancia')
        plt.plot(self.distances, '-')
        plt.xlabel('Iteración')
        plt.ylabel('Distancia total')

        plt.show()