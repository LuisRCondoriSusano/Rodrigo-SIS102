opcion=int(input("escoja una opcion//1.Suma 2.Resta 3.Multiplicacion 4.Division "))
n1 = int(input("ingrese primer numero "))
n2 = int(input("ingrese segundo numero "))
sum = n1+n2
res = n1-n2
mul = n1*n2 
div = n1/n2

if opcion=="1":
    print("resultado: ", sum)
elif opcion=="2":
    print("resultado: ", res)
elif opcion=="3":
    print("resultado: ", mul)
elif opcion=="4":
    print("resultado:", div)  
else:
    print("opcion invalida")         