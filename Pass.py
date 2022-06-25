from PyQt5 import QtCore, QtGui, QtWidgets
import string
import random
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 460)
        MainWindow.setFixedSize(578, 460)
        MainWindow.setStyleSheet('background:rgb(36, 31, 49); font-weight:bold;')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(142, 106, 283, 77))
        self.lineEdit.setStyleSheet("font-size:15pt;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet('color:white; border: 2px solid white; background:rgb(129, 61, 156); font-size:15pt;')
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(197, 203, 176, 80))
        self.generate.setStyleSheet("font-size:20pt;")
        self.generate.setObjectName("generate")
        self.generate.clicked.connect(self.password)
        self.generate.setCursor(QtCore.Qt.PointingHandCursor)
        self.generate.setStyleSheet('*{background:rgb(255, 120, 0); border: 2px solid white; border-radius:20px; color:white; font-size:22pt} :hover{background:rgb(255, 190, 111)}')

        self.saved = QtWidgets.QComboBox(self.centralwidget)
        self.saved.setGeometry(QtCore.QRect(439, 128, 109, 40))
        self.saved.setObjectName("saved")
        self.saved.currentTextChanged.connect(self.combo)
        self.saved.setCursor(QtCore.Qt.PointingHandCursor)
        self.saved.setStyleSheet('color:white; background:rgb(97, 53, 131);')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName('label')
        self.label.setGeometry(QtCore.QRect(200, 20, 283, 77))
        self.label.setStyleSheet('font-size:30pt; color:white;')


        self.value = QtWidgets.QSpinBox(self.centralwidget)
        self.value.setValue(5)
        self.value.setGeometry(QtCore.QRect(61, 122, 64, 44))
        self.value.setObjectName("value")
        self.value.setStyleSheet('color:white; background:rgb(97, 53, 131);')

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(234, 295, 107, 40))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saving)
        self.save.setCursor(QtCore.Qt.PointingHandCursor)
        self.save.setStyleSheet('*{color:white; border:2px solid white; background:rgb(224, 27, 36);} :hover{background:rgb(246, 97, 81);}')


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def password(self):
        length = self.value.value()
        all = string.ascii_lowercase + string.ascii_uppercase + string.digits
        table = []
        for i in range(length):
            gotten = random.choice(all)
            table.append(gotten)
        print(''.join(str(i) for i in table))
        self.lineEdit.setText(''.join(str(i) for i in table))

    def saving(self):
        if self.lineEdit.text() == '':
            pass
        else:
                pass_ = self.lineEdit.text()
                self.saved.addItem(pass_)

    def combo(self):
        value = self.saved.currentText()
        print(value)
        self.lineEdit.setText(value)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate('MainWindow', 'Generate!'))
        self.label.setText(_translate('MainWindow', 'Generate!'))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
