import random


def embaralhar(palavra):
    embaralhada = ''.join(random.sample(palavra, len(palavra)))
    return embaralhada


palavra = str(input("\nInsira uma palavra: "))

print(f"Palavra embaralhada: {embaralhar(palavra)}")
