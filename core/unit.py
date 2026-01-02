from core.card import Card

class Unit(Card):
    def __init__(
        self,
        fome=0,
        fadiga=0,
        fome_max=100,
        fadiga_max=100,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.fome = fome
        self.fadiga = fadiga
        self.fome_max = fome_max
        self.fadiga_max = fadiga_max
    def esta_faminto(self):
        return self.fome >= self.fome_max

    def esta_exausto(self):
        return self.fadiga >= self.fadiga_max

