import datetime
import pickle

from Servizio import Dottore


class Sistema:

    def __init__(self):
        self.annuncio = []
        self.dataPubblicazioneAnnuncio = datetime.datetime (0,0,0)
        self.listaPrenotazioni = []

    def aggiornaDataSistema (self):
        listaGiornataOdierna = []
        for prenotazione in self.listaPrenotazioni:
            if (prenotazione.dataOra == datetime.date.today()):
                listaGiornataOdierna.append(prenotazione)
        for dottore in Segreteria.listaDottori:
            Dottore.listaPrenotazioniDottore = self.ricercaDottore (dottore.getNome, listaGiornataOdierna)

    def ricercaDottore (self, nome, lista):
        listaPrenotazioniDottore = []
        for elemento in lista:
         if (elemento.nomeDottore == nome):
             listaPrenotazioniDottore.append(elemento)

    def invioPromemoria(self, listaPrenotazioniCliente):
        if (datetime.datetime.now()==(listaPrenotazioniCliente.dataOra-datetime.date(0,0,1))):
            return True
        else:
            return False

    def leggiPrenotazioni(self):
        with open('dati/Prenotazioni.pickle', 'rb+') as f:
            self.listaPrenotazioni = pickle.load(f)

    def salvaPrenotazioni(self):
        appoggio = {}
        for prenotazione in self.listaPrenotazioni:
            appoggio += prenotazione.stampaPrenotazione()
        with open('dati/Prenotazioni.pickle', 'wb+') as f:
            pickle.dump(appoggio, f, pickle.HIGHEST_PROTOCOL)











