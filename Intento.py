# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import glob
from subprocess import call
import pylab
import matplotlib.pyplot as plt
import numpy
import glob
import sys

# <codecell>

coso7=sys.argv[1]

# <codecell>

def calculabbe(entrada):


    argumen = entrada.split('/')
    
    nd = argumen[4].split('.')
    numero = nd[0]
    
    datos= open ("Datos/lmc_sc"+str(coso7)+"/phot/I/"+numero+".dat").read()
    

    datoos= open ("Datos/lmc_sc"+str(coso7)+"/lmc_sc"+str(coso7)+".tab").read()
    
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
             fase1 = ((float(coso[2])-float(t0))/periodo) - int(((float(coso[2])-float(t0))/periodo ))
             fase.append(fase1)
             fasem.append(fase1+1)
         
    for i in range(len(fase)):
        fase.append(fasem[i])
    
    
    magnitudf = magnitud + magnitud
    
    
    # <ahora calculemos el abby>
    
    n = len(magnitud)
    
    
    
    prom = 0
    suma = float(0)
    for i in range(len(magnitud)):
        suma = suma + float(magnitud[i])
    prom = suma/ len(magnitud)
    
    
    
    sumarri = []
    sumab = []
    abbe = 0
    
    algo = len(magnitud)
    
    for i in range(len(magnitud)-1):
        sumarri.append( ( float(magnitud[i+1]) -float(magnitud[i]) )**2)
    
    for i in range(len(magnitud)):
        sumab.append( (float(magnitud[i]) - prom)**2 )
    
    
    algomas = float((2*(algo-1)))
    
    coso5 = float(algo/algomas)
    
    aba = sum(sumab)
    arri = sum(sumarri)
    
    abbe=float((arri)/(aba))
    realabbe = coso5*abbe
    
    return realabbe
        

# <codecell>

# <codecell>



abbee=[]

fileset = glob.glob('Datos/lmc_sc'+str(coso7)+'/phot/I/*.dat')
for nfile in fileset:
  
  abbee.append(calculabbe(nfile))
  



# <codecell>

# <codecell>

plt.hist(abbee)
plt.savefig(str(coso7)+".png")

# <codecell>


