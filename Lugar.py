class Lugar:
    def __init__(self, registro, pos_x, pos_y, ):
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
        print("Tipo: {0}".format(self.ocupado))
        print("")
