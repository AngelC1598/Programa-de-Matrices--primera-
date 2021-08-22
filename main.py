from os import system
import multiplicacion
import transversa
import traza
import suma
from tkinter import *
print("Bienvenido al programa de Matrices")
input()

menu = 0
while menu != 6:
    print("----------------Calculadora de Matrices----------------")
    print("\nSeleccione la opcion a realizar\n")
    print("1. Traza de una matriz\n","2. Suma de dos Matrices\n", "3. Multiplicacion de dos Matrices\n", "4. Norma de una matriz\n", "5. Traspuesta de una matriz\n", "6. Salir")
    menu = int(input("Ingresa una opcion: "))
    input()

    if menu == 1:
        traza.trazaDematriz(traza)
        input()
        system("cls")
    elif menu == 2:
        suma.sumaDeMatriz(suma)
        input()
        system("cls")
    elif menu == 3:
        multiplicacion.multiplicacion()
        input()
        system("cls")
    elif menu == 4:
        None
    elif menu == 5:
        transversa.transversa()
        input()
        system("cls")
    elif menu == 6:
        system("cls")
        print("Usted está saliendo del programa...")
        input()

        break
    else:
        print("La opcion seleccionada no es válida...")
        input()
        system("cls")