nome = 'Patrick Peçanha'
altura = 1.76
peso = 95
imc = peso / (altura) ** 2

# Introdução a "f-strings"

linha_1 = f'{nome} tem {altura:.2f} m de altura,'
linha_2 = f'peso {peso} kg e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


