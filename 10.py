# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, 
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e 
# ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora 
# é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar 
# um 7 antes de tirar este Ponto novamente.

import random
import time


def lancamentoDados():
    resultado_lancamento = random.randrange(2, 13)
    return resultado_lancamento


def verificar_resultado(lancamento):
    if (lancamento in [7, 11]):
        print(f"Você tirou: {lancamento} \nVocê é um natural e ganhou!")
    elif (lancamento in [2, 3, 12]):
        print(f"Você tirou: {lancamento} \n[Craps] VOCÊ PERDEU!")
    else:
        print(f"Você tirou: {lancamento} \nVocê ganhou um Ponto")
        numero = lancamento
        lancamento2 = True
        while (numero != lancamento2):
            lancamento2 = random.randrange(2, 13)
            if (lancamento2 == 7):
                print(f"Você tirou: {lancamento2} \nVocê perdeu!")
                break
            elif (lancamento2 == numero):
                print(f"Você tirou: {lancamento2} \nVocê tirou o mesmo número novamente. você GANHOU")
            else:
                print(f"Você tirou: {lancamento2} \nJogando novamente em 2 segundos...")
                time.sleep(5)


lancamento = lancamentoDados()
verificar_resultado(lancamento)
