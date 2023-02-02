# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em
# dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão
# e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M.
# e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro
# formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
# repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversor(hora24):
    hora12 = hora24 - 12
    return hora12


def saida(hora12, hora24, minuto):
    if ((hora24 >= 12) and (hora24 <= 24)):
        print(f"{hora12}:{minuto}PM")
    else:
        print(f"{hora24}:{minuto}AM")


while True:
    hora24 = int(input("\nInsira a hora: "))
    minuto = int(input("Insira o minuto: "))
    hora12 = conversor(hora24)
    saida(hora12,hora24,minuto)
