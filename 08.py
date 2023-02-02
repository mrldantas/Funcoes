# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contador(numero):
    numero = str(numero)
    print(f"O número de dígitos é: {len(numero)}")


n = int(input("\nInsira um número: "))

contador(n)
