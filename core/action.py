class Action:
    def __init__(self, nome, condicao, efeito):
        self.nome = nome
        self.condicao = condicao
        self.efeito = efeito

    def pode_executar(self, contexto):
        return self.condicao(contexto)

    def executar(self, contexto):
        self.efeito(contexto)
