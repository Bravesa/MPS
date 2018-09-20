class Organizador:
    def __init__(self, registro, nome, telefone, cpf, endereco):
        self.registro = registro
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco

    def dados_mostrar(self):
        print("Registro: {0}".format(self.registro))
        print("Nome: {0}".format(self.nome))
        print("Telefone: {0}".format(self.telefone))
        print("CPF: {0}".format(self.cpf))
        print("Endereco: {0}".format(self.endereco))
