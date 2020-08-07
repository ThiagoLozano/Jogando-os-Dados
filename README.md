# PROJETO PYTHON: Jogando os Dados

> Um programa que simula uma jogo de dados.

  O programa deve perguntar quantas partidas o usuário deseja fazer, depois, retornar uma mensagem de qual
jogada está sendo referida, gerar um valor randômico simulando os valores do dado e mostrar para o usuário
qual valor caiu, fazer isso até o fim das jogadas. Mostrar para o usuário qual foi o maior e o menor valor
tirado no dado e um ranking do maior até o menor valor tirado.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
class GirarDado:
    def __init__(self):
        self.dado = []
        self.jogadas = int(input("Digite o número de jogadas: "))
```
![Classe](https://github.com/ThiagoLozano/Jogando-os-Dados/blob/master/Screenshot/Classe.PNG)

### Função que mostra o valor gerado no dado
```
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
```
![jogando os dados](https://github.com/ThiagoLozano/Jogando-os-Dados/blob/master/Screenshot/Funcao_jogando_os_dados.PNG)

# Bibliotecas e Configurações

### Biblioteca Python Utilizada

```
from random import randint
from time import sleep
```
![Biblioteca](https://github.com/ThiagoLozano/Jogando-os-Dados/blob/master/Screenshot/Biblioteca.PNG)
