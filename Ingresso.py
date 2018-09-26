class Ingresso:
    def __init__(self, codigo_verificacao):
        self.codigo_verificacao = codigo_verificacao


class Promocao:
    def __init__(self, nome_promo, porcentagem_promo, data_validade):
        self.nome_promo = nome_promo
        self.porcentagem_promo = porcentagem_promo
        self.data_validade = data_validade
