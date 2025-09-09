'''Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a
saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa Noite - 18-23.'''


entrada_hora = input('Digite a hora utilizando números inteiros entre 0 h a 23 h: ')

try:
    entrada_hora_int = int(entrada_hora)
    if entrada_hora_int >= 0 and entrada_hora_int <= 11:
        print('Bom dia!')
    
    elif entrada_hora_int >= 12 and entrada_hora_int <= 17:
        print('Boa tarde!')
    
    elif entrada_hora_int >= 18 and entrada_hora_int <= 23:
        print('Boa noite!')
    else:
        print('Você não digitou um horário válido.')

except:
    print('Você não digitou um horário válido.')