class Usuario:
    def __init__(self, registro, nome, senha):
        self.registro = registro
        self.nome = nome
        self.senha = senha


class Administrador:
    def __init__(self):
        self.grupo = "Administradores"


class Atendente:
    def __init__(self):
        self.grupo = "Atendentes"


class Cliente:
    def __init__(self):
        self.grupo = "Clientes"
