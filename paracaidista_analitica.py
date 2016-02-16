
# coding: utf-8

# In[20]:

from math import *
import matplotlib
print "{0:3s} | {1:10s}".format("Tiempo", "Solucion analitica")
m= 68.1     #Constante masa
c= 12.5    # Constante coeficiente friccion
g= 9.8     # Constante gravedad

def analitica(t):
    return ((g*m)/c) * (1-exp(-(c/m)*t)) 

for i in range (50):
    print "{0:3d}    | {1:10f}".format(i, analitica(i))


# In[ ]:



