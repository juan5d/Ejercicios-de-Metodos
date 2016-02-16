
# coding: utf-8

# In[15]:

#metodo aproximado vs metodo analitico
#graficas 
from math import *
import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt
print "{0:3s} |{1:10s} | {2:10s}".format("Tiempo", "Solución analitica","Solución aproximada")
m= 68.1     #Constante masa
c= 12.5    # Constante coeficiente friccion
g= 9.8     # Constante gravedad
vel_ant= 0.0
t_ant= 0
sol_aprox=0
valores_analitica= []  #lista vacia, guarda los valores del calculo analitico
valores_aprox= []  #lista vacia, guarda los valores del calculo aproximado
sol_analitica= 0   # Valor verdadero
sol_aprox= 0      # Valor aproximado


for t in range (50):
    analitica=((g*m)/c) * (1-exp(-(c/m)*t)) 
    vel_act= vel_ant + (g-(c/m)*vel_ant) * (t - t_ant)
    vel_ant= vel_act
    t_ant= t
    valores_analitica.append(analitica)     #Agrega valores analiticos a la lista valores analitica
    valores_aprox.append(vel_act)       #Agrega valores aproximados a la lista valores_aprox



    print "{0:3d}    |{1:10f}         | {2:10f} ".format(t, analitica,vel_act)


sol_analitica,= plt.plot(valores_analitica,"b-", label="Sol. Analitica")
sol_aprox,= plt.plot(valores_aprox,"r-", label= "Sol. Aproximada")
plt.legend(handles=[sol_analitica, sol_aprox], loc= 4)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)
plt.show()


# In[ ]:




# In[ ]:



