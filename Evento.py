class Lugar:
    def __init__(self, registro, pos_x, pos_y):
        self.registro = registro
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipo = None
        self.ocupado = False

    def ocupar(self):
        self.ocupado = True

    def desocupar(self):
        self.ocupado = False

    def posicao_mudar(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def tipo_mudar(self, tipo):
        self.tipo = tipo

    def informacoes_mostrar(self):
        print("Lugar: {0}".format(self.registro))
        print("Posição: ({0}, {1})".format(self.pos_x, self.pos_y))
        print("Ocupado: {0}".format(self.ocupado))
        print("Tipo: {0}\n".format(self.ocupado))


class Evento:
    def __init__(self, registro, nome, quantidade_lugares):
        self.registro = registro
        self.nome = nome
        self.quantidade_lugares = quantidade_lugares
        self.lista_lugares = []
        for i in range(quantidade_lugares):
            self.adicionar = Lugar(i, 0, 0)
            self.lista_lugares.append(self.adicionar)

    def nome_mudar(self, nome):
        self.nome = nome

    def informacoes_mostrar(self):
        print("Registro do evento: {0}".format(self.registro))
        print("Nome: {0},".format(self.nome))
        print("Quantidade de lugares: {0}".format(self.quantidade_lugares))

    def lugares_mostrar(self):
        print("**-----**")
        for i in range(self.quantidade_lugares):
            # print(self.lista_lugares[i])
            print(self.lista_lugares[i].informacoes_mostrar())
        print("---****----")
