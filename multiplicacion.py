from os import closerange, system
import numpy as np 
from os import system

def multiplicacion():
    print("Introduzca el tamanho de la primera matriz")
    filas = int(input("Ingrese el numero de filas: \n"))
    columnas = int(input("Ingrese el numero de columnas: \n"))

    m = np.zeros([filas,columnas])

    for i in range(filas):
        for j in range(columnas):
            print("Introduzca el valor para la posicion", [i,j])
            m[i,j] = input()
    print("La matriz es: \n", m)

    print("Introduzca el tamanho de la segunda matriz")
    filas = int(input("Ingrese el numero de filas: \n"))
    columnas = int(input("Ingrese el numero de columnas: \n"))

    n = np.zeros([filas,columnas])

    for x in range(filas):
        for y in range(columnas):
            print("\nIntroduzca el valor para la posicion", [x,y])
            n[x,y] = input()
    print("La matriz es: \n", n)
    input()
    system("cls")


    c = np.zeros([filas,columnas])
    for i in range(filas):
        for j in range(columnas):
            for k in range(filas): 
                c[i][j] += m[i][k] * n[k][j]


    print("La primera matriz es: \n\n", m)
    print("La segunda matriz es: \n\n", n)

    print("\nLa matriz resultante de la multiplicacion es: \n", c)