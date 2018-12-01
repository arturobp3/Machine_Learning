import matplotlib.pyplot as plt
import numpy as np 
from pandas.io.parsers import read_csv
from numpy.linalg import inv


#Algoritmo de aprendizaje
def regresionLineal(alfa, x, y, theta, precision, opcion):

    #Vector de 1's
    p = np.ones( [len(x) , 1], int)

    #Matriz de x_norm con el 1 añadido en el elemento x0
    x = np.hstack([p, x])

    #Variables del resultado temporal de theta
    temp0 = np.zeros((x[0].size, 1))
 
    if(opcion == 0):
        theta = descensoGradiente(alfa, x, y, theta, temp0)
    else:
        theta = ecuacionNormal(x, y)
       

    return theta


#Predice un nuevo resultado
def nuevaPrediccion(dato0, dato1, opcion):

    #Función hipotesis
    h0 = lambda x : x.dot(theta)

    x_nuevo = np.array([[dato0, dato1]])

    if(opcion == 0):
        #Normalizamos los datos
        x_nuevo = (x_nuevo - mu) / sigma

    p = np.ones( [len(x_nuevo) , 1], int)
    x_nuevo = np.hstack([p, x_nuevo])


    return str(h0(x_nuevo)[0,0])


#Devuelve en un solo paso el valor óptimo para theta
def ecuacionNormal(x, y):
    return ( (inv((x.T).dot(x))).dot((x.T).dot(y)) )


def descensoGradiente(a, x, y, theta, temp0):

    #Funciones matemáticas 
    h0 = lambda x : x.dot(theta)  
    h1 = lambda x : x.dot(temp0)
    #Funciones de coste
    fun = lambda x : 1/(2*x.size) *  ( (h0(x) - y).T).dot( h0(x) - y ) 
    JT = lambda x : 1/(2*x.size) *  ( (h1(x) - y).T).dot( h1(x) - y ) 

    #Realizamos un primer descenso de gradiente
    temp0 = calculaDescenso(alfa, x, y, theta, h0)

    vueltas = 0

    #Comparamos la diferencia entre el coste anterior y el actual
    r = abs(fun(x) - JT(x))
    while (r.all() > precision): 
        theta = temp0
        temp0 = calculaDescenso(alfa, x, y, theta, h0)
        r = abs(fun(x) - JT(x))
       
        #plt.plot(vueltas, r, 'b.')

        vueltas += 1


    #Imprimimos por pantalla los resultados
    plt.xlabel("Nº de Iteraciones")
    plt.ylabel("J("+chr(952)+")")
    #plt.show()

    return theta



#Función que aplica el descenso de gradiente
def calculaDescenso(a, x, y, theta, h0):
    return (theta - a/(x.size) * ((h0(x) - y).T).dot(x).T)


#Función que normaliza los datos de entrenamiento y obtiene los vectores mu y sigma correspondientes
def normalizar(x):

    mu = x.mean(axis=0)
    s = x.std(axis=0)

    x_norm = (x - mu) / s

    return (x_norm, mu, s)

     
#Lee los datos del fichero csv
def lee_csv(file_name):
    valores = read_csv(file_name, header=None).values

    return valores.astype(float)


#---------------------------------------------------------------------------#
#-------------------------      CONSTANTES       ---------------------------#
#---------------------------------------------------------------------------#

# Obtenemos los datos del fichero indicado por parametro
datos = lee_csv("ex1data2.csv")

# Entradas Xi de los datos, sin contar el precio
x = datos[:, 0:-1]

# Vector de precios
y = datos[:, -1:]

# Normalizamos las x
x_norm, mu, sigma = normalizar(x)

# Inicializamos las thetas a 0
theta = np.zeros((x_norm[0].size + 1, 1))

# Valor usado para calcular el descenso
alfa = 0.01


# Distancia mínima que tiene que haber entre el coste actual calculado y el anterior
# para considerar que el bucle del descenso gradiente ha terminado
precision = 0.01


#---------------------------------------------------------------------------#
#---------------------      LLAMADA A LA FUNCIÓN      ----------------------#
#---------------------------------------------------------------------------#


#Opcion de ejecución:
opcion = 1
nuevoDato1 = 1650
nuevoDato2 = 3


if(opcion == 0):
    #Calculamos el resultado mediante descenso gradiente
    print("\nVersion con descenso gradiente")
    print("-------------------------------")
    theta = regresionLineal(alfa, x_norm, y, theta, precision, opcion)
    print("El precio esperado es: " + nuevaPrediccion(nuevoDato1, nuevoDato2, opcion) + "\n")
else:
    #Calculamos el resultado mediante ecuacion normal
    print("\nVersion con ecuacion normal")
    print("-------------------------------")
    theta = regresionLineal(alfa, x, y, theta, precision, opcion)
    print("El precio esperado es: " + nuevaPrediccion(nuevoDato1, nuevoDato2, opcion) + "\n")



