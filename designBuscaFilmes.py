# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscaFilmes.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(796, 610)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-4, 0, 801, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setToolTip("")
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 31, 941, 21))
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelTituloP = QtWidgets.QLabel(self.centralwidget)
        self.labelTituloP.setGeometry(QtCore.QRect(10, 60, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelTituloP.setFont(font)
        self.labelTituloP.setTextFormat(QtCore.Qt.AutoText)
        self.labelTituloP.setObjectName("labelTituloP")
        self.lineEditTitulo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTitulo.setGeometry(QtCore.QRect(90, 54, 201, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTitulo.sizePolicy().hasHeightForWidth())
        self.lineEditTitulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditTitulo.setFont(font)
        self.lineEditTitulo.setText("")
        self.lineEditTitulo.setObjectName("lineEditTitulo")
        self.ButtonPesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPesquisar.setGeometry(QtCore.QRect(654, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ButtonPesquisar.setFont(font)
        self.ButtonPesquisar.setObjectName("ButtonPesquisar")
        self.labelAnoP = QtWidgets.QLabel(self.centralwidget)
        self.labelAnoP.setGeometry(QtCore.QRect(320, 60, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelAnoP.setFont(font)
        self.labelAnoP.setObjectName("labelAnoP")
        self.comboBoxAno = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxAno.setGeometry(QtCore.QRect(380, 60, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxAno.setFont(font)
        self.comboBoxAno.setObjectName("comboBoxAno")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.comboBoxAno.addItem("")
        self.labelTipoP = QtWidgets.QLabel(self.centralwidget)
        self.labelTipoP.setGeometry(QtCore.QRect(491, 50, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelTipoP.setFont(font)
        self.labelTipoP.setObjectName("labelTipoP")
        self.comboBoxTipo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTipo.setGeometry(QtCore.QRect(550, 60, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxTipo.setFont(font)
        self.comboBoxTipo.setObjectName("comboBoxTipo")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.comboBoxTipo.addItem("")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 941, 21))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(260, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setToolTip("")
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.tbWidgetResult = QtWidgets.QTableWidget(self.centralwidget)
        self.tbWidgetResult.setGeometry(QtCore.QRect(0, 140, 801, 141))
        self.tbWidgetResult.setObjectName("tbWidgetResult")
        self.tbWidgetResult.setColumnCount(4)
        self.tbWidgetResult.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        item.setFont(font)
        self.tbWidgetResult.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        item.setFont(font)
        self.tbWidgetResult.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        item.setFont(font)
        self.tbWidgetResult.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        item.setFont(font)
        self.tbWidgetResult.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 420, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 480, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.labelTituloExibe = QtWidgets.QLabel(self.centralwidget)
        self.labelTituloExibe.setEnabled(True)
        self.labelTituloExibe.setGeometry(QtCore.QRect(70, 320, 511, 46))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.labelTituloExibe.setFont(font)
        self.labelTituloExibe.setText("")
        self.labelTituloExibe.setTextFormat(QtCore.Qt.PlainText)
        self.labelTituloExibe.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelTituloExibe.setWordWrap(True)
        self.labelTituloExibe.setObjectName("labelTituloExibe")
        self.labelAnoExibe = QtWidgets.QLabel(self.centralwidget)
        self.labelAnoExibe.setGeometry(QtCore.QRect(60, 370, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.labelAnoExibe.setFont(font)
        self.labelAnoExibe.setText("")
        self.labelAnoExibe.setObjectName("labelAnoExibe")
        self.labelGeneroExibe = QtWidgets.QLabel(self.centralwidget)
        self.labelGeneroExibe.setGeometry(QtCore.QRect(80, 420, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.labelGeneroExibe.setFont(font)
        self.labelGeneroExibe.setText("")
        self.labelGeneroExibe.setWordWrap(True)
        self.labelGeneroExibe.setObjectName("labelGeneroExibe")
        self.labelDiretorExibe = QtWidgets.QLabel(self.centralwidget)
        self.labelDiretorExibe.setGeometry(QtCore.QRect(240, 370, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.labelDiretorExibe.setFont(font)
        self.labelDiretorExibe.setText("")
        self.labelDiretorExibe.setWordWrap(True)
        self.labelDiretorExibe.setObjectName("labelDiretorExibe")
        self.labelIMDBExibe = QtWidgets.QLabel(self.centralwidget)
        self.labelIMDBExibe.setGeometry(QtCore.QRect(250, 480, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.labelIMDBExibe.setFont(font)
        self.labelIMDBExibe.setText("")
        self.labelIMDBExibe.setObjectName("labelIMDBExibe")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(579, 309, 20, 271))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.labelPoster = QtWidgets.QLabel(self.centralwidget)
        self.labelPoster.setGeometry(QtCore.QRect(591, 313, 201, 266))
        self.labelPoster.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPoster.setObjectName("labelPoster")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 480, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 300, 941, 21))
        self.line_4.setAutoFillBackground(False)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 500, 589, 21))
        self.line_5.setAutoFillBackground(False)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 571, 589, 21))
        self.line_6.setAutoFillBackground(False)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.ButtonAnterior = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAnterior.setGeometry(QtCore.QRect(20, 283, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ButtonAnterior.setFont(font)
        self.ButtonAnterior.setObjectName("ButtonAnterior")
        self.ButtonProxima = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonProxima.setGeometry(QtCore.QRect(675, 283, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ButtonProxima.setFont(font)
        self.ButtonProxima.setObjectName("ButtonProxima")
        self.labelNumResult = QtWidgets.QLabel(self.centralwidget)
        self.labelNumResult.setGeometry(QtCore.QRect(470, 112, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.labelNumResult.setFont(font)
        self.labelNumResult.setText("")
        self.labelNumResult.setObjectName("labelNumResult")
        self.labelNumPag = QtWidgets.QLabel(self.centralwidget)
        self.labelNumPag.setGeometry(QtCore.QRect(380, 287, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.labelNumPag.setFont(font)
        self.labelNumPag.setObjectName("labelNumPag")
        self.plainTESinopse = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTESinopse.setGeometry(QtCore.QRect(0, 510, 588, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.plainTESinopse.setFont(font)
        self.plainTESinopse.setObjectName("plainTESinopse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Filmes e Séries"))
        self.labelTituloP.setText(_translate("MainWindow", "Título:"))
        self.ButtonPesquisar.setText(_translate("MainWindow", "Pesquisar!"))
        self.labelAnoP.setText(_translate("MainWindow", "Ano:"))
        self.comboBoxAno.setItemText(0, _translate("MainWindow", "------"))
        self.comboBoxAno.setItemText(1, _translate("MainWindow", "1984"))
        self.comboBoxAno.setItemText(2, _translate("MainWindow", "1985"))
        self.comboBoxAno.setItemText(3, _translate("MainWindow", "1986"))
        self.comboBoxAno.setItemText(4, _translate("MainWindow", "1987"))
        self.comboBoxAno.setItemText(5, _translate("MainWindow", "1988"))
        self.comboBoxAno.setItemText(6, _translate("MainWindow", "1989"))
        self.comboBoxAno.setItemText(7, _translate("MainWindow", "1990"))
        self.comboBoxAno.setItemText(8, _translate("MainWindow", "1991"))
        self.comboBoxAno.setItemText(9, _translate("MainWindow", "1992"))
        self.comboBoxAno.setItemText(10, _translate("MainWindow", "1993"))
        self.comboBoxAno.setItemText(11, _translate("MainWindow", "1994"))
        self.comboBoxAno.setItemText(12, _translate("MainWindow", "1995"))
        self.comboBoxAno.setItemText(13, _translate("MainWindow", "1996"))
        self.comboBoxAno.setItemText(14, _translate("MainWindow", "1997"))
        self.comboBoxAno.setItemText(15, _translate("MainWindow", "1998"))
        self.comboBoxAno.setItemText(16, _translate("MainWindow", "1999"))
        self.comboBoxAno.setItemText(17, _translate("MainWindow", "2000"))
        self.comboBoxAno.setItemText(18, _translate("MainWindow", "2001"))
        self.comboBoxAno.setItemText(19, _translate("MainWindow", "2002"))
        self.comboBoxAno.setItemText(20, _translate("MainWindow", "2003"))
        self.comboBoxAno.setItemText(21, _translate("MainWindow", "2004"))
        self.comboBoxAno.setItemText(22, _translate("MainWindow", "2005"))
        self.comboBoxAno.setItemText(23, _translate("MainWindow", "2006"))
        self.comboBoxAno.setItemText(24, _translate("MainWindow", "2007"))
        self.comboBoxAno.setItemText(25, _translate("MainWindow", "2008"))
        self.comboBoxAno.setItemText(26, _translate("MainWindow", "2009"))
        self.comboBoxAno.setItemText(27, _translate("MainWindow", "2010"))
        self.comboBoxAno.setItemText(28, _translate("MainWindow", "2011"))
        self.comboBoxAno.setItemText(29, _translate("MainWindow", "2012"))
        self.comboBoxAno.setItemText(30, _translate("MainWindow", "2013"))
        self.comboBoxAno.setItemText(31, _translate("MainWindow", "2014"))
        self.comboBoxAno.setItemText(32, _translate("MainWindow", "2015"))
        self.comboBoxAno.setItemText(33, _translate("MainWindow", "2016"))
        self.comboBoxAno.setItemText(34, _translate("MainWindow", "2017"))
        self.comboBoxAno.setItemText(35, _translate("MainWindow", "2018"))
        self.comboBoxAno.setItemText(36, _translate("MainWindow", "2019"))
        self.comboBoxAno.setItemText(37, _translate("MainWindow", "2020"))
        self.labelTipoP.setText(_translate("MainWindow", "Tipo:"))
        self.comboBoxTipo.setItemText(0, _translate("MainWindow", "------"))
        self.comboBoxTipo.setItemText(1, _translate("MainWindow", "Movie"))
        self.comboBoxTipo.setItemText(2, _translate("MainWindow", "Series"))
        self.label_3.setText(_translate("MainWindow", "Resultado da pesquisa:"))
        item = self.tbWidgetResult.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TÍTULO"))
        item = self.tbWidgetResult.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ANO"))
        item = self.tbWidgetResult.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIPO"))
        item = self.tbWidgetResult.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IMDB ID"))
        self.label_2.setText(_translate("MainWindow", "Título:"))
        self.label_4.setText(_translate("MainWindow", "Ano:"))
        self.label_5.setText(_translate("MainWindow", "Gênero:"))
        self.label_7.setText(_translate("MainWindow", "Diretor:"))
        self.label_8.setText(_translate("MainWindow", "IMDB:"))
        self.labelPoster.setText(_translate("MainWindow", " PÔSTER"))
        self.label_6.setText(_translate("MainWindow", "Sinopse:"))
        self.ButtonAnterior.setText(_translate("MainWindow", "Página anterior"))
        self.ButtonProxima.setText(_translate("MainWindow", "Próxima página"))
        self.labelNumPag.setText(_translate("MainWindow", "0/0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
