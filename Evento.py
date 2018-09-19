class Evento:
    def __init__(self, registro, nome, quantidade_lugares):
        self.registro = registro
        self.nome = nome
        self.quantidade_lugares = quantidade_lugares

    def nome_mudar(self, nome):
        self.nome = nome

    def informacoes_mostrar(self):
        print("Registro do evento: {0}".format(self.registro))
        print("Nome: {0},".format(self.nome))
        print("Quantidade de lugares: {0}".format(self.quantidade_lugares))
