def soma(n1, n2):
    res_soma = n1 + n2
    print(res_soma)
    return res_soma

def sub(n1, n2):
    res_sub = n1 - n2
    print(res_sub)
    return res_sub

def mult(n1, n2):
    res_mult = n1 * n2
    print(res_mult)
    return res_mult

def div(n1, n2):
    if n2 != 0:
        res_div = n1 / n2
        print(res_div)
    return res_div


opp = input('Qual será a operação realizada?')

if opp == 'soma':
    soma(int(input('Forneça o primeiro número')),int(input('Forneça o segundo número')))

if opp == 'subtração':
    sub(int(input('Forneça o primeiro número')),int(input('Forneça o segundo número')))

if opp == 'multiplicação':
    mult(int(input('Forneça o primeiro número')),int(input('Forneça o segundo número')))

if opp == 'divisão':
    div(int(input('Forneça o primeiro número')),int(input('Forneça o segundo número')))
