import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QStackedWidget

from Amministrazione.Calendario import Calendario
from GUI.EliminaPrenotazioneGUI import EliminaPrenotazioneGUI
from GUI.MenuClienteGUI import MenuClienteGUI
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI
from GUI.loginGUI import loginGUI
from Servizio.Cliente import Cliente

app=QApplication(sys.argv)
#form = loginGUI()
form = Cliente ()
x= Calendario()
form.richiediPrenotazione([datetime(1,2,5)], x.Dottori)
sys.exit(app.exec_())