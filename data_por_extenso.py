class DATE:
    def __init__(self,dd,mm,yyyy):
        self.day = dd
        self.month = mm
        self.year = yyyy

    def formated(self):
        month_name = {
            '1': 'janeiro',
            '2': 'fevereiro',
            '3': 'março',
            '4': 'abril',
            '5': 'maio',
            '6': 'junho',
            '7': 'julho',
            '8': 'agosto',
            '9': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro'        
        }
        # numeric = f'{self.day:02d}/{self.month:02d}/{self.year:04d}'
        written = f'\n{cidade} {str(self.day)} de {month_name[str(self.month)]} de {str(self.year)}.\n'
        # ret = numeric + ' - ' + written
        ret = written
        print(ret)
        return ret
cidade = input('\nCidade: ')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
new_date = DATE(dia, mes, ano)
new_date.formated()