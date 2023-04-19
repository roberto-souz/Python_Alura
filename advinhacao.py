import random

# Escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Define o número máximo de tentativas
num_tentativas = 5

# Loop principal do jogo
for tentativa in range(1, num_tentativas + 1):
    print("Tentativa", tentativa)
    
    # Pede ao jogador para adivinhar o número
    guess = int(input("Digite um número entre 1 e 100: "))
    
    # Verifica se o jogador acertou o número
    if guess == numero_secreto:
        print("Parabéns! Você acertou o número em", tentativa, "tentativas!")
        break
    
    # Verifica se o jogador chutou muito alto ou muito baixo
    elif guess < numero_secreto:
        print("Chute um número maior.")
    else:
        print("Chute um número menor.")
        
# Se o jogador não acertar o número dentro do número máximo de tentativas, informa o número secreto
if tentativa == num_tentativas and guess != numero_secreto:
    print("Fim de jogo! O número secreto era", numero_secreto)
