from datetime import datetime

dia = int(input('\nDia da Semana: '))

class Calendar:
    def __init__(self) -> None:
        self.events = []
    def add_event(self, event):
        self.events.append(event)
    
    @staticmethod
    def is_weekend(date: datetime):
        return date.weekday() > dia

c = Calendar()
c.add_event("party")
curr_date = datetime.now()
print(f'\n{Calendar.is_weekend(curr_date)}\n')