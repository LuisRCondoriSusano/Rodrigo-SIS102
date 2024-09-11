import funcion_conversiones
def menu():
    print("-------------Seleccione que conversion desea hacer-------------")
    print("1: metros a kilometros")
    print("2: kilometros a metros")
    print("3: gramos a kilogramos")
    print("4: kilogramos a gramos")
    print("5: celcius a fahrenheit")
    print("6: fahrenheit a celcius")
    print("7: Salir")
menu()
while True:
    
    opcion=int(input("Seleciones que opcion desea hacer: "))
    num1=float(input("Deme un numero: ")) 
    
    if opcion == 7:
        print("Saliendo")
        break
    if opcion == 1:
        print(f"Resultados: {funcion_conversiones.metrosAkilometros(num1):.2f}")
    elif opcion == 2:
        print(f"Resultado: {funcion_conversiones.kilometrosAmetros(num1):.2f}")
    elif opcion == 3:
        print(f"Resultado: {funcion_conversiones.gramosAKilogramos(num1):.2f}")
    elif opcion == 4:
        print(f"Resultado: {funcion_conversiones.kilogramosAgramos(num1):.2f}")
    elif opcion == 5:
        print(f"Resultado: {funcion_conversiones.celsiusAfah(num1):.2f}")    
    elif opcion == 6:
        print(f"Resultado: {funcion_conversiones.fahAcelcuis(num1):.2f}")
