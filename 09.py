# Faça uma função que retorne o reverso de um número inteiro informado.

def reverso(n):
    return str(n[::-1])


n = str(input("\nInsira um número: ")).strip()

print(f'Reverso: {reverso(n)}')
