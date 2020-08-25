from random import randint
from time import sleep


class GirarDado:
    def __init__(self):
        # Cria uma lista vazia.
        self.dado = []
        # Pergunta para o usuário.
        self.jogadas = int(input("Digite o número de jogadas: "))

    def jogando_os_dados(self):
        for c in range(self.jogadas):
            print("\n{}º Jogada".format(c + 1))
            sleep(2)
            print("Jogando o dado...")
            sleep(2)
            # Sortei um valor.
            valor_dado = randint(1, 6)
            print("Caiu o valor {}".format(valor_dado))
            # Coloca o valor na lista.
            self.dado.append(valor_dado)
            sleep(2)

    def analisar(self):
        print("\nMaior valor da partida: {}".format(max(self.dado)))
        print("Menor valor da partida: {}".format(min(self.dado)))
        print("\nRanking de jogadas: ")
        # Mostra o ranking de jogadas do maior para o menor valor tirado.
        for p, c in enumerate(sorted(self.dado, reverse=True)):
            print("{}º Lugar: ".format(p + 1), c)


jg = GirarDado()
jg.jogando_os_dados()
jg.analisar()
