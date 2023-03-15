def jogar():
    print('***********************************')
    print('*****Bem vindo ao jogo forca!******')
    print('***********************************')
    print('Desenvolvido por Rafael C. Oliveira')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        
        chute = input('Qual letra você quer tentar? ')
        chute = chute.strip()
        
        index = 0

        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print(f'Encontrei {letra} na posição {index}')
            index = index + 1
        
        print('jogando...')

        



if (__name__ == '__main__'):
    jogar()