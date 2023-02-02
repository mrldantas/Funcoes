# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres 
# ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, 
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
# Se valores fora da faixa forem informados, eles devem ser modificados para valores 
# dentro da faixa de forma elegante.

def moldura(linha, coluna):
    print("+", "-" * (linha - 2), "+")
    for i in range(coluna - 2):
        print("|", " " * (linha - 2), "|")
    print("+", "-" * (linha-2), "+")


print('\n[Criador de Moldura]\n')

linha = int(input("Insira a quantidade de linhas: "))

while ((linha < 1) or (linha > 20)):
    print("Valor inválido, insira novamente [1-20]: ")
    linha = int(input("Insira a quantidade de linhas: "))
coluna = int(input("Insira a quantidade de colunas: "))
while ((coluna < 1) or (coluna > 20)):
    print("Valor inválido, insira novamente [1-20]: ")
    coluna = int(input("Insira a quantidade de colunas: "))

moldura(linha, coluna)
