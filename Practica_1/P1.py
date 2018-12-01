import matplotlib.pyplot as plt
import numpy as np 
from pandas.io.parsers import read_csv



def regresionLineal(a, datos, t0, t1):

    #Variables del resultado temporal de t0 y t1
    temp0 = 0
    temp1 = 0

    #Número de vueltas que realiza el bucle
    vueltas = 0

    #Distancia mínima que tiene que haber entre el coste de función actual y anterior
    #para considerar que el bucle ha terminado
    precision = 0.0001
    
    #Funciones matemáticas propias del algoritmo
    h0 = lambda x : t0 + t1*x    
    h1 = lambda x : temp0 + temp1*x
    fun = lambda x : 1/(2*x.size) * sum((h0(x[:,0]) - x[:,1])**2)
    JT = lambda x : 1/(2*x.size) * sum((h1(x[:,0]) - x[:,1])**2)
    
    #Realizamos un primer descenso de gradiente
    temp0, temp1 = descensoGradiente(a, datos, h0, h1, t0, t1)
    
    #Comparamos la diferencia entre el coste anterior y el actual
    while abs(fun(datos) - JT(datos)) > precision: 
        t0 = temp0
        t1 = temp1

        temp0, temp1 = descensoGradiente(a, datos, h0, h1, t0, t1)
        vueltas += 1
       
    #Imprimimos por pantalla los resultados
    print("T0: " + str(t0))
    print("T1: " + str(t1))
    print("Vueltas: " + str(vueltas))    
        
    #Realiza la gráfica correspondiente pasándole como argumento los datos y la hipótesis
    graficarDatos(datos, h0, fun)


    p = np.ones( [len(datos[:, 0]) , 1], int)
    p2 = datos[:, 0].reshape(len(datos[:, 0]), 1)
  
    print(np.hstack([p, p2]))


    return



def descensoGradiente(a, datos, h0, h1, t0, t1):
    tmp0 = t0 - a/datos.size * np.sum(h0(datos[:,0]) - datos[:,1])
    tmp1 = t1 - a/datos.size * np.sum((h0(datos[:,0]) - datos[:,1]) * datos[:,0])

    return (tmp0, tmp1)



def graficarDatos(datos, h0, fun):

    #Establece unos maximos y minimos para los ejes
    ax = plt.gca()
    ax.axis([datos[:,0].min() - 1, datos[:,0].max() + 1, datos[:,1].min() - 1, datos[:,1].max() + 1])

    #Grafica la recta
    plt.plot([datos[:,0].min(), datos[:,0].max()], [h0(datos[:,0].min()), h0(datos[:,0].max())], '-b')
    '''Logica del plot:
    -El primer array indica lo que debe ocupar el eje X, es decir, del minimo de X (en datos) hasta el maximo
    -El segundo array indica la pendiente de la recta, o dicho de otra forma, donde empieza y acaba la recta
    en el eje Y
    Para hallar esto nos serviremos de la función hip, que es la que nos da la ecuación de la recta. 
    Le pasamos como argumento los theta obtenidos y el maximo y minimo X que se puede obtener de los datos y
    creamos un array con esos datos'''

    #Grafica los datos
    plt.plot(datos[:,0], datos[:,1], 'rx')
    plt.xlabel('Población de la ciudad')
    plt.ylabel('Ingresos en $')

    plt.show()

    return
    


def lee_csv(file_name):
    valores = read_csv(file_name, header=None).values

    return valores.astype(float)



#---------------------------------------------------------------------------#
#-------------------------- LLAMADA A LA FUNCIÓN ---------------------------#
#---------------------------------------------------------------------------#


#Constantes
theta0 = 0
theta1 = 0
alfa = 0.01


#Obtenemos los datos del fichero indicado por parametro
datos = lee_csv("ex1data1.csv")

#Calculamos el resultado
regresionLineal(alfa, datos, theta0, theta1)