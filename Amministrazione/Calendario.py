from datetime import datetime

from Amministrazione.Stanza import Stanza
from Servizio.Dottore import Dottore


class Calendario:

    def __init__(self):
        self.dataOdierna=datetime.today()
        self.Dottori=[Dottore('Enrico Corradini','3333333333'),Dottore('Andrea Marini','22222222222'),Dottore('Simone Sgalla','1111111111'),Dottore('Domenico Ursino','0000000000')]
        self.orarioStanzaVuota=[]
        self.stanze = [Stanza(self.Dottori[0],0), Stanza(self.Dottori[1],1), Stanza(self.Dottori[2],2), Stanza(self.Dottori[3],3) ]

    def getListaDottori(self):
        return self.Dottori

    def aggiornaStanze(self):
        i=0
        for dottore in self.Dottori:
            if datetime.now>dottore.OrarioLavoro[datetime.weekday()] and datetime.now<dottore.OrarioLavoro[datetime.weekday()]+datetime.time(6):
                self.stanze[i].occupata=True
                self.stanze[i].orarioLibero=dottore.OrarioLavoro[datetime.weekday()]+datetime.time(6)
            else:
               self.stanze[i].orarioLibero=datetime.time.now()
            i+=1

    def getOrarioStanzaVuota(self):
        return self.stanze[0].orarioLibero, self.stanze[1].orarioLibero, self.stanze[2].orarioLibero, self.stanze[3].orarioLibero

    def getStanzeOccupate(self):
        return self.stanze[0].occupata, self.stanze[1].occupata, self.stanze[2].occupata, self.stanze[3].occupata