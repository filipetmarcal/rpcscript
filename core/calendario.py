class Calendario:
    def __init__(
        self,
        ano=1, mes=1, dia=1,
        hora=0, minuto=0, segundo=0,
        *,
        segundos_por_minuto=60,
        minutos_por_hora=60,
        horas_por_dia=24,
        dias_por_mes=30,
        meses_por_ano=12,
        periodos=None
    ):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

        self.segundos_por_minuto = segundos_por_minuto
        self.minutos_por_hora = minutos_por_hora
        self.horas_por_dia = horas_por_dia
        self.dias_por_mes = dias_por_mes
        self.meses_por_ano = meses_por_ano

        self.periodos = periodos or {
            "madrugada": range(0, 5),
            "manha": range(5, 12),
            "tarde": range(12, 18),
            "noite": range(18, self.horas_por_dia)
        }

    def avancar_segundos(self, segundos):
        """Calcula o avanço do tempo usando divisões inteiras (mais eficiente)."""
        self.segundo += segundos

        # Uso de // (divisão inteira) e % (resto) evita loops longos
        if self.segundo >= self.segundos_por_minuto:
            minutos_extras = self.segundo // self.segundos_por_minuto
            self.segundo %= self.segundos_por_minuto
            self.minuto += minutos_extras

        if self.minuto >= self.minutos_por_hora:
            horas_extras = self.minuto // self.minutos_por_hora
            self.minuto %= self.minutos_por_hora
            self.hora += horas_extras

        if self.hora >= self.horas_por_dia:
            dias_extras = self.hora // self.horas_por_dia
            self.hora %= self.horas_por_dia
            self.dia += dias_extras

        # Ajuste de meses e anos (dias começam em 1)
        while self.dia > self.dias_por_mes:
            self.dia -= self.dias_por_mes
            self.mes += 1

        while self.mes > self.meses_por_ano:
            self.mes -= self.meses_por_ano
            self.ano += 1

    def consumir_tempo(self, segundos=0, minutos=0, horas=0, dias=0):
        total_segundos = (
            segundos
            + (minutos * self.segundos_por_minuto)
            + (horas * self.minutos_por_hora * self.segundos_por_minuto)
            + (dias * self.horas_por_dia * self.minutos_por_hora * self.segundos_por_minuto)
        )
        self.avancar_segundos(total_segundos)

    def obter_periodo_atual(self):
        """Retorna o nome do período baseado na hora atual."""
        for nome, intervalo in self.periodos.items():
            if self.hora in intervalo:
                return nome
        return "Desconhecido"

    def __str__(self):
        return f"Data: {self.dia:02d}/{self.mes:02d}/{self.ano:04d} | Hora: {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d} ({self.obter_periodo_atual()})"
