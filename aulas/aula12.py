velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro = velocidade >= RADAR_1
carro_multado_rd1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro:
    print('Velocidade excedida do radar')

if carro_multado_rd1 and velocidade_carro:
    print('Multado pro excesso de velocidade')