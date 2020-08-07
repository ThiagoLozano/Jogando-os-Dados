from random import randint
from time import sleep


class GirarDado:
    def __init__(self):
        self.dado = []
        self.jogadas = int(input("Digite o número de jogadas: "))

    def jogando_os_dados(self):
        for c in range(self.jogadas):
            print("\n{}º Jogada".format(c + 1))
            sleep(2)
            print("Jogando o dado...")
            sleep(2)
            valor_dado = randint(1, 6)
            print("Caiu o valor {}".format(valor_dado))
            self.dado.append(valor_dado)
            sleep(2)

    def analisar(self):
        print("\nMaior valor da partida: {}".format(max(self.dado)))
        print("Menor valor da partida: {}".format(min(self.dado)))
        print("\nRanking de jogadas: ")
        for p, c in enumerate(sorted(self.dado, reverse=True)):
            print("{}º Lugar: ".format(p + 1), c)


jg = GirarDado()
jg.jogando_os_dados()
jg.analisar()
