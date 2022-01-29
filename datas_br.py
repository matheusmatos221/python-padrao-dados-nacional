from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def dia_cadastro(self):
        dia_cadastro = self.momento_cadastro.day
        return dia_cadastro

    def dia_semana_cadastro(self):
        dia_semana_lista = [
            'segunda-feira',
            'terça-feira',
            'quarta-feira',
            'quinta-feira',
            'sexta-feira',
            'sábado',
            'domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana].capitalize()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1].capitalize()

    def ano_cadastro(self):
        ano_cadastro = self.momento_cadastro.year
        return ano_cadastro

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=30) - self.momento_cadastro
        return tempo_cadastro