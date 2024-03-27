velocidade = 61  # velocidade atual do carro
km_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print(f'Carro multado, passou {velocidade-RADAR_1}km/h da velocidade máxima.')
