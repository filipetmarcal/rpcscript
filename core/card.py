class Card:
    def __init__(
        self,
        nome,
        tipo,
        custo=0,
        fome=0,
        aparencia="",
        descricao="",
        pv=0,
        dano=0
    ):
        self.nome = nome
        self.tipo = tipo
        self.custo = custo
        self.fome = fome
        self.aparencia = aparencia
        self.descricao = descricao
        self.pv = pv
        self.dano = dano

        self.inventario = []
        self.partes = []

    def esta_ativo(self):
        return self.pv > 0

    def receber_dano(self, valor):
        self.pv -= valor
