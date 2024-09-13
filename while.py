#estructura de repeticion
opcion = input("digite la opcion del menu:")
resultado = 1 + 2
while opcion != "salir":
    if opcion == "1": 
        print(f"suma = {resultado}")
    elif opcion == "2":
        print(f"resta =", 3-4)
    elif opcion == "3": 
        print(f"multiplicacion =", 3*4)
    elif opcion == "4":
        print(f"div =", 3/4)
    elif opcion =="5":
        print(f"potencia =", 3**4)
    else:
        print("opcion incorrecta, ingrese del 1 al 5")
        print("fuera del bucle")

