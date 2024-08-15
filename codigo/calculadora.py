opcion=int(input("escoja una opcion//1.Suma 2.Resta 3.Multiplicacion 4.Division "))
n1 = int(input("ingrese primer numero "))
n2 = int(input("ingrese segundo numero "))
def suma(n1,n2):
    sum=n1+n2
    return sum
def resta(n1,n2):
    res=n1-n2
    return res
def multiplicacion(n1,n2):
    mul=n1*n2
    return mul
def division(n1,n2):
    div=n1/n2
    return div
if opcion == 1:
    print("resultado: ", suma(n1,n2))
elif opcion == 2:
    print("resultado: ", resta(n1,n2))
elif opcion == 3:
    print("resultado: ", multiplicacion(n1,n2))
elif opcion == 4:
    print("resultado:", division(n1,n2))  
else:
    print("opcion invalida")         