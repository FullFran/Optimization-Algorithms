

# Optimización en Sistemas Físicos

# y Aplicaciones Industriales

###### Maśter Universitario en Tecnología Física: Investigación y Aplicaciones

<br>

Curso 2023-2024

![](images/sa90.png)
# Portfolio de actividades guiadas

###### Francisco Manuel Olmedo Cortés



<br>
<br>

Nota: Todos los códigos que aparecen aquí se encuentra en el siguiente repositorio: 

[Optimization-Algorithms](https://github.com/FullFran/Optimization-Algorithms/tree/main)

---

# TEMA 1: Introducción a los problemas de optimización

## ***Resumen y objetivos:***


En esta actividad vamos a resolver el problema del viajante (TSP) con un método exacto y uno aproximado, comparándolos entre sí. En concreto:

- Fijando el número de ciudades N y sus posiciones (generadas aleatoriamente), analizaremos todos los caminos posibles que empiezan y acaban en la misma ciudad (permutaciones), buscando aquel de mínimo recorrido. Este será nuestro **método exacto**.
- Con las mismas ciudades, buscaremos una solución aproximada, partiendo de una ciudad y saltando siempre a la más cercana para cada una de ellas. Este es el **método del vecino más cercano**.
- Finalmente representaremos las posiciones de las ciudades y los caminos seguidos en el plano.
- Calculamos el tiempo invertido en calcular la solución con cada método y representaremos esto en función de N.

## Resultados:

- Comparación de resultados obtenidos:


![](images/Pasted%20image%2020231211170401.png)


![](images/Pasted%20image%2020231211171805.png)



En estas imágenes podemos ver la diferencia entre el camino obtenido con el método aproximado y el exacto. Se puede observar qué, el resultado obtenido por el método aproximado no tiene por qué dar la solución óptima para el problema.


- Comparación de tiempos de ejecución en función del número de ciudades.


![](images/Pasted%20image%2020240127180621.png)


En la gráfica podemos ver la comparación del tiempo de ejecución en función el número de ciudades para el algoritmo exacto y el aproximado. Como podemos observar, el orden de complejidad del algoritmo aproximado es mucho menor que la del algoritmo exacto. Además podemos ver como el algoritmo aproximado escala de forma polinómica ($O(n^2$)) y el exacto escala peor ($O(n!)$).

## Discusión:

-   Observamos que para Ns muy pequeños, el algoritmo exacto es más
    rápido, pero este se vuelve extremadamente lento para Ns grandes,
    comparado con el otro.
-   El algoritmo exacto se vuelve inviable para N\>10. Sin embargo,
    podemos usar el método aproximado para Ns mucho más grandes.

## Anexo(s):

-   [tsp.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/1%20Introducción%20TSP/tsp.py) (Aquí están las funciones utilizadas para la implementación de la lógica del método exacto y el método aproximado).
- [resultados.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/1%20Introducción%20TSP/resultados.ipynb) (Aquí calculamos los tiempos de ejecución para el método exacto y el método del vecino más cercano, comparándolos. Además, graficamos la solución para el problema generando ciudades de forma aleatoria).

---

# Tema 2: Fundamentos físico-matemáticos de los algoritmos de optimización.

## Generadores de números aleatorios.

### Resumen y Objetivos:
En esta actividad vamos a implementar varios métodos para la generación de números aleatorios y compararlos entre ellos. En concreto:
- Implementar un **generador congruencial lineal** (GCL1 Y GCL2) y uno de **Fibonacci** (GCF). 
- Comparar histogramas entre los distintos generadores para  $10^6$ números, y la relación del siguiente número en función del anterior.
- Implementar métodos para generar números aleatorios distribuidos conforme a una distribución dada, por el **método de la transformada inversa** y el **método de aceptación rechazo**.

### Resultados:
Nota: En el archivo *ejercicios.ipynb* se encuentran resueltos los ejercicios planteados en las diapositivas.

- Histogramas de los números generados.
  
![](images/Pasted%20image%2020240123123656.png)

Podemos ver como el generador de Fibonacci genera números de forma más uniforme que el congruencial lineal, el cual con los primeros parámetros es el que tiene menor uniformidad. Por otro lado, el de **numpy** es muy uniforme.

- Relación del siguiente número generado con su anterior.

![](images/Pasted%20image%2020240127115142.png)

Podemos ver como el generador lineal congruencial con los primeros parámetros, abarca poco espacio por lo que es 'menos aleatorio' mientras que el de Fibonnaci, abarca más espacio y el de **numpy**, rellena casi todo.

- Método de la transformada inversa:

![](images/Pasted%20image%2020240123133011.png)

Podemos observar como los números se distribuyen de forma exponencial.

- Método de aceptación rechazo:

![](images/Pasted%20image%2020240123133047.png)

Podemos observar como los números se distribuyen según las distribuciones dadas.

### Discusión:
- Podemos observar como el generador de números aleatorios de **numpy** devuelve números aleatorios de una forma muy uniforme, por otro lado, el generador de Fibonacci es el que mejor se desempeña de los que hemos desarrollado. El generador lineal congruencial, los genera de forma menos uniforme y además es muy sensible a los parámentros utilizados.
- En la imagen donde hemos representado la relación del siguiente número con fu anterior, hemos ordenado de "mejor" a "peor" generador para ver como "cubren más huecos", es decir, en los mejores generadores desde cada número se puede acceder a más números.
- El método de la transformada inversa es sencillo y más eficiente, pero requiere poder operar de forma analítica la función, lo cual, puede no ser viable. El método de aceptación rechazo aunque, es menos eficiente (ya que tenemos que generar más números aleatorios para conseguir los que buscamos), se puede realizar con cualquier distribución.

### Anexo:
- [generadoresAleatorios.py](https://github.com/FullFran/Optimization-Algorithms/tree/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Generación%20de%20números%20Aleatorios/generadoresAleatorios.py) (Aquí se implementa la lógica de los generadores de números aleatorios).
- [ejercicios.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Generación%20de%20números%20Aleatorios/ejercicios.ipynb) (Aquí se realizan los ejercicios propuestos en la asignatura, comparando los distintos generadores de números aleatorios).

## Aguja de Buffon:

### Resumen y Objetivos:
En esta actividad realizaremos el experimento de la **aguja de Buffon**, comprobando el orden de convergencia de los **métodos de Montecarlo**. En concreto:
- Implementar un código para estimar el valor de $\pi$ empleando el método de la aguja de Buffon.
- Estudiar la convergencia, determinando que converge con un orden de $\frac{1}{\sqrt N}$.
- Comparar la convergencia para distintos tamaños de la aguja.
### Resultados:
- Estimación de $\pi$ con el método de Buffon. 

![](images/Pasted%20image%2020240127184645.png)

Podemos observar como a mayor número de iteraciones, el resultado oscila menos, convergiendo al valor de $\pi$ dado por **numpy** (línea naranja).

- Error en la convergencia en función del número de tiradas y la longitud de la aguja:

![](images/Pasted%20image%2020240123134450.png)

Se pude observar como al aumentar el tamaño de la aguja (d), el error disminuye, esto concuerda con lo visto teóricamente. Además se comprueba que el orden de convergencia se ajusta a $N^{-1/2}$.

- Se realizó un ajuste lineal del error representado en doble logarítmico para estimar el orden de convergencia ($co$). Para suavizar los resultados se realizó la media del orden de convergencia estimado para varias simulaciones obteniendo un resultado de: 
 $$co=-0.501\pm0.01$$   

- Al realizar el experimento tirando una aguja nueva en cada iteración manteniendo las anteriores, el orden de convergencia es distinto:

![](images/buffoncon.png)

- Realizando una regresión al igual que en el caso anterior obtenemos un resultado de:

$$co = -1.64\pm0.04$$

### Discusión:
- En la imagen de la convergencia del error, observamos como hay que "tirar del orden de 10000 agujas" para obtener una precisión de unos 2 decimales en la estimación de $\pi$. 
- Haciendo un ajuste, hemos demostrado que el error converge con $N^\frac{-1}{2}$, como vimos en la teoría para los métodos de Monte Carlo.
- También podemos ver como al aumentar el tamaño de la aguja, se reduce el error como vimos en la teoría.
- Un resultado curioso que obtuvimos sucedió al realizar el experimento generando una aguja nueva en vez de n agujas nuevas en cada iteración, aprovechando las generadas anteriormente para agilizar la simulación. El orden de convergencia nos salía distinto de lo esperado como se aprecia en la imagen. Es incluso posible que se trate de un error en la implementación de la simulación, pero decidí dejarlo porque me resulta curioso. Se encuentra al final del notebook. 
## Anexo:
- [buffon_needle.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Aguja%20de%20Buffon/buffon_needle.py)  (Aquí implementamos la lógica para la simulación del problema).
- [buffon_needle.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Aguja%20de%20Buffon/buffon_needle.ipynb) (Aquí ejecutamos el código, calculamos los tiempos de ejecución y hacemos el ajuste).

---
# Tema 3: Algoritmos para la optimización en espacios de alta dimensionalidad.

## Resumen y Objetivos:
En esta actividad resolveremos el TSP mediante 
**simulated annealing** y un **algoritmo genético**. En concreto:
- Implementaremos los métodos de simulated annealing y algoritmo genético para resolver el TSP.
- Resolveremos el TSP para distintos números de ciudades con ambos métodos, mostrando la evolución de la distancia de la ruta.

## Resultados:

- Resultados obtenidos por el simulated annealing con 30 ciudades:

![](images/sa30.png)

Resultado obtenido para 30 ciudades en 2.4s.

- Resultados obtenidos por el simulated annealing con 90 ciudades:

![](images/sa90.png)

Resultado obtenido para 90 ciudades en 3.5s.


- Resultados obtenidos por el algoritmo genético con 30 ciudades:

![](images/ga30.png)

Resultado obtenido para 30 ciudades en 10.2s.

- Resultados obtenidos por el algoritmo genético con 90 ciudades:

![](images/ga90.png)

Resultado obtenido para 90 ciudades en 31.6s.



## Discusión:
- En las gráficas podemos observar como tanto el simulated annealing como el algoritmo genético se desempeñan bien a la hora de resolver el TSP reduciendo la distancia recorrida con el tiempo hasta aproximarse a la solución exacta.
- En las gráficas del simulated annealing, podemos observar como en las primeras iteraciones, encontrándose a mayores temperaturas, la distancia recorrida no se reduce a penas. El algoritmo explora más estados, hasta que se alcanza una temperatura crítica (igual que en el [modelo de Issing](https://github.com/FullFran/Optimization-Algorithms/tree/main/2%20Números%20aleatorios%2C%20Métodos%20de%20Montecarlo/Trabajo%20Issing/Code)) a la cual el sistema empieza a 'congelarse' y converge a soluciones con menor distancia recorrida. Esto es debido a que al bajar la temperatura, la probabilidad de aceptar peores soluciones disminuye.
- En el algoritmo genético, podemos observar como en cada generación la distancia de la ruta del mejor individuo siempre se reduce o se mantiene. Esto es debido a que hemos contemplado **Elitismo**, haciendo que los mejores individuos pasen directamente a la siguiente generación. Además podemos ver como la distribución del fitness evoluciona, habiendo cada vez más individuos con un fitness mayor. (ver usando el método **graficRun** de la clase **GeneticAlgorithm**).

## Anexo:
- [simAnnealing.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/simAnnealing.py) (Aquí se implementa la lógica del simulated annealing para resolver el TSP).
- [simAnnealing.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/simAnnealing.ipynb) (Aquí están los resultados obtenidos con el simulated annealing).
- [genetic.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/genetic.py) (Aquí se implementa la lógica del algoritmo genético para resolver el TSP).
- [genetic.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/3%20Algoritmos%20para%20la%20optimización%20en%20espacios%20de%20alta%20dimensionalidad/genetic.ipynb) (Aquí están los resultados obtenidos con el algoritmo genético).

---

# Tema 4: Clasificación de eventos y detección de fallos.

## Resumen y Objetivos:
En esta actividad vamos a implementar una **red neuronal artificial de Hopfield**. En concreto vamos a:
- Entrenar la red con distintos patrones.
- Ver la evolución de la energía en la dinámica de la red.
- Recuperar las imágenes con las que ha sido entrenada la red, pudiendo observar la memoria asociativa.
- Estudiar el límite de almacenamiento, entrenando redes de distintos tamaños con distintos patrones aleatorios e intentar recuperar un patrón a partir de si mismo con un error aleatorio introducido.


## Resultados:

- Patrones con los que se ha entrenado a la red con sus correspondientes energías.

![](images/entrenamientoHopfield.png)


- Reconstrucción de una imagen usando la red de Hopfield entrenada en los 4 patrones anteriores. Reconstruida a partir de la imagen con ruido. 

![](images/recoHopfield.png)

Se muestra la evolución de la energía, en negativo para poder representar en doble logarítmico para apreciar mejor la evolución, (aunque veamos que aumenta el número en la gráfica, la energía se minimiza), por lo que se está minimizando la energía de la red. Este resultado era de esperar ya que el modelo de Hopfield implementado, es una variación del **algoritmo de Metrópolis** con T=0.

- Reconstrucción de imagen de un gato (previamente almacenada en la red) a partir de una imagen de uno distinto. Poniendo de manifiesto la memoria asociativa al reconstruir un patrón a partir de otro con características similares.

![](images/animecat.png)

- **Atractor espúreo**, aparentemente combinación de patrones. Obtenido añadiendo como input una imagen distinta a con las que se entrenó la red.

![](images/epureo.png)

- Error relativo al tamaño de la red (I) en función del número de patrones (N) entre el tamaño de la red. Podemos ver como se obtiene el resultado visto en teoría para el límite de almacenamiento. (La banda de color representa la dispersión de los resultados).

![](images/capacidadHopfield.png)

Podemos observar como el límite de almacenamiento de patrones en la red de Hopfield concuerda con lo visto en teoría ya que, a partir de ahí, comienza a 'añadir errores' al patrón cuando lo dejamos evolucionar.
Al representar los distintos tamaños, podemos observar como la pendiente de los errores relativos tras el cambio de comportamiento parece crecer con el tamaño de la red.


## Discusión:
- Podemos ver como el modelo de Hopfield evoluciona hacia mínimos de energía en la red. Esto, como hemos dicho, es debido a que sigue la misma lógica que el algoritmo de Metropolis a temperatura 0. Durante el entrenamiento, definir la matriz de pesos es definir la energía de nuestro sistema de forma que tenga mínimos en los patrones con los cuales hemos entrenado la red. Así, esta evolucionará hacia esos patrones.
- Hemos visto la capacidad del modelo para 'recordar' patrones a partir de otros que comparten características como hemos visto con el patrón con ruido introducido o el nuevo gato que no "conocía" la red. Además también recupera patrones a partir de "trozos" de los mismos. Pudiendo ver la capacidad de memoria asociativa del modelo.
- También hemos visto uno de los problemas de este modelo, que es la aparición de estados estables distintos de los patrones con los que entrenamos a la red, como es el caso de los atractores espúreos como el mostrado en la imagen.
- Por último, hemos realizado una simulación para comprobar el límite de almacenamiento de patrones del modelo. Realizando varias veces el proceso de entrenar con n patrones aleatorios y recordar uno de ellos añadiendole un error. Con esta simulación hemos visto como este se encuentra sobre el $N=0.14I$ como vimos en teoría.

## Anexo:
- [hopfield.py](https://github.com/FullFran/Optimization-Algorithms/blob/main/4%20Clasificaci%C3%B3n%20de%20eventos%20y%20detecci%C3%B3n%20de%20fallos/hopfiled.py) (Aquí se implementa la lógica del modelo de Hopfield).
- [hopfield.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/4%20Clasificaci%C3%B3n%20de%20eventos%20y%20detecci%C3%B3n%20de%20fallos/hopfield.ipynb) (Aquí se entrena la red de Hopfield con distintos patrones y se observa como recupera el patrón original a partir de un patrón con ruido).
- [capacidad_red.ipynb](https://github.com/FullFran/Optimization-Algorithms/blob/main/4%20Clasificaci%C3%B3n%20de%20eventos%20y%20detecci%C3%B3n%20de%20fallos/capacidad_red.ipynb) (Aquí se estudia la capacidad de la red para almacenar patrones en función del tamaño de la red).
