import forca
import adivinhacao

def escolhe_jogo():
    
    print('Escolha o seu jogo')

    print('(1) forca (2) adivinhação')

    jogo = int(input('Qual jogo você quer jogar?'))

    if jogo == 1:
        forca.jogar()

    elif jogo == 2: 
        adivinhacao.jogar()
    else:
        print('Escolha uma das opções abaixo')

if (__name__ == '__main__'):
    escolhe_jogo()