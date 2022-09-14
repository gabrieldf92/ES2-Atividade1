# PEDRA, PAPEL E TESOURA, MELHOR DE 3

import random

# Inicia os contadores...
cont_rodada = 0
vitoria_jogador = 0
vitoria_maquina = 0

# Faz um laço de repetição while que se repete enquanto ambos tem menos de 2 vitórias...
# Quando alguém atingir as duas vitórias ele sai do laço de repetição...
while vitoria_jogador < 2 and vitoria_maquina < 2:

    while True:
        # Recebe a escolha do jogador convertendo pra minúsculo...
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        if escolha_jogador in ["pedra", "papel", "tesoura"]:  # Faz a validação da escolha do jogador...
            break
        else:
            print("Escolha inválida. Escolha entre pedra, papel e tesoura...")

    # Gera um número randômico, com uso de dicionário, que será atribuído a escolha da máquina...
    escolha_maquina = {0:"pedra", 1:"papel", 2:"tesoura"}[random.randrange(3)]
    print(f"A máquina escolheu {escolha_maquina}")

        # Pedra vence tesoura
        # Tesoura vence papel
        # Papel vence pedra

    # Faz as devidas verificações pra determinar o vencedor e incrementa 1 ao contador de vitória...
    if escolha_jogador == escolha_maquina:
        print(" * Empate *")
    elif escolha_jogador == "pedra" and escolha_maquina == "papel":
        vitoria_maquina += 1
        print(" * Máquina venceu! *")
    elif escolha_jogador == "pedra" and escolha_maquina == "tesoura":
        vitoria_jogador += 1
        print(" * Jogador venceu! *")
    elif escolha_jogador == "papel" and escolha_maquina == "pedra":
        vitoria_jogador += 1
        print(" * Jogador venceu! *")
    elif escolha_jogador == "papel" and escolha_maquina == "tesoura":
        vitoria_maquina += 1
        print(" * Máquina venceu! *")
    elif escolha_jogador == "tesoura" and escolha_maquina == "pedra":
        vitoria_maquina += 1
        print(" * Máquina venceu! *")
    elif escolha_jogador == "tesoura" and escolha_maquina == "papel":
        vitoria_jogador += 1
        print(" * Jogador venceu! *")
    
    cont_rodada += 1

# Mostra o resultado final...
print("-"*50)
print(f"{cont_rodada} rodadas disputadas")
# No final só pode dar 2x1 ou 2x0...
if vitoria_jogador == 1 or vitoria_maquina == 1:  # Se for 2x1...
    print("O jogador venceu 1 vez enquanto a máquina venceu 2 vezes" if vitoria_jogador == 1 else "O jogador venceu 2 vezes enquato a máquina venceu 1 vez")
else:  # Se for 2x0...
    print("O jogador venceu 2 vezes enquato a máquina não venceu nenhuma vez" if vitoria_jogador == 2 else "O jogador não venceu nenhuma vez enquato a máquina venceu 2 vezes")
