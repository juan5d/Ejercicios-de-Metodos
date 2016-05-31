import matplotlib
matplotlib.use('Qt4Agg')   
import matplotlib.pyplot as pl
import math


x = [6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]
y = [29, 21, 29, 14, 21, 15, 7, 7, 13, 0, 3]

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



recta = []    
a0 = RegresionLineal().calc_a0(x, y)   
a1 = RegresionLineal().calc_a1(x, y)   
r = RegresionLineal().calc_r(x, y)   
error = RegresionLineal().error_std(x, y)  

print "\nResultados: "
print "Coeficientes:"
print "\ta0=   %.4f\ta1=   % .4f" % (a0, a1)
print "\t(Coef. Correlación) r=  %.4f" % r
print "Ecuación Recta:"
print "\ty =   %.4f  +  (%.4f)  X" % (a0, a1)
print "Error Estándar Estimado: "
print "\tSyx =   %.4f" % error

for xi in x:
    temp = a0 + a1 * xi    
    recta.append(temp)

    
pl.figure(u"Gráfica ")
pl.title(u"Recta Regresión Lineal de X", fontweight="bold")
pl.plot(x, y, "*", label= "Valores X")      
pl.plot(x, recta, label=u"Recta Regresión", lw=1.5)      
pl.xlabel("Valores X", fontweight="bold")
pl.ylabel("Valores Y", fontweight="bold")
pl.legend(loc=1)
pl.margins(y=.1, x=.1)
pl.grid(True)
pl.show()


