velocidade_carro = 50
posicao_carro = 100

VELOCIDADE_MAX_RADAR = 60
POSICA0_RADAR = 100
RADAR_RANGE = 1

if posicao_carro >= 99 and posicao_carro <= 101:
    print('O carro passou pelo radar.')

if velocidade_carro > VELOCIDADE_MAX_RADAR:
    print('A velocidade do carro é superior a permitida pelo radar.')
    
    if posicao_carro >= 99 and posicao_carro <= 101:
        print('O carro foi multado.')
    else:
        print('O carro não foi multado, pois não passou pelo radar.')

