import matplotlib
matplotlib.use('Qt4Agg')  
import matplotlib.pyplot as pl
import numpy as npy
import math 

x = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
y = [5, 6, 7, 6, 9, 8, 7, 10, 12, 12]

consecutivo = npy.arange(1, 11)    
recta_xy = []    
recta_x = []        
recta_y = []        

class RegresionLineal():
    
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


a0_x = RegresionLineal().calc_a0(consecutivo, x)     
a1_x = RegresionLineal().calc_a1(consecutivo, x)       
error_x = RegresionLineal().error_std(consecutivo, x)   

a0_y = RegresionLineal().calc_a0(consecutivo, y)   
a1_y = RegresionLineal().calc_a1(consecutivo, y)        
error_y = RegresionLineal().error_std(consecutivo, y)    

a0_xy = RegresionLineal().calc_a0(x, y)   
a1_xy = RegresionLineal().calc_a1(x, y)   
error_xy = RegresionLineal().error_std(x, y)    

for xi, c in zip(x, consecutivo):
    recta_xy.append(a0_xy + a1_xy * xi)
    recta_x.append(a0_x + a1_x * c)
    recta_y.append(a0_y + a1_y * c)

print  "Ejercicio 17,4"

print "\nRegresión Para X: "
print "\t(Consecutivo) c= ", consecutivo
print "\tx= ", x
print "Coeficientes:"
print "\ta0= %.4f\ta1=  %.4f" % (a0_x, a1_x)
print "\t(Ecuación) y=  %.4f  +  (%.4f)  *  x" % (a0_x, a1_x)
print "\t(Coeficiente Correlación) r=  %.4f" % RegresionLineal().calc_r(consecutivo, x)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error_x
print "#", "-" * 80, "\n"

print "\nRegresión Para Y: "
print "\t(Consecutivo) c= ", consecutivo
print "\ty= ", y
print "Coeficientes:"
print "\ta0= %.4f\ta1=  %.4f" % (a0_y, a1_y)
print "\t(Ecuación) y=  %.4f  +  (%.4f) *  x" % (a0_y, a1_y)
print "\t(Coeficiente Correlación) r=  %.4f" % RegresionLineal().calc_r(consecutivo, y)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error_y
print "#", "-" * 80, "\n"


print "\nRegresión Para X vs Y: "
print "\tx= ", x
print "\ty= ", y
print "Coeficientes:"
print "\ta0= %.4f\ta1=  %.4f" % (a0_xy, a1_xy)
print "\t(Ecuación) y=  %.4f  +  (%.4f)  *  x" % (a0_xy, a1_xy)
print "\t(Coeficiente Correlación) r=  %.4f" % RegresionLineal().calc_r(x, y)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error_xy


pl.figure(u"Gráfica Regresión X")
pl.title(u"Regresión Lineal X", fontweight="bold")
pl.plot(consecutivo, x, "*", label= "Valores X")     
pl.plot(consecutivo, recta_x, label=u"Recta Regresión", lw=1.5)         
pl.xlabel("Consecutivo", fontweight="bold")
pl.ylabel("Valores X", fontweight="bold")
pl.legend(loc=4)
pl.margins(y=.1, x=.1)
pl.grid(True)
pl.show()

pl.figure(u"Gráfica Regresión Y")
pl.title(u"Regresión Lineal Y", fontweight="bold")
pl.plot(consecutivo, y, "*", label= "Valores Y")       
pl.plot(consecutivo, recta_y, label=u"Recta Regresión", lw=1.5)          
pl.xlabel("Consecutivo", fontweight="bold")
pl.ylabel("Valores Y", fontweight="bold")
pl.legend(loc=4)
pl.margins(y=.1, x=.1)
pl.grid(True)
pl.show()

pl.figure(u"Gráfica Regresión xy")
pl.title(u"Regresión Lineal x vs y", fontweight="bold")
pl.plot(x, y, "*", label= "y")        
pl.plot(x, recta_xy, label=u"Recta Regresión", lw=1.5)  
pl.xlabel("Valores x", fontweight="bold")
pl.ylabel("Valores y", fontweight="bold")
pl.legend(loc=4)
pl.margins(y=.1, x=.1)
pl.grid(True)
pl.show()

