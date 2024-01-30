

# Optimización en Sistemas Físicos

# y Aplicaciones Industriales

###### Maśter Universitario en Tecnología Física: Investigación y Aplicaciones

Curso 2023-24

# Portfolio de actividades guiadas

###### Francisco Manuel Olmedo Cortés



---

# TEMA 1: Introducción a los problemas de optimización

## ***Resumen y objetivos:***


En esta actividad vamos a resolver el problema del viajante (TSP) con un método exacto y uno aproximado. Comparándolos entre sí. En concreto:

- Fijando el número de ciudades N y sus posiciones (generadas aleatoriamente), analizaremos todos los caminos posibles que empiezan y acaban en la misma ciudad (permutaciones), buscando aquel de mínimo recorrido. Este será nuestro método exacto.
- Con las mismas ciudades, buscaremos una solución aproximada, partiendo de una ciudad y saltando siempre a la más cercana (esto lo haremos para cada ciudad). Este es el método del vecino más cercano.
- Finalmente representaremos las posiciones de las ciudades y los caminos seguidos en el plano.
- Calculamos el tiempo invertido en calcular la solución con cada método y representaremos esto en función de N.
## Resultados:

- Comparación de resultados obtenidos


![](images/Pasted%20image%2020231211170401.png)


![](images/Pasted%20image%2020231211171805.png)



En estas imágenes podemos ver la diferencia entre el camino obtenido con el método aproximado y el exacto. Se puede observar como el resultado obtenido por el método aproximado no tiene por qué dar la solución óptima para el problema.


- Comparación de tiempos de ejecución en función del número de ciudades.


![](images/Pasted%20image%2020240127180621.png)


En la gráfica podemos ver la comparación del tiempo de ejecución en función el número de ciudades para el algoritmo exacto y el aproximado, como podemos observar, el orden de complejidad del algoritmo aproximado es mucho menos que la del algoritmo exacto. Además podemos ver como el algoritmo aproximado escala de forma polinómica ($O(n^2$)) y el exacto escala peor ($O(n!)$).


## Discusión:

Incluir aquí cualquier comentario de interés referente a la activdad,
como por ejemplo:

-   Observamos que para Ns muy pequeños, el algoritmo exacto es más
    rápido, pero este se vuelve extremadamente lento para Ns grandes,
    comparado con el otro.
-   El algoritmo exacto se vuelve inviable para N\>10. Sin embargo,
    podemos usar el algoritmo aproximado para Ns mucho más grandes!

## Anexo(s):

Enumerar aquí los códigos usados:

-   [tsp.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/1%20Introducción%20TSP/tsp.py) (Aquí están las funciones utilizadas para la implementación de la lógica del método exacto y el método aproximado).
- [resultados.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/1%20Introducción%20TSP/resultados.ipynb) (Aquí calculamos los tiempos de ejecución para el método exacto y el método del vecino más cercano y los comparamos, además graficamos la solución para el problema generando ciudades de forma aleatoria).

---
# Tema 2: Fundamentos físico-matemáticos de los algoritmos de optimización.

## Generadores de números aleatorios.

### Resumen y Objetivos:
En esta actividad vamos a implementar varios métodos para la generación de números aleatorios y compararlos entre ellos. En concreto:
- Implementar un generador congruencial lineal y uno de fibonacci. Comparando histogramas entre ellos generando $10^6$ números y la relación del siguiente número en función del anterior para los distintos generadores.
- Implementar métodos para generar números aleatorios distribuidos conforme a una distribución dada por el método de la transformada inversa y el método de aceptación rechazo.

### Resultados:
Nota: En el archivo ejercicios.ipynb se encuentran los ejercicios planteados en las diapositivas resueltos.

![](images/Pasted%20image%2020240123123656.png)

Histogramas de los números generados.

![](images/Pasted%20image%2020240127115142.png)

Relación del número generado con el anterior.

- Método de la transformada inversa:

![](images/Pasted%20image%2020240123133011.png)


- Método de aceptación rechazo:

![](images/Pasted%20image%2020240123133047.png)



### Discusión:
- Podemos observar como el generador de números aleatorios de numpy los genera de una forma muy uniforme, por otro lado, el generador de fibonacci es el que mejor se desempeña de los que hemos desarrollado, mientras tanto, el generador lineal congruencial, los genera de forma menos uniforme y además es muy sensible a los parámentros utilizados.
- En la imagen donde hemos representado la relación del siguiente número con el anterior, hemos ordenado de "mejor" a "peor" generador para ver como "cubren más huecos" es decir, en los mejores generadores desde cada número se puede acceder a más números.
- El método de la transformada inversa es sencillo y más eficiente, pero requiere poder operar de forma analítica la función, lo cual puede no ser viable mientras que el método de aceptación rechazo, aunque es menos ineficiente (ya que tenemos que generar más números aleatorios para conseguir los que buscamos) se puede realizar con cualquier distribución.

### Anexo:
- [generadoresAleatorios.py](https://github.com/FullFran/Optimization-Algorithms/tree/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Generación%20de%20números%20Aleatorios/generadoresAleatorios.py) (Aquí se implementa la lógica de los generadores de números aleatorios).
- [ejercicios.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Generación%20de%20números%20Aleatorios/ejercicios.ipynb) (Aquí se realizan los ejercicios propuestos en la asignatura, comparando los distintos generadores de números aleatorios).

### Resumen y Objetivos:
En esta actividad realizaremos el experimento de la aguja de Buffon, comprobando el orden de convergencia de los métodos de montecarlo. En concreto:
- Implementar un código para estimar el valor de $\pi$ empleando el método de la aguja de Buffon.
- Estudiar la convergencia, determinando que converge con un orden de $\frac{1}{\sqrt N}$.
- Comparar la convergencia para distintos tamaños de la aguja.
### Resultados:
- Estimación de pi con el método de Buffon. 

![](images/Pasted%20image%2020240127184645.png)

- Error en la convergencia en función del número de tiradas y la longitud de la aguja:

![](images/Pasted%20image%2020240123134450.png)

### Discusión:
- En la imagen de la convergencia del error, vemos como hay que "tirar del orden de 10000 agujas" para obtener una precisión de unos 2-3 decimales en la estimación de $\pi$. 
- Haciendo un ajuste, hemos demostrado que el error converge con $N^\frac{-1}{2}$, como vimos en la teoría para los métodos de Monte Carlo. 
- También podemos ver como al aumentar el tamaño de la aguja, se reduce el error como vimos en la teoría.
## Anexo:
- [buffon_needle.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Aguja%20de%20Buffon/buffon_needle.py)  (Aquí implementamos la lógica para la simulación del problema).
- [buffon_needle.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Aguja%20de%20Buffon/buffon_needle.ipynb) (Aquí ejecutamos el código, calculamos los tiempos de ejecución y hacemos el ajuste).

---
# Tema 3: Algoritmos para la optimización en espacios de alta dimensionalidad.

## Resumen y Objetivos:
En esta actividad resolveremos el TSP mediante simulated annealing y un algoritmo genético. En concreto:
- Implementaremos los métodos de simulated annealing y algoritmo genético para resolver el TSP.
- Resolveremos el TSP para distintos números de ciudades con ambos métodos, mostrando la evolución de la distancia de la ruta.

## Resultados:

- Resultados obtenidos por el simulated annealing con 30 ciudades:

![](images/sa30.png)

- Resultados obtenidos por el simulated annealing con 90 ciudades:

![](images/sa90.png)


- Resultados obtenidos por el algoritmo genético con 30 ciudades:

![](images/ga30.png)

- Resultados obtenidos por el algoritmo genético con 90 ciudades:

![](images/ga90.png)





## Discusión:
- En las gráficas podemos observar como tanto el simulated annealing como el algoritmo genético se desempeñan bien a la hora de resolver el TSP reduciendo la distancia recorrida con el tiempo hasta aproximarse a la solución exacta.
- En las gráficas del simulated annealing, podemos observar como en las primeras iteraciones, encontrándose a mayores temperaturas, la distancia recorrida no se reduce a penas, pero el algoritmo está explorando más estados, hasta que se alcanza una temperatura crítica (igual que en el [modelo de issing](https://github.com/FullFran/Optimization-Algorithms/tree/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Trabajo%20Issing/Code)) a la cual el sistema empieza a 'congelarse' y converge a soluciones con menor distancia recorrida. Esto es debido a que al bajar la temperatura, la probabilidad de aceptar peores soluciones disminuye.
- En el algoritmo genético, podemos observar como en cada generación la distancia de la ruta del mejor individuo siempre se reduce o se mantiene, esto es debido a que hemos contemplado Elitismo, haciendo que los mejores individuos pasen directamente a la siguiente generación. Además podemos ver como la distribución del fitness conforme avanzan las generaciones, la mayoría de individuos tienen un mayor fitness (ver usando el método graficRun de la clase GeneticAlgorithm).

## Anexo:
- [simAnnealing.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/simAnnealing.py) (Aquí se implementa la lógica del simulated annealing para resolver el TSP).
- [simAnnealing.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/simAnnealing.ipynb) (Aquí están los resultados obtenidos con el simulated annealing).
- [genetic.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/genetic.py) (Aquí se implementa la lógica del algoritmo genético para resolver el TSP).
- [genetic.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/genetic.ipynb) (Aquí están los resultados obtenidos con el algoritmo genético).

---

# Tema 4: Clasificación de eventos y detección de fallos.

## Resumen y Objetivos:

## Resultados:

## Discusión:

## Anexo: