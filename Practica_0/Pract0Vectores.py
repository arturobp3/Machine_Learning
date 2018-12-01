#PONER COMO EN EL ITERATIVO EL MAIN Y DEMÁS



import matplotlib.pyplot as plt 
import numpy as np
import time
from scipy import integrate


def integra_mc(fun, a, b, num_puntos=10000):
    #Tiempo inicial
    tic = time.process_time()
    
    #Calcula el maximo de la funcion
    max = valorMax(fun, a, b)

    #Array de puntos aleatorios
    pX = np.random.uniform(a, b, (1, num_puntos))
    pY = np.random.uniform(0, max, (1, num_puntos))

    #Obtenemos las imagenes de cada elemento de pX
    imagen_pX = fun(pX)

    #Obtenemos que elementos son mayores y cuales no
    resultResta = imagen_pX > pY

    #Obtenemos el número de elementos True de resultResta
    nDebajo = len(resultResta[resultResta == True])

    #Dibuja los puntos creados aleatoriamente
    plt.plot(pX[0], pY[0], 'r.', label='Puntos aleatorios')


    #Establece la información de los ejes
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc=0) #El parámetro permite colocar la leyenda en la mejor posición posible.
    plt.show() #Muestra la grafica

     #Obtiene el tiempo final
    toc = time.process_time()
    
    return (((nDebajo / num_puntos) * ((b - a)*max)), toc-tic)



def valorMax(fun, a, b):   
    puntosX = np.arange(a, b, 0.01)
    puntosY = fun(puntosX)    

    max = puntosY.max()
    
    plt.plot(puntosX, puntosY, '-b', label='Grafica de f(x)')
    plt.fill_between(puntosX, puntosY, facecolor='blue', alpha=0.25)

    return max


#-------------------------------------------------------------------------
#----------------------- LLAMADA A LA FUNCION ----------------------------
#-------------------------------------------------------------------------

a = 0
b = np.math.pi
fun = lambda x: 2**x

resIntegral, valor = integrate.quad(fun, a, b)

print("\nEl resultado obtenido mediante 'integrate.quad' es: " + str(resIntegral))

#Llamada a integra con el segmento deseado
result, tiempo = integra_mc(fun, a, b, 1000)
print("El resultado de la funcion es: " + str(result))

#Muestra el tiempo de ejecucion
print("Tiempo de ejecucion: " + str((tiempo)) + "\n")

