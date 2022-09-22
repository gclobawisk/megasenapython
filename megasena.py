#MEGA SENA PROGRAMAÇÃO ESTRUTURADA PYTHON by Gabriel R.

import random

def Gerador():
    resultados = []
    while True:
        bola = random.randint(1,60)
        if bola not in resultados:
            resultados.append(bola)

        if len(resultados) == 6:
            break

    return resultados

def Apuracao(aposta):
    acertos = []
    for i in aposta:
        if i in resultados:
            acertos.append(i)
    return acertos

resultados = Gerador()
print (f"Sorteados: {resultados}")

aposta = [2,10,20,25,35,55]

acertos = Apuracao(aposta)
print (f"{len(acertos)} Acertos: {acertos}")