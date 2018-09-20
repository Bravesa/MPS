class Usuario:
    def __init__(self, registro, nome, senha):
        self.registro = registro
        self.nome = nome
        self.senha = senha


class Administrador(Usuario):
    def __init__(self, registro, nome, senha):
        Usuario.__init__(self, registro, nome, senha)
        self.tipo = "Administrador"

    def dados_mostrar(self):
        print(self.tipo)
        print("Registro: {0}".format(self.registro))
        print("Nome: {0}".format(self.nome))


class Atendente(Usuario):
    def __init__(self, registro, nome, senha):
        Usuario.__init__(self, registro, nome, senha)
        self.tipo = "Atendente"

    def dados_mostrar(self):
        print(self.tipo)
        print("Registro: {0}".format(self.registro))
        print("Nome: {0}".format(self.nome))
