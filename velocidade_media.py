"""
    02/05/2021
    Projeto desenvolvido para a disciplina de Modelagem e Simulação de Sistemas da Faculdade Impacta de Tecnologia.
    Integrantes:
        Aparecido
        Cibele
        Carolini
        Daniel
        Humberto
        Victor
        
    Professor:
        Fábio
"""

import RPi.GPIO as GPIO
import time

sensorInicio = 2
sensorFim = 4
led = 3
sleeptime = 0.4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorInicio, GPIO.IN)
GPIO.setup(sensorFim, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

tempoInicio = ['None']
tempoFim = ['None']

contador = 0

while contador < 2:
    
    if GPIO.input(sensorInicio) == GPIO.LOW:
        GPIO.output(led, not GPIO.input(sensorInicio))
        time.sleep(sleeptime)
        GPIO.output(led, GPIO.LOW)
        tempo1 = time.localtime()
        contador += 1
                
    elif GPIO.input(sensorFim) == GPIO.LOW:
        GPIO.output(led, not GPIO.input(sensorFim))
        time.sleep(sleeptime)
        GPIO.output(led, GPIO.LOW)
        tempo2 = time.localtime()
        contador += 1
             
    print('Aguardando leitura...')
  
tempoInicio = tempo1[5]
tempoFim = tempo2[5]
tempoTotal = tempoFim - tempoInicio
velocidade = 17/(tempoFim - tempoInicio)

print('#############################################################')

if velocidade >= 18.19:
    print('Velocidade média permitida: 18.19 cm/s')
    print('Velocidade média acima do permitido! Veículo multado!')
else:
    print('Velocidade média permitida: 18.19 cm/s')
    print('Velocidade média dentro do permitido!')

print('#############################################################')
print('Distância entre sensores: 17cm')
print('Tempo total:', tempoTotal, 's')
print('Velocidade média do veículo:', velocidade , 'cm/s' )  
print('Fim da leitura!')
    