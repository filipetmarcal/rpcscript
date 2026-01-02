from core.unit import Unit

class Inventory(Unit):
    def __init__(self, limite=None, **kwargs):
        super().__init__(**kwargs)
        self.limite = limite
        self.inventario = []  # inicialização obrigatória

    def adicionar(self, carta):
        """Adiciona uma carta ao inventário se houver espaço."""
        if self.limite is None or len(self.inventario) < self.limite:
            self.inventario.append(carta)
            return True
        return False

    def remover_item(self, carta):
        """
        Remove UMA ocorrência do item do inventário.
        Útil ao consumir ou descartar.
        """
        if carta in self.inventario:
            self.inventario.remove(carta)
            return True
        return False

    def contar_itens(self):
        """
        Retorna um dicionário com a contagem de cada item.
        """
        contagem = {}
        for item in self.inventario:
            contagem[item] = contagem.get(item, 0) + 1
        return contagem

    def contar_por_tipo(self):
        resultado = {}
        for item in self.inventario:
            tipo = item.tipo
            resultado[tipo] = resultado.get(tipo, 0) + 1
        return resultado

    def esta_cheio(self):
        if self.limite is None:
            return False
        return len(self.inventario) >= self.limite
