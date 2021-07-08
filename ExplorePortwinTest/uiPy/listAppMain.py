from PyQt5 import QtCore, QtGui, QtWidgets
from listApp import Ui_ListApp
import io
from pageSwitchingButton import pageSwitchingButton

class listApp(Ui_ListApp):
    def setup(self, ListApp):
        Ui_ListApp.setupUi(self, ListApp)

        self.dataStream = open("echantillon.txt", 'r+')
        self.data = self.dataStream.readlines()

        #self.logsContent.setText(''.join(["%s"] * (len(self.data) - 1)) % tuple(self.data[1:]))

        self.RetourBouton.clicked.connect(self.switchPage(0))
        self.visualiserBouton.clicked.connect(self.switchPage(3))
        self.aJouterBouton.clicked.connect(self.switchPage(2))
        self.validerBouton.clicked.connect(self.ajouter)
        self.RetourBoutonAjout.clicked.connect(self.switchAndClear(0,
                                                                   self.nomText,
                                                                   self.prenomText,
                                                                   self.ageText))

        self.errorAge.setVisible(False)
        self.errorNom.setVisible(False)
        self.errorPrenom.setVisible(False)
        self.errorLabels = [(self.nomText, self.errorNom), (self.prenomText, self.errorPrenom), (self.ageText, self.errorAge)]

        self.currentListY = 0
        self.fillScroll()
        self.stackedWidget.setCurrentIndex(3)
        self.RetourBoutonTest.clicked.connect(self.switchPage(0))


    #default page switching function, pass index of page in stakced widget
    def switchPage(self, index):
        def switch():
            self.stackedWidget.setCurrentIndex(index)
            if index == 2:
                for error in self.errorLabels:
                    error[0].setStyleSheet("")
                    error[1].setVisible(False)
        return switch

    #page switching function with added field clearing, pass list of fields to clear
    def switchAndClear(self, index, *toClear):
        def switching():
            for text in toClear:
                text.clear()
            self.stackedWidget.setCurrentIndex(index)
        return switching

    def clearFields(self, *toClear):
        for text in toClear:
            text.clear()

    #adding function, adtivated upon pressing 'Ajouter' button in page 2 of stakced
    def ajouter(self):
        newdata = str()
        self.dataStream.seek(0, io.SEEK_END) #get to the end of stream to avoid rewriting data

        #fetch data from text fields
        nom = self.nomText.text()
        prenom = self.prenomText.text()
        age = self.ageText.text()

        #build error list to check validity of fields
        #keep list in variable to keep track of which fields are incorrect, for error messages
        error = [not nom.isalpha(), not prenom.isalpha(), not age.isnumeric()]
        if (error[0] or error[1] or error[2]):
            for i in range(len(self.errorLabels)):
                self.errorLabels[i][0].setStyleSheet("border-right: 2px solid red; border-bottom: 2px solid red")
                self.errorLabels[i][1].setVisible(error[i])
            return

        #dump data in string
        newdata += str(self.getIndex()) + '\t'
        newdata += nom + '\t'
        newdata += prenom + '\t'
        newdata += age + '\n'

        #write to the end of file, do not forget to get back to beggining for reading purposes
        self.dataStream.write(newdata)
        self.dataStream.truncate()
        self.dataStream.seek(0, 0)
        self.data.append(newdata)
        self.stackedWidget.setCurrentIndex(0)
        self.createFrame(self.testContents, newdata, self.currentListY)
        self.currentListY += 50
        self.testContents.setMinimumHeight(self.currentListY)
        self.clearFields(self.nomText, self.prenomText, self.ageText)

    #get next valid index in list of persons, to add the next one
    def getIndex(self):
        return (int(self.data[len(self.data) - 1].split('\t')[0]) + 1)

    def createFrame(self, parent, entry, coords):
        vals = entry.split('\t')
        newHor = QtWidgets.QWidget(parent)

        newHor.setGeometry(QtCore.QRect(0, coords, parent.width(), 50))
        newLayout = QtWidgets.QHBoxLayout(newHor)
        newHor.setStyleSheet("QLabel{ border: 2px solid black; margin-right: 16px }")
        id = QtWidgets.QLabel(newHor)
        id.setText(vals[0])
        newLayout.addWidget(id)
        nom = QtWidgets.QLabel(newHor)
        nom.setText(vals[1])
        newLayout.addWidget(nom)
        prenom = QtWidgets.QLabel(newHor)
        prenom.setText(vals[2])
        newLayout.addWidget(prenom)
        age = QtWidgets.QLabel(newHor)
        age.setText(vals[3])
        newLayout.addWidget(age)
        return newHor

    def fillScroll(self):
        coords = 0
        header = self.createFrame(self.testPage, self.data[0], 15)
        header.setGeometry(QtCore.QRect(self.testScroll.x(), 15, self.testScroll.width(), 50))

        for entry in self.data[1:]:
            self.createFrame(self.testContents, entry, coords)
            coords += 50
        self.testContents.setMinimumHeight(coords)
        self.currentListY = coords



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListApp = QtWidgets.QMainWindow()
    ui = listApp()
    ui.setup(ListApp)
    ListApp.show()
    sys.exit(app.exec_())