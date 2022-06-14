import datetime
import os
import pickle

from Amministrazione.Sistema import Sistema
from Servizio.Dottore import Dottore



class Segreteria:

    def _init_(self):
        self.listaClienti=[]
        self.listaDottori=[]
        self.username="segreteria"
        self.password="1234578"
        self.x=Sistema
        self.appoggioPrezzo=0

    def ricercaPrenotazioneData(self,data,listaPrenotazioni):
        listaOdierna=[]
        for prenotazione in listaPrenotazioni:
            if prenotazione.dataOra.date==data:
                listaOdierna.append(prenotazione)
            elif prenotazione.dataOra.date<data:
                self.eliminaPrenotazione(listaPrenotazioni,prenotazione)
        return listaOdierna

    def eliminaPrenotazione(self,prenotazione):
        for elem in self.x.listaPrenotazioni:
            if elem==prenotazione:
                self.x.listaPrenotazioni.remove(prenotazione)
        self.x.salvaPrenotazioni()

    def aggiornaStatoClinica(self):
        data = datetime.datetime.today()
        listaOdierna = self.ricercaPrenotazioneData(data.date,self.x.listaPrenotazioni)
        Dottore.listaPrenotazioni = listaOdierna

    def compilaRicevuta(self):
        if self.appoggioPrezzo != 0:
            x=compilaRicevutaGUI
            if x == True:
                Ricevuta.stampa (self.appoggioPrezzo)

    def eliminaCartellaClinica(self,id):
        os.remove('dati/CC/cartella' + str(self.id) + '.pickle')

    def inviaMessaggioSingolo(self):
        messaggio, nome = MessaggioGUI
        for cliente in self.listaClienti:
            if cliente.nome == nome:
                cliente.messaggio = messaggio

    def salvaClienti(self):
        appoggio={}
        for cliente in self.listaClienti:
            appoggio+=cliente.dizio()
        with open('dati/Clienti.pickle', 'wb+') as f:
            pickle.dump(appoggio, f, pickle.HIGHEST_PROTOCOL)

    def leggiClienti(self):
        with open('dati/Clienti.pickle', 'rb+') as f:
            self.listaClienti = pickle.load(f)

    def ricercaCliente(self,cliente):
        for elem in self.listaClienti:
            if elem.nomeCognome==cliente:
                return elem

    def modificaCliente(self):
        cliente=selezionaClienteGUI(self.listaClienti)
        appoggio=self.ricercaCliente(cliente)
        self.listaClienti.remove(appoggio)
        appoggio.nomeCognome, appoggio.email,appoggio.numTelefono=modificaClienteGUI(cliente)
        self.listaClienti.append(appoggio)
        self.salvaClienti()

    def eliminaCliente(self):
        cliente = selezionaClienteGUI(self.listaClienti)
        self.listaClienti.remove(self.ricercaCliente(cliente))
        self.salvaClienti()