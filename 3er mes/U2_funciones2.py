import random

def generarLista(a, b, c):
    lista = random.sample(range(b, c + 1), a)
    return lista
  
def encontrarNumero(f, numero):
    for i in range(len(f)):
        if (numero==f[i]):
            print(f"Numero encontrado con busqueda lineal en el indice {i}")
            return 1

def busqueda_binaria(x, num):
    izquierda, derecha = 0, len(x) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 
        if x[medio] == num:
            print(f"Número encontrado con busqueda binaria en el índice {medio}") 
            return medio 
        elif x[medio] < num:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Número no encontrado")
    return -1 