import glob
from subprocess import call


# <codecell>

fileset = glob.glob('Datos/lmc_sc14/phot/I/*.dat')
for i in range(16):  
  call(["python", "Intento.py", str(i)])
  

# <codecell>

