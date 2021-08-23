import numpy as np

def norma():
    print("Introduzca el tamaño de la matriz\n")
    filas = int(input("Ingrese el numero de filas: \n"))
    columnas = int(input("Ingrese el numero de columnas: \n"))
    m = np.zeros([filas,columnas])
    for i in range(filas):
        for j in range(columnas):
            print("Introduzca el valor para la posicion", [i,j])
            m[i,j] = input()
    print("La matriz original es: \n", m,"\n")

    m = np.linalg.norm(m)
    print("La norma es: \n", m)