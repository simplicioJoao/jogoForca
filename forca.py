import random

palavras = ["jogo", "trabalho", "julgamento", "internet", "escolha", "dados"]
palavra_aleatoria = random.choice(palavras)
#print(palavra_aleatoria)
#print(len(palavra_aleatoria))

display = []
for n in range(len(palavra_aleatoria)):
    display.append("_")
print(display)

vidas = 6
while vidas > 0 and "_" in display:
    i = 0
    acertou = False
    chute = input("Digite uma letra: ")
    print(chute)
    for letra in palavra_aleatoria:
        if chute == letra:
            display[i] = chute
            acertou = True
        i += 1
    if not acertou:
        vidas -= 1
    print(display)
    print(vidas)

if vidas > 0:
    print("Voce ganhou!!!")
else:
    print("Voce perdeu...")