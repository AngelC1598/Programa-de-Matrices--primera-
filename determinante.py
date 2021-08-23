from tkinter.constants import N
import numpy as np

def det():
    print("Introduzca el tamaño de la matriz\n")
    filas = int(input("Ingrese el numero de filas: \n"))
    columnas = int(input("Ingrese el numero de columnas: \n"))
    orden = int(input("Ingrese el orden de la matriz\n"))
    trans = np.zeros([filas,columnas])
    m = np.zeros([filas,columnas])
    for i in range(filas):
        for j in range(columnas):
            print("Introduzca el valor para la posicion", [i,j])
            m[i,j] = input()
    print("La matriz es: \n", m,"\n")
    m = np.linalg.det(m)
    print(int(m))


#def determinante(m,orden):
#    d = 0.0
#    if(orden == 1):
#        d = m[0,0]
#    else:
#        for j in range(orden):
#            d = d + m[0,j] * cofactores(m,orden,0,j)    
#    return d

    

#def cofactores(m, orden, filas, columnas):
 #   c = np.zeros([filas,columnas])
  #  x = 0
   # y = 0
    #n = orden - 1
    #for i in range(orden):
     #   for j in range(orden):
      #      if(i != filas and j != columnas):
       #         c[x,y] = m[i,j]
        #        y += y
         #       if(y>=n):
          #          x += x
           #         y = 0
   # return pow(-1.0,filas+columnas)*determinante(c,n)

#print("El determinante es: \n", determinante(m,orden))


#det

