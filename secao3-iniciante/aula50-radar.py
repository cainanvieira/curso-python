velocidade = 99  # velocidade atual do carro
km_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_ultrapassou = velocidade > RADAR_1
range_99 = LOCAL_1 - RADAR_RANGE
range_101 = LOCAL_1 + RADAR_RANGE
carro_multado = km_carro >= range_99 and km_carro <= range_101 and velocidade_ultrapassou

if carro_multado:
    if velocidade_ultrapassou:
        print('Carro acima da velocidade permitida')
    print(f'Carro carro multado, ultrapassou {velocidade - RADAR_1}km/h da velocidade máxima')
