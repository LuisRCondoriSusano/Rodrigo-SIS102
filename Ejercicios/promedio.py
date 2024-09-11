filas=int(input("numero de filas: "))
columnas=int(input("numero de columnas: "))
matriz=[]
suma=0
for i in range(filas):
    for j in range(columnas):
        fila=[]
        valor=int(input("ingrese los valores para la matriz en {i} {j} "))
        fila.append(valor)
        matriz.append(fila)
        suma+=valor
    print(matriz)
    promedio=suma/filas*columnas
print(promedio)