numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print(f"tentativa {rodada} de {total_de_tentativas}")

    chute_str = input('Digite o seu número: ')
    print(f'Você digitou {chute_str}')
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Parabéns. Você acertou!')
    else:
        if maior:
            print('O seu chute foi maior do que o número secreto!')
        if menor:
            print('O seu chute foi menor do que o número secreto!')
    
    rodada = rodada + 1