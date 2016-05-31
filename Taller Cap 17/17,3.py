import matplotlib.pyplot as pl
import numpy as npy

datos = [28.65, 26.55, 26.65, 27.65, 27.35, 28.35, 26.85,
         28.65, 29.65, 27.85, 27.05, 28.25, 28.35, 26.75,
         27.65, 28.45, 28.65, 28.45, 31.65, 26.35, 27.75,
         29.25, 27.65, 28.65, 27.65, 28.55, 27.55, 27.25]

class RegLineal():
    
    def sumatoria(self,v_val):
        suma = 0     

        for i in v_val:     
            suma += i

        return suma      


    def sumatoria_cua(self, v_val):
        sum_cua = 0

        for i in v_val:
            sum_cua += i ** 2

        return sum_cua

    def sumatoria_xy(self, v_x, v_y):
        sum_xy = 0

        for xi, yi in zip(v_x, v_y):
            sum_xy += xi * yi

        return sum_xy


    def calc_media(self,v_val):
        return self.sumatoria(v_val) / float(len(v_val))   

    def varianza(self, v_val):
        med = self.calc_media(v_val)
        _sum = 0
        var = 0

        for i in v_val:
            _sum += (i - med) ** 2

        var = _sum / float(len(v_val) - 1)

        return var      

    def desv_std(self, v_val):
        desv = self.varianza(v_val)

        return math.sqrt(desv)

    def cv(self, v_val):
        med = self.calc_media(v_val)    
        sd = self.desv_std(v_val)   

        cv = (sd / med) * 100

        return cv

    def calc_a1(self,v_x, v_y):
        n = len(v_x)    # Tamanio
        sum_xy = self.sumatoria_xy(v_x, v_y)    
        sum_x = self.sumatoria(v_x)     
        sum_y = self.sumatoria(v_y)      
        sum_x_cua = self.sumatoria_cua(v_x)    

        a1 = ((n * sum_xy) - (sum_x * sum_y)) / float(((n * sum_x_cua) - (sum_x**2)))

        return a1

    def calc_a0(self,v_x, v_y):
        a1 = self.calc_a1(v_x, v_y)
        x_med = self.calc_media(v_x)
        y_med = self.calc_media(v_y)

        return float(y_med - a1 * x_med)

    def calc_r(self, v_x, v_y):
        n = len(v_x)
        sum_x = self.sumatoria(v_x)
        sum_y = self.sumatoria(v_y)
        sum_x_cua = self.sumatoria_cua(v_x)
        sum_y_cua = self.sumatoria_cua(v_y)
        sum_xy = self.sumatoria_xy(v_x, v_y)

        r = ((n * sum_xy) - (sum_x * sum_y)) / ((math.sqrt(n * sum_x_cua - (sum_x ** 2))) * (math.sqrt(n * sum_y_cua - (sum_y ** 2))))

        return r

    def error_std(self, v_x, v_y):
        a0 = self.calc_a0(v_x, v_y)    
        a1 = self.calc_a1(v_x, v_y)    
        sr = 0

        for xi, yi in zip(v_x, v_y):
            sr += (yi - a0 - a1 * xi) ** 2

        sr /= float(len(v_x) - 2)
        Syx = math.sqrt(sr)

        return Syx    


print "Ejercicio 17,3"
print "Datos:"
print "\t",datos
print "\nResultados:"
print "\tMedia=  ", RegLineal().calc_media(datos)
print "\tDesviacion Estandar=  ", RegLineal().desv_std(datos)
print "\tVarianza=  ", RegLineal().varianza(datos)
print "\tCoef. Variacion(%)=  ", RegLineal().cv(datos)


rango = npy.arange(26, 32 + 0.5, 0.5)       

pl.figure("Histograma Ej17,3")
pl.hist(datos,rango, facecolor='y', alpha=0.8)
pl.title("Histograma Datos", fontweight="bold")
pl.xlabel("Rango (26-32)",fontweight="bold")
pl.ylabel("Frecuencia Acumulada",fontweight="bold")
pl.margins(x=.01,y=.01)
pl.subplots_adjust(left=0.15)
pl.grid(True)
pl.show()



