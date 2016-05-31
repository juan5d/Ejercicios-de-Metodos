import numpy as npy
import matplotlib.pyplot as pl


datos = [8.8,9.4,10,9.8,10.1,
         9.5,10.1,10.4,9.5,9.5,
         9.8,9.2,7.9,8.9,9.6,
         9.4,11.3,10.4,8.8,10.2,
         10,9.4,9.8,10.6,8.9]

rango = npy.arange(7.5, 11.5 + 0.5, 0.5)       
pl.figure("Histograma Ejercicio 17,2")
pl.hist(datos,rango, facecolor='r', alpha=0.8)
pl.title("Histograma Datos", fontweight="bold")
pl.xlabel("Rango (7.5 - 11.5)",fontweight="bold")
pl.ylabel("Frecuencia Acumulada",fontweight="bold")
pl.margins(y=.01,x=.01)
pl.subplots_adjust(left=0.15)
pl.grid(True)
pl.show()



