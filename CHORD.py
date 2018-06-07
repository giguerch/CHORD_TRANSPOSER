### -*- Encoding: utf-8 -*-
from PyQt5 import QtWidgets
from template import Ui_MainWindow
from about import Ui_Dialog
import sys

class SecondWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        

class ApplicationWindow(QtWidgets.QMainWindow):
    # Fonction pour lancer l'interface. 
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Association des actions à des fonctions.
        self.ui.comboBox.activated.connect(self.setorig)
        self.ui.comboBox_2.activated.connect(self.settransp)
        self.ui.spinBox.valueChanged.connect(self.clickroulette)
        self.ui.actionAbout.triggered.connect(self.about)
    # Menu about
    def about(self):
        self.abd = SecondWindow()
        self.abd.show()
    # Action si on change l'accord original. 
    def setorig(self):
        trIndex = (self.ui.comboBox.currentIndex() + self.ui.spinBox.value()) % 12
        self.ui.comboBox_2.setCurrentIndex(trIndex)
    # Action si on change l'intervalle de transposition.
    def clickroulette(self):
        trIndex = (self.ui.comboBox.currentIndex() + self.ui.spinBox.value()) % 12
        self.ui.comboBox_2.setCurrentIndex(trIndex)
    # Action si on change l'accord transposé.
    def settransp(self):
        trIndex = (self.ui.comboBox_2.currentIndex() - self.ui.comboBox.currentIndex())
        trIndex2 = trIndex - 12 
        if(abs(trIndex) < abs(trIndex2)): 
            self.ui.spinBox.setValue(trIndex)
        if(abs(trIndex) >= abs(trIndex2)):
            self.ui.spinBox.setValue(trIndex2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

