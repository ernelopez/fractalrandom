import numpy as np
import random
import matplotlib.pyplot as plt

# función que calcula las n raíces complejas de la unidad
def nthRootsOfUnity1(n): 
    return np.exp(2j * np.pi / n * np.arange(n))

# valores iniciales
n = 5				# cantidad de lados
cant = 100000		# número de iteraciones

raices = nthRootsOfUnity1(n)
re = []
im = []

# sorteo inicial
re.append(random.uniform(-1,1))
im.append(random.uniform(-1,1))

for i in range(cant) :
	m = random.randint(0,n-1)										#el vértice sorteado
	re.append((raices[m].real + raices[(m+1)%n].real + re[i])/3)	#promedio parte real
	im.append((raices[m].imag + raices[(m+1)%n].imag + im[i])/3)	#promedio parte im

raices_re = [ele.real for ele in raices]
raices_im = [ele.imag for ele in raices]
plt.scatter(raices_re, raices_im, s=10)
plt.scatter(re, im, s=1)
plt.scatter(re[0], im[0], s=10)			#ploteo aparte el punto inicial
plt.ylabel('Im')
plt.xlabel('Re')
plt.show()