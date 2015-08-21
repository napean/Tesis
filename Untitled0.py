 
import glob
from subprocess import call
 
 
# <codecell>
 
fileset = glob.glob('Datos/lmc_sc1/phot/I/*.dat')
for nfile in fileset:
   
  call(["python", "Graficas1.py", nfile])
   
