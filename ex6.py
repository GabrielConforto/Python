lista = []
t=0
while t !=-1:
    def emp(valor):
        lista.append(valor)
        print(lista)
    emp(input('Forneça um valor'))
    chck = input('Quer adicionar mais valores(S/N)')
    if chck == 'N' or 'n':
        t = -1
        print(lista)

