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
        self.condicao = condicao      # função(contexto) -> bool
        self.efeito = efeito          # função(contexto)
        self.custo_tempo = custo_tempo or {}

    def pode_executar(self, contexto):
        return self.condicao(contexto)

    def executar(self, contexto):
        if not self.pode_executar(contexto):
            return False

        # Aplica o efeito
        self.efeito(contexto)

        # Consome tempo
        calendario = contexto.get("calendario")
        if calendario and self.custo_tempo:
            calendario.consumir_tempo(**self.custo_tempo)

        return True
