class Realm:
    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao
        self.unidades = []
        self.acoes = []

    def adicionar_unidade(self, unidade):
        self.unidades.append(unidade)

    def adicionar_acao(self, acao):
        self.acoes.append(acao)
