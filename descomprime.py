# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import glob
from subprocess import call
call(["ls", "-l"])

# <codecell>

fileset = glob.glob('Datos/*.tar')
counter=0
for nfile in fileset:
  call(["tar", '-xvf',nfile])
  

# <codecell>


