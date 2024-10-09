import random
lista=[]
for i in range(100):
    r=random.randint(0,100)
    lista.append(r)
print(lista)
print(type(lista))
print(len(lista))    

lista_2=[]

rang=int(input("Dame el numero de elementos de la lista "))
Vmin=int(input("Dame el valor minimo que debe tener "))
Vmax=int(input("Dame el valor maximo que debe tener "))
def genlist(rang,Vmin,Vmax):

    for j in range(rang):
        azar=random.randint(Vmin, Vmax)
        lista_2.append(azar)
    print(f"La lista dos es: {lista_2}")
genlist(rang,Vmin,Vmax)
print(lista_2)
print(len(lista_2))