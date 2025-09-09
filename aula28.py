import time

nome = input('Digite seu nome: ')
time.sleep(2)
idade = input('Digite sua idade: ')
time.sleep(2)

if nome and idade:
    print(f'Seu nome é {nome}.')
    time.sleep(2)
    print(f'Seu nome invertido é {nome[::-1]}.')
    time.sleep(2)
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome NÃO contém espaços.')
    time.sleep(2)
    print(f'Seu nome tem {len(nome)} letras.')
    time.sleep(2)
    print(f'A primeira letra do seu nome é {nome[0]}.')
    time.sleep(2)
    print(f'A última letra do seu nome é {nome[-1]}.')
    time.sleep(2)
else:
    print('Desculpe, você deixou campos vazios.')
