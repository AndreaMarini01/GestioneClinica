import sys

from PyQt5.QtWidgets import QApplication, QStackedWidget

from GUI.EliminaPrenotazioneGUI import EliminaPrenotazioneGUI
from GUI.MenuClienteGUI import MenuClienteGUI
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI
from GUI.loginGUI import loginGUI

app=QApplication(sys.argv)
form = loginGUI()
sys.exit(app.exec_())