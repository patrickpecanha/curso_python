'''Faça um programa que peça ao usuário para digitar um número inteiro, informe
se esse número é par ou ímpar. Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro.'''

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    resto_numero = numero_int % 2

    print(resto_numero)


    if resto_numero == 0:
        print('O número digitado é PAR.')
    else:
        print('O número digitado é ÍMPAR.')

except:
    print('O número digitado não é um INTEIRO.')