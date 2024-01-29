

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
![[images/Pasted image 20231211170401.png]]
![[images/Pasted image 20231211171805.png]]

En estas imágenes podemos ver la diferencia entre el camino obtenido con el método aproximado y el exacto. Se puede observar como el resultado obtenido por el método aproximado no tiene por qué dar la solución óptima para el problema.


- Comparación de tiempos de ejecución en función del número de ciudades.
![[Pasted image 20240127180621.png]]

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

-   [tsp.py](Master Tecnologías físicas/optimización en sistemas físicos y aplicaciones industriales/Optimization Algorithms/1 Introducción TSP/tsp.py) (Aquí están las funciones utilizadas para la implementación de la lógica del método exacto y el método aproximado).
- [[resultados.ipynb]] (Aquí calculamos los tiempos de ejecución para el método exacto y el método del vecino más cercano y los comparamos, además graficamos la solución para el problema generando ciudades de forma aleatoria).

---
# Tema 2: Fundamentos físico-matemáticos de los algoritmos de optimización.

## Generadores de números aleatorios.

### Resumen y Objetivos:

### Resultados:
Nota: En el archivo ejercicios.ipynb se encuentran los ejercicios planteados en las diapositivas resueltos.

![[Pasted image 20240123123656.png]]
Histogramas de los números generados.

![[Pasted image 20240127115142.png]]
Relación del número generado con el anterior.

- Método de la transformada inversa:

![[Pasted image 20240123133011.png]]


- Método de aceptación rechazo:

![[Pasted image 20240123133047.png]]



### Discusión:
- Podemos observar como el generador de números aleatorios de numpy los genera de una forma muy uniforme, por otro lado, el generador de fibonacci es el que mejor se desempeña de los que hemos desarrollado, mientras tanto, el generador lineal congruencial, los genera de forma menos uniforme y además es muy sensible a los parámentros utilizados.
- En la imagen donde hemos representado la relación del siguiente número con el anterior, hemos ordenado de "mejor" a "peor" generador para ver como "cubren más huecos" es decir, en los mejores generadores desde cada número se puede acceder a más números.
- El método de la transformada inversa es sencillo y más eficiente, pero requiere poder operar de forma analítica la función, lo cual puede no ser viable mientras que el método de aceptación aunque es menos ineficiente (ya que tenemos que generar más números aleatorios para conseguir los que buscamos) se puede realizar con cualquier distribución.

### Anexo:

## Aguja de Buffon.

### Resumen y Objetivos:

### Resultados:
- Estimación de pi con el método de Buffon. 
![[Pasted image 20240127184645.png]]
- Error en la convergencia en función del número de tiradas y la longitud de la aguja:
![[Pasted image 20240123134450.png]]

### Discusión:
- En la imagen de la convergencia del error, vemos como hay que "tirar del orden de 10000 agujas" para obtener una precisión de unos 2-3 decimales en la estimación de $\pi$. 
- Haciendo un ajuste, hemos demostrado que el error converge con $N^\frac{-1}{2}$, como vimos en la teoría para los métodos de Monte Carlo. 
- También podemos ver como al aumentar el tamaño de la aguja, se reduce el error como vimos en la teoría.
## Anexo:
- [buffon_needle.py](Master Tecnologías físicas/optimización en sistemas físicos y aplicaciones industriales/Optimization Algorithms/2 Números aleatorios, Métodos de Montecarlo/Aguja de Buffon/buffon_needle.py)  (Aquí implementamos la lógica para la simulación del problema).
- [buffon_needle.ipynb](Master Tecnologías físicas/optimización en sistemas físicos y aplicaciones industriales/Optimization Algorithms/2 Números aleatorios, Métodos de Montecarlo/Aguja de Buffon/buffon_needle.ipynb) (Aquí ejecutamos el código, calculamos los tiempos de ejecución y hacemos el ajuste).

---
# Tema 3: Algoritmos para la optimización en espacios de alta dimensionalidad.

## Resumen y Objetivos:

## Resultados:

## Discusión:

## Anexo:

---

# Tema 4: Clasificación de eventos y detección de fallos.

## Resumen y Objetivos:

## Resultados:

## Discusión:

## Anexo: