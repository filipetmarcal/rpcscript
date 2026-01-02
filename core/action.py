class Action:
    def __init__(
        self,
        nome,
        condicao,
        efeito,
        *,
        custo_tempo=None
    ):
        self.nome = nome
        self.condicao = condicao
        self.efeito = efeito
        self.custo_tempo = custo_tempo or {}
