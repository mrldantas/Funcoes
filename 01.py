# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def executar(n):
    for i in range(n):
        i = i + 1
        print((str(i)+"   ")*i)


n = int(input("Insira n: "))

executar(n)
