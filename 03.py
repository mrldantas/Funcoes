# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a, b, c):
    print("\nA soma é igual a:", a + b + c)


valor = []

for i in range(3):
    print(f"\nArgumento n°{i + 1}")
    valor.append(int(input("Insira o valor: ")))

soma(valor[0], valor[1], valor[2])
