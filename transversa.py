import numpy as np
def transversa():
    print("Introduzca el tamaño de la matriz\n")

    filas = int(input("Ingrese el numero de filas: \n"))
    columnas = int(input("Ingrese el numero de columnas: \n"))

    trans = np.zeros([filas,columnas])
    m = np.zeros([filas,columnas])
    for i in range(filas):
        for j in range(columnas):
            print("Introduzca el valor para la posicion", [i,j])
            m[i,j] = input()
            trans[j,i] = m[i,j]
    print("La matriz original es: \n", m,"\n")

    for i in range(columnas):
        for j in range(filas):
            x =+1
    print("La matriz transpuesta es:\n",trans)

    