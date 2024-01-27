import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import PIL.Image as Image # librería para cargar imágenes
import matplotlib.image as img # librería para representar imágenes y otras funciones básicas con estas

# Lee una imagen y la convierte a un patrón binario de dimensiones Lx * Ly: 
# La función devuelve el resultado como un único vector de +-1s de dimensiones I= Lx * Ly
def readPattern(fname, size):  # argumentos de la función: fname = "nombre_del_archivo", size=[Lx, Ly]
	this_img = Image.open(fname) # abre la imagen a color
	this_img = this_img.convert('1') # la convierte a blanco y negro binaria
	this_img = this_img.resize(size=[size[0],size[1]]) # re-escala la imagen para que tenga dimensiones [Lx, Ly]

	posicion_punto = fname.find(".") # busca en el nombre del archivo qué posición ocupa la extensión, para insertar ahí "_simple.png"
	fname2 = fname[:posicion_punto]+"_simple.png" # la imagen simplificada es png para evitar la compresión de datos (y cambiar así los colores)
	this_img.save(fname2) # almacena la imagen convertida

	# representa la imagen original y la imagen convertida
	fig = plt.figure()

	# subplot a la izquierda: imagen original
	fig.add_subplot(1,2,1)		
	original = img.imread(fname)
	plt.imshow(original)
	plt.title("original")
	plt.axis('off')

	# subplot a la derecha: imagen convertida
	matrix = img.imread(fname2) # lee la imagen convertida y la convierte a una matriz de 0s y 1s
	matrix = 2*matrix-1 # convierte los valores  [0,1] -> [-1,1]
	fig.add_subplot(1,2,2)		
	plt.matshow(matrix, cmap=plt.cm.gray,fignum=0)
	plt.axis('off')
	plt.title("simplificada")
	plt.show()
	
	# Devuelve la imagen como un vector 1D (no como una matriz)
	return matrix.flatten()
	
#####################################################################################

# APRENDIZAJE: define una función para calcular los PESOS de la red en base a una lista de patrones que se desea almacenar y la regla de Hebb
# La función devuelve una matriz de pesos w_ij
def calcula_w(patterns):
	M = len(patterns)

	w = np.zeros([I,I]) # weights

	for k in range(M):
		print("pattern ", k)
		# this is not efficient, but we could use it anyway:
	#		for i in range(self.I):
	#			for j in range(self.I):
	#				w[i,j] += patterns[k][i]*patterns[k][j]/(1.*self.M)

		# it is more efficient to use built-in functions:
		w += np.outer(patterns[k],patterns[k])/(1.*M)



	return w

# DINÁMICA: evoluciona la red un determindo número de steps
# la función devuelve el estado de la red tras ese número de pasos, s_new
def evoluciona_red(s, w, h, steps):

	for k in range(steps):
		i = np.random.randint(I) # elije un nodo aleatorio
		
		sum_wijsj = np.sum(w[i,:]*s) # calcula el argumento de la función activación
		if sum_wijsj < h[i]: # por debajo del umbral
			s[i] = -1
		else: # por encima del umbral
			s[i] = 1

	return s

#######################################################################

Lx = Ly = 75 # dimensiones de las imágenes (simplificadas)
I = Lx*Ly # número de neuronas



## PASO 1: LEE LAS IMÁGENES Y CONVIÉRTELA A PATRONES BINARIOS
# lista de imágnees que quiero almacenar en mi red neuronal
files = ["patterns/batman.png", "patterns/gato.jpg", "patterns/yo.jpg"]

print("Leyendo imágenes y conviertiéndolas a patrones binarios...")
patterns = [] # cada elementro de esta lista contendrá un patrón (vector) de +-1s.
for fname in files:
	patterns.append(readPattern(fname, size=[Lx,Ly]))


## PASO 2: CREA LA RED Y ALMACENA LOS PATRONES PREVIOS EN BASE A LA REGLA DE HEBB
h = np.zeros(I) # funciones umbral (usamos siempre h_i = 0)
w = calcula_w(patterns) # pesos


## PASO 3: ESTABLECE OTRO PATRÓN COMO CONDICIÓN INICIAL DEL ESTADO DE LA RED
s = readPattern("inputs/batman2.png", size=[Lx,Ly]) # lee la imagen input y conviértela a vector de +-1s.
# muéstralo
plt.matshow(np.resize(s,[Lx, Ly]), cmap=plt.cm.gray)
plt.title("Condición inicial")
#plt.axis('off') # elimina los ejes
plt.show()


## PASO 4: PROCEDE A LA DINÁMICA DE LA RED
#################### ANIMACION #################################
TOTAL_FRAMES = 1000000 # número de "frames" de la animación
DT_FRAMES = 100 # duración de cada frame (ms); si lo modificamos, hacemos más rápdia/lenta la animación


fig = plt.figure() # genera una figura vacía, que será sobre la que correrá la animación
fig_mat = plt.matshow(np.resize(s,(Lx,Ly)), cmap=plt.cm.gray, fignum=0) # etiquetando la figura con fignum (e.g. fignum=0), reusamos siempre la misma figura para ir sobreescribiendo los datos; el resultado de plt.matshow se almacena en fig_mat, para que podamos ir modificando los datos
plt.title("Pasos iterados: 0")
#plt.axis('off')



# definimos la función usada para producir la animación
def actualiza_animacion(i): 
	evoluciona_red(s, w, h, steps=i*I//10)
	fig_mat.set_data(np.resize(s,(Lx,Ly)))
	plt.title("Pasos iterados: %d"%(i*I//10))
	return fig_mat
	
# genera la animación
ani = animation.FuncAnimation(fig, actualiza_animacion, frames=TOTAL_FRAMES, interval=DT_FRAMES, repeat=False) 
plt.show()











