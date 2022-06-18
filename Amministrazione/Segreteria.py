import datetime
import os
import pickle

from Amministrazione.Calendario import Calendario
from Amministrazione.Sistema import Sistema
from GUI.VisualizzaPrenotazioneGUI import VisualizzaPrenotazioneGUI
from Servizio.Dottore import Dottore



class Segreteria:

    def _init_(self):
        self.listaClienti=[]
        self.listaDottori=[]
        self.leggiOrario()
        self.username="segreteria"
        self.password="1234578"
        self.x=Sistema
        self.appoggioPrezzo=0
        self.calendario=Calendario()

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
                cliente.messaggio.append(messaggio)

    def salvaClienti(self):
        appoggio={}
        for cliente in self.listaClienti:
            appoggio+=cliente.dizio()
        with open('dati/Clienti.pickle', 'wb+') as f:
            pickle.dump(appoggio, f, pickle.HIGHEST_PROTOCOL)

    def leggiClienti(self):
        if os.path.isfile('dati/Clienti.pickle'):
            with open('dati/Clienti.pickle', 'rb+') as f:
                self.listaClienti = pickle.load(f)
        else:
            self.errore()

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

    def modificaOrarioDottore(self):
        dottore= selezionaDottoreGui(self.listaDottori)
        giorno=selezionaGiornoGUI()
        self.listaDottori[dottore].OrarioLavoro[giorno]=selezionaOrarioGUI(self)
        self.salvaOrario()

    def salvaOrario(self):
        dizio={}
        i=0
        for i in range (0,3):
            for j in range (0,5):
                dizio+={'orario dottore'+ i+1 + 'giorno' + j:self.listaDottori[i].OrarioLavoro[j] }
                i+1
        with open('dati/orari.pickle', 'wb+') as f:
            pickle.dump(dizio, f, pickle.HIGHEST_PROTOCOL)

    def leggiOrario(self):
        if os.path.isfile('dati/orari.pickle'):
            with open('dati/orari.pickle', 'rb+') as f:
                appoggio = pickle.load(f)
            for i in range (0,3):
                for j in range(0, 5):
                    self.listaDottori[i].OrarioLavoro[j]=appoggio['orario dottore'+ i+1 + 'giorno' + j]
        else:
            for i in range(0, 3):
                for j in range(0, 5):
                    self.listaDottori[i].OrarioLavoro[j] = datetime.time(hour=10,minute=0)

    def pubblicaAnnuncio(self):
        annuncio=scriviMessaggioGUI()
        dizio={'annuncio': annuncio}
        with open('dati/annunci.pickle', 'wb+') as f:
            pickle.dump(dizio, f, pickle.HIGHEST_PROTOCOL)

    def leggiAnnuncio(self):
        if os.path.isfile('dati/annunci.pickle'):
            with open('dati/annunci.pickle', 'rb+') as f:
                messaggio = pickle.load(f)
            for cliente in self.listaClienti:
                cliente.messaggio.append(messaggio)

    def leggiCertificato(self):
        if os.path.isfile('dati/Certificati.pickle'):
            with open('dati/Certificati.pickle', 'rb+') as f:
                certificato = pickle.load(f)
            stampaCertificatoGUI(certificato)
        else :
            self.errore()

    def leggiRicetta(self):
        if os.path.isfile('dati/Ricetta.pickle'):
            with open('dati/Ricetta.pickle', 'rb+') as f:
                ricetta = pickle.load(f)
            stampaRicettaGUI(ricetta)
        else :
            self.errore()

    def visualizzaCliente(self):
        risposta=sceltaVisualizzaClienteGUI()
        listaClientiDottore=[]
        if risposta == True:
            dottoreSelezionato=selezionaDottoreGUI()
            for cliente in self.listaClienti:
                if cliente.nomeDottore==dottoreSelezionato:
                    listaClientiDottore.append(cliente)
            visualizzaClientiListaGUI(listaClientiDottore)
        else:
            cliente=selezionaClienteGUI(self.listaClienti)
            if cliente!=None
                visualizzaClienteSingoloGUI(cliente)

    def visualizzaOrarioStanzaLibera(self):
        visualizzaOrarioStanzaLiberaGUI(self.calendario.getOrarioStanzaVuota())

    def visualizzaStanzeOccupate(self):
        visualizzaStanzeOccupateGUI(self.calendario.getStanzeOccupate())

    def visualizzaPrenotazione(self):
        risposta=visualizzaPrenotazioneGUI()
        listaPrenotazioni=[]
        if risposta == True:
            dottoreSelezionato=selezionaDottoreGUI()
            for prenotazione in self.x.listaPrenotazioni:
                if prenotazione.dottore==dottoreSelezionato:
                    listaPrenotazioni.append(prenotazione)
            visualizzaPrenotazioneListaGUI(listaPrenotazioni)
        else:
            prenotazione=selezionaPrenotazioniListaGUI(listaPrenotazioni)
            if prenotazione!=None:
                appoggio=VisualizzaPrenotazioneGUI()
                appoggio.apriPrenotazione(prenotazione)