import random
p_secreta=["luis", "python", "gustavo", "juego", "electrocardiograma"]
p_sistema=random.choice(p_secreta)
letras_adividas=["_"]*len(p_sistema)
intentos=6
intento=0
def menu():
    print(f"la palabra a adivinar es: {"".join(letras_adividas)}")
    print(f"Su numero de intentos es: {intentos}")
menu()
while intentos<intento:
    letra=input("De una letra")
    if letra in letras_adividas:
        print("Ya adivinaste esta palabra")
        continue
    intento+=1  
    if letra in p_sistema:
        for i, caracter in range(len(p_sistema)):
            if caracter==letra:
                letras_adividas={i}
            
                print(f"Felicidades la letra: {letra} si esta en la palabra secreta ")
            else:
                print(f"La letra {letra} no esta en la palabra")
    if "_" not in letras_adividas:
        print(f"Felicidades adivinaste la palabra: {p_sistema}")
else:
    print("Ya no quedan intentos")    


            

        


    