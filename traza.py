import numpy as np

def trazaDematriz(traza):
    print("Introduzca el tamanho de la matriz")
    filas = int(input("Ingrese el numero de filas: \n"))
    columnas = int(input("Ingrese el numero de columnas: \n"))

    m = np.zeros([filas,columnas])

    for i in range(filas):
        for j in range(columnas):
            print("Introduzca el valor para la posicion", [i,j])
            m[i,j] = input()
    print("La matriz es: \n", m)



    print("\n\nCalculando la traza de la matriz")
    traza = np.trace(m)
    print(traza)

   # diago = 0
    #for i in range(filas):
     #   diago = diago + m[i,i]
    #print(str(diago))