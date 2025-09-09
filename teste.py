'''Verificação de idade
Peça a idade do usuário e:
Se for menor que 12 → escreva "Você é uma criança".
Se for entre 12 e 17 → escreva "Você é um adolescente".
Se for entre 18 e 59 → escreva "Você é adulto".
Se for 60 ou mais → escreva "Você é idoso".'''


idade = input('Digite sua idade: ')

try:
    idade_int = int(idade)

    if idade_int >= 0 and idade_int < 12:
        print('Você é uma criança.')
    elif idade_int >= 12 and idade_int <= 17:
        print('Você é um adolescente.')
    elif idade_int > 17 and idade_int <= 59:
        print('Você é um adulto.')
    elif idade_int > 59:
        print('Você é um idoso.')
    else:
        print('Dados inválidos. Digite apenas números positivos.')
        
except ValueError:
   print('Dados inválidos. Digite apenas números inteiros.')