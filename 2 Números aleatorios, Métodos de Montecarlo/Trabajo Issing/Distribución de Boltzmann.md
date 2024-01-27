# Queremos simular la distribución de Boltzmann con el metropolis.
Partimos de un sistema a una temperatura T con una energía, con N partículas. La energía es la suma de la energía de todas las partículas por separado. 

A una determinada energía, hay un número de microestados posible (formas de tener esa energía).

Boltzman postuló que la entropía es $$k_{b}ln(\Omega)$$ Así la entropía depende del número de configuraciones del estado.

Otro postulado: Mirando N,T,u y las energías de cada partícula. La configuración más probable es la que tiene entropía máxima. (microestado y macro estado como ya sabemos)...

Tenemos que buscar el estado que maximiza la entropía y minimiza la energía.

$$ 
U = \sum_{i}n_{i}E_{i}
$$
De forma que el número de partículas sea el número de partículas total (la suma de las partículas en cada estado sea el número total de partículas)

$$
N = \sum_{i}n_{i}
$$
(Función objetivo: la energía, ligadura: Número de partículas, por ahora).

Ahora, para nuestro cuerpo negro tenemos que usar como energía de una partícula el Hamiltoniano del oscilador armónico cuántico. si usamos el oscilador armónico clásico -> catástrofe del ultravioleta.

## Nacimiento de la mecánica cuántica!!! Solución a la catástrofe del ultravioleta.

$$
E = \frac{1}{2M}P^{2} +\frac{1}{2}m\omega^{2}x^{2}
$$

si dividimos entre E... Nos queda el área de un elipse. El área de la elipse es proporcional a la energía, nos queda que la energía es proporcional a omega. 

Para que cuadre, podemos decir que en este oscilador siempre tiene que estar en movimiento (independientemente de la temperatura), lo que lleva a que exista una elipse mínima. El área de esta elipse valdrá la constante de plank así sacamos el: 
$$
E_{n} = n\hbar \omega
$$
Esta como sabemos es aproximadamente la solución del oscilador armónico cuántico, y tiene sentido con la teoría desarrollada posteriormente a Plank, solo falta que es $$n+\frac{1}{2}$$
Lo potente de esto es que estamos cuantizando la energía!!!!


## Función de distribución de Plank.

Ligaduras de que se anule el E_t y B_n en las paredes de la cavidad de lado L.
