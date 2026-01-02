class Calendario:
    def __init__(
        self,
        ano=1,
        mes=1,
        dia=1,
        hora=0,
        minuto=0,
        segundo=0,
        *,
        segundos_por_minuto=60,
        minutos_por_hora=60,
        horas_por_dia=24,
        dias_por_mes=30,
        meses_por_ano=12,
        nome="Calendário Padrão"
    ):
        # Identidade
        self.nome = nome

        # Data atual
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

        # Regras do tempo
        self.segundos_por_minuto = segundos_por_minuto
        self.minutos_por_hora = minutos_por_hora
        self.horas_por_dia = horas_por_dia
        self.dias_por_mes = dias_por_mes
        self.meses_por_ano = meses_por_ano

    # =========================
    # Avanço de tempo
    # =========================

    def avancar_segundos(self, segundos: int):
        self.segundo += segundos

        if self.segundo >= self.segundos_por_minuto:
            extra_minutos = self.segundo // self.segundos_por_minuto
            self.segundo %= self.segundos_por_minuto
            self.avancar_minutos(extra_minutos)

    def avancar_minutos(self, minutos: int):
        self.minuto += minutos

        if self.minuto >= self.minutos_por_hora:
            extra_horas = self.minuto // self.minutos_por_hora
            self.minuto %= self.minutos_por_hora
            self.avancar_horas(extra_horas)

    def avancar_horas(self, horas: int):
        self.hora += horas

        if self.hora >= self.horas_por_dia:
            extra_dias = self.hora // self.horas_por_dia
            self.hora %= self.horas_por_dia
            self.avancar_dias(extra_dias)

    def avancar_dias(self, dias: int):
        self.dia += dias

        if self.dia > self.dias_por_mes:
            extra_meses = (self.dia - 1) // self.dias_por_mes
            self.dia = ((self.dia - 1) % self.dias_por_mes) + 1
            self.avancar_meses(extra_meses)

    def avancar_meses(self, meses: int):
        self.mes += meses

        if self.mes > self.meses_por_ano:
            extra_anos = (self.mes - 1) // self.meses_por_ano
            self.mes = ((self.mes - 1) % self.meses_por_ano) + 1
            self.avancar_anos(extra_anos)

    def avancar_anos(self, anos: int):
        self.ano += anos

    # =========================
    # Utilidades
    # =========================

    def snapshot(self) -> str:
        return (
            f"{self.nome} — "
            f"{self.dia:02d}/{self.mes:02d}/{self.ano} "
            f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
        )

    def periodo_do_dia(self) -> str:
        if 6 <= self.hora < 12:
            return "Manhã"
        if 12 <= self.hora < 18:
            return "Tarde"
        if 18 <= self.hora < self.horas_por_dia:
            return "Noite"
        return "Madrugada"
