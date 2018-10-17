# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Analysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import math

def Stint(x,N):
    _x = sum(x) / N
    D = sum([(xk - _x) ** 2 for xk in x]) / N
    return _x,D

def Stationarity(f,M):

    splitted=np.array_split(f.y,M)

    for inter in splitted:
        _x,D=Stint(inter,M)
        #отличаются
        if abs((_x-D)/((_x+D)/2))>0.02:
            return False

    return True

def Statisticks(f):

    N=len(f.y)
    # Среднее+дисперсия
    _x,D=Stint(f.y,N)
    # мин и максимум
    miny,maxy=min(f.y),max(f.y)
    # стандт. откл.
    stdv=math.sqrt(D)
    # среднее квадратическое
    sk=sum([(xk) ** 2 for xk in f.y])/N
    #ско
    sko=math.sqrt(sk)
    #ассиметрия
    assi = sum([(xk-_x) ** 3 for xk in f.y]) / N
    #Коэффициент симметрии
    kassi=assi/stdv**3
    # эксцесс
    ex = sum([(xk - _x) ** 4 for xk in f.y]) / N
    # Коэффициент эксцесса
    ekx = assi / ex ** 4-3

    return ["Минимум",miny,"Максимум",maxy,"Среднее значение",_x, "Дисперсия",D,
            "Стандартное отклонение ",stdv,"Среднее квадратическое",sk,
            "Среднее квадратическое отклонение ",sko,"Ассиметрия",assi ,"Коэффициент симметрии",kassi,
    "Эксцесс",ex ,"Коэффициент эксцесса",ekx ]


def Disp(y, k):
    kcnt = []
    lbnds = []

    # число интервалов группировки k
    # Величина интервала группировки h
    # min и max
    miny, maxy = min(y), max(y)
    h = (maxy - miny) /k

    lbnds.append(miny)
    for i in range(0, k):
        # опред. след границы
        lbnds.append(lbnds[i] + h)
        # запись количества y между ними
        kcnt.append(0)
        for yk in y:
            if yk >= lbnds[i] and yk < lbnds[i + 1]:
                kcnt[i] += 1

    kcnt.append(kcnt[-1])
    return [kcnt, lbnds]


class  Ui_anls(object):
    def setupUi(self, Ui_spik):
        Ui_spik.setObjectName("Ui_spik")
        Ui_spik.resize(354, 276)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_spik.sizePolicy().hasHeightForWidth())
        Ui_spik.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Ui_spik)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 122, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.parStxt = QtWidgets.QLabel(self.centralwidget)
        self.parStxt.setGeometry(QtCore.QRect(20, 44, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parStxt.setFont(font)
        self.parStxt.setObjectName("parStxt")
        self.parEtxt = QtWidgets.QLabel(self.centralwidget)
        self.parEtxt.setGeometry(QtCore.QRect(20, 64, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parEtxt.setFont(font)
        self.parEtxt.setObjectName("parEtxt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.linbutt = QtWidgets.QPushButton(self.centralwidget)
        self.linbutt.setGeometry(QtCore.QRect(140, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.linbutt.setFont(font)
        self.linbutt.setObjectName("linbutt")
        self.textEditSpar = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSpar.setGeometry(QtCore.QRect(70, 44, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditSpar.setFont(font)
        self.textEditSpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditSpar.setDocumentTitle("")
        self.textEditSpar.setUndoRedoEnabled(True)
        self.textEditSpar.setOverwriteMode(False)
        self.textEditSpar.setAcceptRichText(True)
        self.textEditSpar.setObjectName("textEditSpar")
        self.textEditEpar = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEpar.setGeometry(QtCore.QRect(70, 70, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditEpar.setFont(font)
        self.textEditEpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditEpar.setUndoRedoEnabled(True)
        self.textEditEpar.setAcceptRichText(True)
        self.textEditEpar.setObjectName("textEditEpar")
        self.parEEtxt = QtWidgets.QLabel(self.centralwidget)
        self.parEEtxt.setGeometry(QtCore.QRect(30, 96, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parEEtxt.setFont(font)
        self.parEEtxt.setObjectName("parEEtxt")
        self.textEditEEpar = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEEpar.setGeometry(QtCore.QRect(70, 96, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditEEpar.setFont(font)
        self.textEditEEpar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditEEpar.setUndoRedoEnabled(True)
        self.textEditEEpar.setAcceptRichText(True)
        self.textEditEEpar.setObjectName("textEditEEpar")
        self.lim2 = QtWidgets.QTextEdit(self.centralwidget)
        self.lim2.setGeometry(QtCore.QRect(70, 148, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lim2.setFont(font)
        self.lim2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lim2.setUndoRedoEnabled(True)
        self.lim2.setAcceptRichText(True)
        self.lim2.setObjectName("lim2")
        self.lim1 = QtWidgets.QTextEdit(self.centralwidget)
        self.lim1.setGeometry(QtCore.QRect(70, 122, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lim1.setFont(font)
        self.lim1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lim1.setUndoRedoEnabled(True)
        self.lim1.setAcceptRichText(True)
        self.lim1.setObjectName("lim1")
        self.textEditEEpar_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditEEpar_2.setGeometry(QtCore.QRect(210, 44, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEditEEpar_2.setFont(font)
        self.textEditEEpar_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditEEpar_2.setUndoRedoEnabled(True)
        self.textEditEEpar_2.setAcceptRichText(True)
        self.textEditEEpar_2.setObjectName("textEditEEpar_2")
        self.parEEtxt_2 = QtWidgets.QLabel(self.centralwidget)
        self.parEEtxt_2.setGeometry(QtCore.QRect(140, 44, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parEEtxt_2.setFont(font)
        self.parEEtxt_2.setObjectName("parEEtxt_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 70, 191, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(5, 0, 141, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(5, 20, 141, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(140, 120, 191, 81))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(5, 0, 141, 17))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(5, 20, 141, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_5.setGeometry(QtCore.QRect(5, 40, 181, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_6.setGeometry(QtCore.QRect(5, 60, 191, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 164, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.intlim = QtWidgets.QTextEdit(self.centralwidget)
        self.intlim.setGeometry(QtCore.QRect(70, 174, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.intlim.setFont(font)
        self.intlim.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.intlim.setUndoRedoEnabled(True)
        self.intlim.setAcceptRichText(True)
        self.intlim.setObjectName("intlim")
        Ui_spik.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_spik)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 21))
        self.menubar.setObjectName("menubar")
        Ui_spik.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_spik)
        self.statusbar.setObjectName("statusbar")
        Ui_spik.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_spik)
        QtCore.QMetaObject.connectSlotsByName(Ui_spik)

    def retranslateUi(self, Ui_spik):
        _translate = QtCore.QCoreApplication.translate
        Ui_spik.setWindowTitle(_translate("Ui_spik", "Параметры"))
        self.label_2.setText(_translate("Ui_spik", "Пределы"))
        self.parStxt.setText(_translate("Ui_spik", "Старт="))
        self.parEtxt.setText(_translate("Ui_spik", "Конец="))
        self.label.setText(_translate("Ui_spik", "Анализ последовательности"))
        self.linbutt.setText(_translate("Ui_spik", "ОК"))
        self.textEditSpar.setHtml(_translate("Ui_spik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textEditSpar.setPlaceholderText(_translate("Ui_spik", "0"))
        self.textEditEpar.setHtml(_translate("Ui_spik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1000</p></body></html>"))
        self.textEditEpar.setPlaceholderText(_translate("Ui_spik", "1000"))
        self.parEEtxt.setText(_translate("Ui_spik", "Шаг="))
        self.textEditEEpar.setHtml(_translate("Ui_spik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.textEditEEpar.setPlaceholderText(_translate("Ui_spik", "1"))
        self.lim2.setPlaceholderText(_translate("Ui_spik", "None"))
        self.lim1.setPlaceholderText(_translate("Ui_spik", "None"))
        self.textEditEEpar_2.setHtml(_translate("Ui_spik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.textEditEEpar_2.setPlaceholderText(_translate("Ui_spik", "1"))
        self.parEEtxt_2.setText(_translate("Ui_spik", "Масштаб="))
        self.radioButton.setText(_translate("Ui_spik", "Встроенный генератор"))
        self.radioButton_2.setText(_translate("Ui_spik", "Свой генератор"))
        self.radioButton_3.setText(_translate("Ui_spik", "Стационарность"))
        self.radioButton_4.setText(_translate("Ui_spik", "Статистики"))
        self.radioButton_5.setText(_translate("Ui_spik", "Плотность вероятности (встр.)"))
        self.radioButton_6.setText(_translate("Ui_spik", "Плотность вероятности (св. ф.)"))
        self.label_3.setText(_translate("Ui_spik", "Кол-во \n"
" инт-в"))
        self.intlim.setHtml(_translate("Ui_spik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.intlim.setPlaceholderText(_translate("Ui_spik", "10"))

