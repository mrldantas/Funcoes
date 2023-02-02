# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o 
# custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100) * Custo


custo = float(input("Insira o custo: "))
taxa = float(input("Insira a taxa de imposto: "))

print(f"Valor com imposto: R${somaImposto(taxa, custo):,.2f}")
