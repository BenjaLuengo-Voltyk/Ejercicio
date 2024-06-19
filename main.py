import os
import suma
os.system("cls")

while True:
    print("Welcome to the calculator program!")
    print("1. Sumar")
    print("2. Restar")
    print("0. Salir")
    opt = input("Ingrese una opción: ")

    match opt:
        case "1":
            suma()
        case "2":
            #restar()
            pass
        case "0":
            break