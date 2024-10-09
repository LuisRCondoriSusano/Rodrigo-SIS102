import random
def generarLista(a,b,c,f):
    for i in range(a):
        aleatorio=random.randint(b, c)
        f.append(aleatorio)
    return f    
def encontrarNumero(f, numero):
    for i in range(len(f)):
        if (numero==f[i]):
            print(f"numero encontrado en el indice {i}")
            return 1

def busqueda_binaria(x, num):
    izquierda, derecha = 0, len(x) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 
        if x[medio] == num:
            print(f"Número encontrado en el índice {medio}") 
            return medio 
        elif x[medio] < num:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Número no encontrado")
    return -1 


