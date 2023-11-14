def horacerta(tempo):
    if tempo > 12:
        horas = tempo - 12
        print(f'O horário é {horas}PM')
    else:
        print(f'O horário é {tempo}AM')
horacerta(float(input('Forneça um horário')))
