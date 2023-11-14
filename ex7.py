import random


def embaralhar_string(palavra):
    palavra = palavra.lower()

    caracteres = list(palavra)

    random.shuffle(caracteres)

    string_embaralhada = ''.join(caracteres)
    print(string_embaralhada)


embaralhar_string(str(input('Digite uma palavra')))
