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
        dano=0,
        acoes=None
    ):
        self.nome = nome
        self.tipo = tipo
        self.custo = custo
        self.fome = fome
        self.aparencia = aparencia
        self.descricao = descricao
        self.pv = pv
        self.dano = dano

        self.acoes = acoes or []
        self.inventario = []
        self.partes = []
