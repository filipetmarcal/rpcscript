from core.unit import Unit

class Inventory(Unit):
    def __init__(self, limite=None, **kwargs):
        super().__init__(**kwargs)
        self.limite = limite

    def adicionar(self, carta):
        if self.limite is None or len(self.inventario) < self.limite:
            self.inventario.append(carta)
            return True
        return False

    def contar_itens(lista):
        inventario = {}
        for item in lista:
            inventario[item] = inventario.get(item, 0) + 1
        return inventario
