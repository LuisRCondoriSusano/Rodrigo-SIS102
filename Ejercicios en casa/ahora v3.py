import random

p_secreta = ["luis", "python", "gustavo", "juego", "electrocardiograma"]
p_sistema = random.choice(p_secreta)
letras_adivinadas = ["_"] * len(p_sistema)
intentos = 6
intento = 0

def menu():
    print(f"La palabra a adivinar es: {''.join(letras_adivinadas)}")
menu()

while intento < intentos:
    letra = input("Ingresa una letra: ")
    
    # Verificar si ya se adivinó esa letra
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra.")
        continue

    intento += 1  # Incrementar el número de intentos
    
    if letra in p_sistema:
        # Reemplazar las letras adivinadas en la posición correcta
        for i, caracter in enumerate(p_sistema):
            if caracter == letra:
                letras_adivinadas[i] = letra
        print(f"Felicidades, la letra '{letra}' está en la palabra secreta.")
    else:
        print(f"Lo siento, la letra '{letra}' no está en la palabra secreta.")
    
    menu()  # Mostrar el estado del juego después de cada intento
    
    # Verificar si ya se adivinó la palabra completa
    if "_" not in letras_adivinadas:
        print("¡Felicidades, has adivinado la palabra!")
        break
else:
    print("Ya no te quedan intentos. ¡Suerte la próxima vez!")
