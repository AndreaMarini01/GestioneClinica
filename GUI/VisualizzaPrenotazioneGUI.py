from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.ModificaPrenotazioneGUI import ModificaPrenotazioneGUI


class VisualizzaPrenotazioneGUI(QDialog):

    def __init__(self,listaPrenotazioniCliente):
        super(VisualizzaPrenotazioneGUI, self).__init__()
        loadUi("Visualizza Dopo.ui", self)
        self.modificaPrenotazione=ModificaPrenotazioneGUI(listaPrenotazioniCliente)
        self.modificaPrenotazione.setWindowTitle('Visualizza la prenotazione')
        self.dataOrascelta
        self.prenotazione

    def stampaModifica(self):
        self.dataOraScelta = self.modificaPrenotazione.prenotazioneScelta()
        self.prenotazione = Segreteria.ricercaPrenotazione(self.dataOraScelta)
        #self.pushButton.clicked.connect(self.apriPrenotazione)
        #self.pushButton_2.clicked.connect(self.close)
        if self.prenotazione != None:
            self.apriPrenotazione(self.prenotazione)

    def apriPrenotazione(self,prenotazione):
        self.label_3=prenotazione.cliente
        self.label_5=prenotazione.dottore
        self.label_9=prenotazione.dataOra
        self.label_10=prenotazione.tipoAppuntamento
        self.textEdit=prenotazione.note
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.close)