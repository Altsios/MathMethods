# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linear.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self,  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(246, 175)
        MainWindow.setMaximumSize(QtCore.QSize(246, 175))
        self.linbutt = QtWidgets.QPushButton(MainWindow)
        self.linbutt.setGeometry(QtCore.QRect(80, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.linbutt.setFont(font)
        self.linbutt.setObjectName("linbutt")
        self.parStxt = QtWidgets.QLabel( MainWindow)
        self.parStxt.setGeometry(QtCore.QRect(120, 30, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parStxt.setFont(font)
        self.parStxt.setObjectName("parStxt")
        self.parEtxt = QtWidgets.QLabel(MainWindow)
        self.parEtxt.setGeometry(QtCore.QRect(120, 50, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parEtxt.setFont(font)
        self.parEtxt.setObjectName("parEtxt")
        self.textEditSpar = QtWidgets.QTextEdit(MainWindow)
        self.textEditSpar.setGeometry(QtCore.QRect(170, 30, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditSpar.setFont(font)
        self.textEditSpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditSpar.setUndoRedoEnabled(True)
        self.textEditSpar.setAcceptRichText(True)
        self.textEditSpar.setObjectName("textEditSpar")
        self.textEditEpar = QtWidgets.QTextEdit(MainWindow)
        self.textEditEpar.setGeometry(QtCore.QRect(170, 56, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditEpar.setFont(font)
        self.textEditEpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditEpar.setUndoRedoEnabled(True)
        self.textEditEpar.setAcceptRichText(True)
        self.textEditEpar.setObjectName("textEditEpar")
        self.textEditEEpar = QtWidgets.QTextEdit(MainWindow)
        self.textEditEEpar.setGeometry(QtCore.QRect(170, 80, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditEEpar.setFont(font)
        self.textEditEEpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditEEpar.setUndoRedoEnabled(True)
        self.textEditEEpar.setAcceptRichText(True)
        self.textEditEEpar.setObjectName("textEditEEpar")
        self.parEEtxt = QtWidgets.QLabel(MainWindow)
        self.parEEtxt.setGeometry(QtCore.QRect(130, 80, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parEEtxt.setFont(font)
        self.parEEtxt.setObjectName("parEEtxt")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(90, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEditEpar_2 = QtWidgets.QTextEdit(MainWindow)
        self.textEditEpar_2.setGeometry(QtCore.QRect(40, 56, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditEpar_2.setFont(font)
        self.textEditEpar_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditEpar_2.setUndoRedoEnabled(True)
        self.textEditEpar_2.setAcceptRichText(True)
        self.textEditEpar_2.setObjectName("textEditEpar_2")
        self.parktxt = QtWidgets.QLabel(MainWindow)
        self.parktxt.setGeometry(QtCore.QRect(10, 30, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parktxt.setFont(font)
        self.parktxt.setObjectName("parktxt")
        self.textEditKpar = QtWidgets.QTextEdit(MainWindow)
        self.textEditKpar.setGeometry(QtCore.QRect(40, 31, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditKpar.setFont(font)
        self.textEditKpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditKpar.setUndoRedoEnabled(True)
        self.textEditKpar.setAcceptRichText(True)
        self.textEditKpar.setObjectName("textEditKpar")
        self.paEtxt_2 = QtWidgets.QLabel(MainWindow)
        self.paEtxt_2.setGeometry(QtCore.QRect(10, 50, 16, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.paEtxt_2.setFont(font)
        self.paEtxt_2.setObjectName("paEtxt_2")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 61, 16))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Параметры"))
        self.linbutt.setText(_translate("Form", "График"))
        self.parStxt.setText(_translate("Form", "Старт="))
        self.parEtxt.setText(_translate("Form", "Конец="))
        self.textEditSpar.setHtml(_translate("Form",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-0.5</p></body></html>"))
        self.textEditSpar.setPlaceholderText(_translate("Form", "-0.5"))
        self.textEditEpar.setHtml(_translate("Form",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.5</p></body></html>"))
        self.textEditEpar.setPlaceholderText(_translate("Form", "0.5"))
        self.textEditEEpar.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.001</p></body></html>"))
        self.textEditEEpar.setPlaceholderText(_translate("Form", "0.001"))
        self.parEEtxt.setText(_translate("Form", "Шаг="))
        self.label.setText(_translate("Form", "y=kx+b"))
        self.textEditEpar_2.setHtml(_translate("Form",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textEditEpar_2.setPlaceholderText(_translate("Form", "0"))
        self.parktxt.setText(_translate("Form", "k="))
        self.textEditKpar.setHtml(_translate("Form",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.15</p></body></html>"))
        self.textEditKpar.setPlaceholderText(_translate("Form", "1.15"))
        self.paEtxt_2.setText(_translate("Form", "b="))


