import numpy as np
from matplotlib import pyplot as plt 
import math 

def margen(vol,mc,cost_pam,OCF,ton_pam):
    mg=vol*mc-math.ceil(vol/ton_pam)*cost_pam-OCF
    return mg

mc=80
cost_pam=200
OCF=1000
ton_pam=7



vol=np.array(range(50))
mg=np.zeros(len(vol))

for i in range(len(mg)):
    mg[i]=margen(vol[i],mc,cost_pam,OCF,ton_pam)

plt.plot(vol,mg)
plt.show()
