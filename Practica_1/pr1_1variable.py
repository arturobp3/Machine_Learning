#FALTA HACER LO DE LAS OTRAS GRAFICAS RARAS


import matplotlib.pyplot as plt 
import numpy as np 
from pandas.io.parsers import read_csv
import time


def linearRegresion(theta0, theta1):

    tic = time.process_time()

    #Establece unos maximos y minimos para los ejes
    ax = plt.gca()
    ax.axis([datosX.min() - 1, datosX.max() + 1, datosY.min() - 1, datosY.max() + 1])
    # argumentos axis([minX, maxX, minY, maxY])
    # +1 y -1 para que haya unos margenes


    #DDDDDDDUUUUUUUUUDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    #No se que hacer con el coste que devuelve J
    #Creo que habría que tener algun tipo de condicion en el for que mida cuanto ha sido el cambio
    #del coste, para que cuando apenas cambie y se haya encontrado el minimo deje de iterar
    coste = J(theta0, theta1)

    for i in range(0, 1500): 

        theta0, theta1 = gradientDescent(theta0, theta1)

        coste = J(theta0, theta1)


    print(theta0, theta1)

    #Grafica la recta
    plt.plot([datosX.min(), datosX.max()], [hip(datosX.min(), theta0, theta1), hip(datosX.max(), theta0, theta1)], '-b')
    '''Logica del plot:
    -El primer array indica lo que debe ocupar el eje X, es decir, del minimo de X (en datos) hasta el maximo
    -El segundo array indica la pendiente de la recta, o dicho de otra forma, donde empieza y acaba la recta
    en el eje Y
    Para hallar esto nos serviremos de la función hip, que es la que nos da la ecuación de la recta. 
    Le pasamos como argumento los theta obtenidos y el maximo y minimo X que se puede obtener de los datos y
    creamos un array con esos datos'''


    #Graficamos los datos
    plt.plot(datosX, datosY, 'rx')
    plt.xlabel('Población de la ciudad')
    plt.ylabel('Ingresos en $')
    plt.show()


    toc = time.process_time()

    print(toc - tic)

    return


#Función del descenso de gradiente que permite minimizar el coste J
def gradientDescent(theta0, theta1):

    #Calcula el sumatorio de theta0
    sumTmp = 0
    for i in range(0, len(datos)):
        sumTmp += ( hip( datosX[i], theta0, theta1 ) - datosY[i] )

    tmp0 = (-alfa) * (1 / len(datos)) * sumTmp

    #Calcula el sumatorio de theta1
    sumTmp = 0
    for i in range(0, len(datos)):
        sumTmp += ( ( hip (datosX[i], theta0, theta1 ) - datosY[i] ) * datosX[i] )

    tmp1 = (-alfa)*(1 / len(datos)) * sumTmp



    #Asigna los nuevos theta
    theta0 = theta0 + tmp0
    theta1 = theta1 + tmp1

    return (theta0, theta1)


#Función de coste
def J(theta0, theta1):

    suma = 0
    division = 1 / (2*len(datos))

    for i in range(0, len(datos)):
        suma += (( hip( datosX[i], theta0, theta1 ) - datosY[i] ) **2 )


    return division * suma 



#Función de la hipótesis
def hip(x, theta0, theta1):
    return theta0 + (theta1 * x)



#Función que permite leer el archivo csv
def lee_csv(file_name):
    valores = read_csv(file_name, header=None).values

    return valores.astype(float)



#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

#Lee el archivo csv
datos = lee_csv("ex1data1.csv")

#Conseguimos dos arrays. Cada uno contiene los elementos x e y respectivamente
datosX = np.array([datos[i][0] for i in range(0, len(datos))])
datosY = np.array([datos[i][1] for i in range(0, len(datos))])

#Constantes
alfa = 0.01
theta0 = 0
theta1 = 0


linearRegresion(theta0, theta1)
