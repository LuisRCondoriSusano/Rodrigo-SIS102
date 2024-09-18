import random
n_secreto=random.randint(0,100)
print(n_secreto)
print("Adivine el numero ")

contador=0
while True:
    n_usuario=int(input("De un numero "))
    contador+=1
    if n_usuario<n_secreto:
        print("Demasiado bajo")
    elif n_usuario>n_secreto:
        print("Demasiado alto")
    elif n_usuario==n_secreto:
        print("Felicidades")
        break
    
    
print("El numero de intentos fue: ")
print(contador)