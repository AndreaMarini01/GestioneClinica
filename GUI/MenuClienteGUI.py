from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.EliminaPrenotazioneGUI import EliminaPrenotazioneGUI
from GUI.ModificaPrenotazioneGUI import ModificaPrenotazioneGUI
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI
from GUI.VisualizzaPrenotazioneGUI import VisualizzaPrenotazioneGUI


class MenuClienteGUI(QDialog):

    def __init__(self):
        super(MenuClienteGUI, self).__init__()
        loadUi("MenuCliente.ui", self)
        self.nuovaPrenotazione = NuovaPrenotazioneGUI(['a','b'])
        self.eliminaPrenotazione = EliminaPrenotazioneGUI(['a','b'])
        self.modificaPrenotazione = ModificaPrenotazioneGUI (['a','b'],['a','b'])
        self.visualizzaPrenotazioni = VisualizzaPrenotazioneGUI (['a','b'])


    def menu (self):
        self.show()
        self.pushButton.clicked.connect(self.nuovaPrenotazione.stampa)
        self.pushButton_2.clicked.connect(self.eliminaPrenotazione.stampa)
        self.pushButton_3.clicked.connect(self.modificaPrenotazione.stampa)
        self.pushButton_4.clicked.connect(self.visualizzaPrenotazioni.stampa())







