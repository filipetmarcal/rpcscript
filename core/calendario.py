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
        periodos=None
    ):
        # Data e hora atual
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

        # Configuração do tempo (customizável)
        self.segundos_por_minuto = segundos_por_minuto
        self.minutos_por_hora = minutos_por_hora
        self.horas_por_dia = horas_por_dia
        self.dias_por_mes = dias_por_mes
        self.meses_por_ano = meses_por_ano

        # Períodos do dia (opcional)
        self.periodos = periodos or {
            "madrugada": range(0, 5),
            "manha": range(5, 10),
            "tarde": range(10, 15),
            "fim_de_tarde": range(15, 19),
            "noite": range(19, self.horas_por_dia)
        }

def avancar_segundos(self, segundos):
    self.segundo += segundos

    while self.segundo >= self.segundos_por_minuto:
        self.segundo -= self.segundos_por_minuto
        self.minuto += 1

    while self.minuto >= self.minutos_por_hora:
        self.minuto -= self.minutos_por_hora
        self.hora += 1

    while self.hora >= self.horas_por_dia:
        self.hora -= self.horas_por_dia
        self.dia += 1

    while self.dia > self.dias_por_mes:
        self.dia = 1
        self.mes += 1

    while self.mes > self.meses_por_ano:
        self.mes = 1
        self.ano += 1

def consumir_tempo(
    self,
    *,
    segundos=0,
    minutos=0,
    horas=0,
    dias=0
):
    total_segundos = (
        segundos
        + minutos * self.segundos_por_minuto
        + horas * self.minutos_por_hora * self.segundos_por_minuto
        + dias * self.horas_por_dia * self.minutos_por_hora * self.segundos_por_minuto
    )

    self.avancar_segundos(total_segundos)

