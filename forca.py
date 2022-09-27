import random as rd

def jogar():
    print('Bem vindo ao jogo de Forca!')

    palavra=palavra_secreta()

    letras_acertadas = ['_'] * len(palavra)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    print(f'Você tem um total de {len(palavra) - erros} tentativas')

    while (not enforcou and not acertou):  # enquanto nao acertou e nao enforcou:
        chute=chutar()
        # usando a função strip() pra remover os espaços desnecessários inseridos no input
        # função upper() transforma as letras em maiusculo, para apenas comparar amsiculo com maiusculo
        if (chute in palavra):
            marca_chute_correto(chute,letras_acertadas,palavra)
        else:
            erros += 1
            print(f'Ops, você errou! Restam {7 - erros} tentativas.')
            desenha_forca(erros)

        enforcou = erros == len(palavra)
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        mensagem_vencedor(palavra)
    else:
        mensagem_perdedor(palavra)

    print('Fim do jogo.')

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_vencedor(palavra):
    print("Parabéns, você ganhou!")
    print(f'A palavra certa era {palavra}')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra}.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_chute_correto(chute,letras_acertadas,palavra):
    index = 0
    for letra in palavra:
        if chute == letra:
            # print(f'Encontrou a letra {letra} na posição {index+1}')
            letras_acertadas[index] = letra
        index += 1

def chutar():
    palpite = input('Qual letra? ')
    chute = palpite.strip().upper()
    return chute

def palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    #print(palavras)
    palavra = palavras[rd.randrange(0, len(palavras)-1)].upper()
    # deixando tudo em maiusculo com .upper() pra nao dar erro na comparacao
    #print(palavra)
    return palavra

if (__name__ == '__main__'):
    jogar()
