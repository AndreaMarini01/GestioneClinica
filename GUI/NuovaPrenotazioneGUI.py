from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi



class NuovaPrenotazioneGUI(QDialog):

    def __init__(self,lista1):
        super(NuovaPrenotazioneGUI, self).__init__()
        loadUi("Prenotazione.ui", self)
        self.comboBox_2.addItems(lista1)
        self.comboBox.addItems(['Certificato', 'Ricetta', 'Visita Medica Generica'])
        self.textEdit.toPlainText()


    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.chiudiFinestra)
        self.pushButton_2.clicked.connect(self.close)


    def chiudiFinestra(self):
        self.close()
        return self.comboBox_2.currentText(), self.comboBox.currentText(), self.textEdit.toPlainText()









