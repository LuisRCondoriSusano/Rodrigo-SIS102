Estudiantes=int(input("ingrese el numero de estudiantes: "))
NumCalificaciones=int(input("ingrese cuantas calificaciones dara por estudiante: "))
Calificaciones=[]
for i in range(Estudiantes):
    CalDeEstudiante1=[]
    #creamos una variable vacia para llenar las notas que deseamos
    for j in range(NumCalificaciones):
        nota=int(input("ingrese las notas: "))
        CalDeEstudiante1.append(nota)
    #añadimos las notas a la variavle inicial    
    Calificaciones.append(CalDeEstudiante1)
# se crea un nuevo bucle para poner en una variable las notas que se llenaron para cada estudiante
for i in range(Estudiantes):
        #se añade las notas de cada estudiante de cada iteracion a una variable nueva
        Calificaciones2=Calificaciones[i]
        #se suma las notas
        Suma=sum(Calificaciones2)
        #se saca el promedio
        promedio=Suma/NumCalificaciones
        print(f"la suma de cal. de este estudiante es: {Suma}")
        print(f"el promedio de cal. de este estudiante es: {promedio}")    

        