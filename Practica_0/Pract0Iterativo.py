import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import integrate 

#Versión iterativa

def integra_mc(fun, a, b, num_puntos=10000):
    #Tiempo inicial
    tic = time.process_time()
    
    #Array de puntos aleatorios
    pX = []
    pY = []
    
    #Calcula el maximo de la funcion
    max = valorMax(fun, a, b)

    nDebajo = 0
    for i in range(0, num_puntos):
        x = np.random.uniform(a, b)   
        y = np.random.uniform(0, max) 

        pX.append(x)
        pY.append(y)

        if fun(x) > y: nDebajo += 1

    #Dibuja los puntos creados aleatoriamente
    pX = np.array(pX)
    pY = np.array(pY)
    plt.plot(pX, pY, 'r.', label='Puntos aleatorios')

    #Establece la información de los ejes
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc=0) #El parámetro permite colocar la leyenda en la mejor posición posible.
    plt.show() #Muestra la grafica

    #Obtiene el tiempo final
    toc = time.process_time()

    return (((nDebajo / num_puntos) * ((b - a)*max)), toc-tic)



def valorMax(fun, a, b):
    puntosX = []
    puntosY = []

    max = -1

    for i in np.arange(a, b, 0.01):
        if(fun(i) > max):
            max = fun(i)

        puntosX.append(i)
        puntosY.append(fun(i))   
        

    puntosX = np.array(puntosX)
    puntosY = np.array(puntosY)

    plt.plot(puntosX, puntosY, '-b', label='Grafica de f(x)')
    plt.fill_between(puntosX, puntosY, facecolor='blue', alpha=0.25)

    return max





#-------------------------------------------------------------------------
#----------------------- LLAMADA A LA FUNCION ----------------------------
#-------------------------------------------------------------------------

a = 0
b = np.math.pi
fun = lambda x: np.math.sin(x)

resIntegral, valor = integrate.quad(fun, a, b)

print("\nEl resultado obtenido mediante 'integrate.quad' es: " + str(resIntegral))

#Llamada a integra con el segmento deseado
result, tiempo = integra_mc(fun, a, b, 1000)
print("El resultado de la funcion es: " + str(result))

#Muestra el tiempo de ejecucion
print("Tiempo de ejecucion: " + str((tiempo)) + "\n")

