#MEGA SENA PROGRAMAÇÃO ORIENTADO A OBJETOS PYTHON by Gabriel R.
import random

class Megasena:
    def __init__(self):
        self.sorteados = []

    def gerando(self):
        while True:
            if len(self.sorteados) == 6:
                break
            else:
                self.sorteados.append(random.randint(1,60))
        print (sorted(self.sorteados))

    def resultado(self, bilhete):
        self.acertos = 0
        self.bilhete = bilhete
        for i in bilhete:
            if i in self.sorteados:
                self.acertos += 1
        print (f"Acertos: {self.acertos}")

sorteio1 = Megasena()
sorteio1.gerando()
sorteio1.resultado([1,10,15,20,25,30])