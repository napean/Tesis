# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pylab
import matplotlib.pyplot as plt
import numpy
import glob
import sys


numero ="96614"

datos= open ("Datos/lmc_sc14/phot/I/"+numero+".dat").read()


datoos= open ("Datos/lmc_sc14/lmc_sc14.tab").read()

array = datos.split('\n')
datos1 =  array[0].split(' ') 
t0 =  datos1[2]
infosc1 = datoos.split('\n')
periodo = 0

for i in range(len(infosc1)):
 cosos = infosc1[i].split(' ')
 if len(cosos) > 1:     
  
         if cosos[0] == numero:
                    if cosos[3] == '':
                        periodo = float(cosos[4])
                    else: 
                        periodo = float(cosos[3])    


# <codecell>


array = datos.split('\n')
datos1 =  array[0].split(' ')
t0 =  datos1[2]
    
hora=[]
magnitud=[]
error = []
fase = []
fasem = []

for i in range(len(array)):

 coso = array[i].split(' ')
 if len(coso) > 1:
         hora.append(coso[2])
         magnitud.append(coso[5])
         #fase1 = ((float(coso[2])-float(t0))/periodo) - int(((float(coso[2])-float(t0))/periodo ))
         #fase.append(fase1)
	 #fasem.append(fase1+1)
	 
#for i in range(len(fase)):
	#fase.append(fasem[i])


magnitudf = magnitud + magnitud


# <ahora calculemos el abby>

n = len(magnitud)

print n

prom = 0
suma = 0
for i in range(len(magnitud)):
	suma = suma + float(magnitud[i])
prom = suma/ len(magnitud)


print prom

sumarri = 0
sumab = 0

for i in range(len(magnitud)-1):
	sumarri = sumarri +  (float(magnitud[i+1]) + float(magnitud[i]))**2

for i in range(len(magnitud)):
	sumab= sumab +  (float(magnitud[i]) - prom)**2

print sumarri
print sumab

abbe = (len(magnitud)/(2*(len(magnitud) - 1 ))) * (sumarri/sumab)

print abbe
# <codecell>


# <codecell>



# <codecell>



# <codecell>


