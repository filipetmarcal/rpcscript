from core.card import Card

class Unit(Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def adicionar_parte(self, parte):
        self.partes.append(parte)

    def remover_parte(self, parte):
        self.partes.remove(parte)
