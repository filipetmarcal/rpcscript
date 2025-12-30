from core.card import Card

class Part(Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unidade = None

    def associar(self, unidade):
        self.unidade = unidade
        unidade.adicionar_parte(self)
