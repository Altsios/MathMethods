# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(272, 384))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radioButtonlin = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonlin.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonlin.setFont(font)
        self.radioButtonlin.setChecked(True)
        self.radioButtonlin.setObjectName("radioButtonlin")
        self.radioButtonlin_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonlin_2.setGeometry(QtCore.QRect(10, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonlin_2.setFont(font)
        self.radioButtonlin_2.setObjectName("radioButtonlin_2")
        self.radioButtonlin_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonlin_3.setGeometry(QtCore.QRect(10, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonlin_3.setFont(font)
        self.radioButtonlin_3.setObjectName("radioButtonlin_3")
        self.pushCh = QtWidgets.QPushButton(self.groupBox)
        self.pushCh.setGeometry(QtCore.QRect(180, 100, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushCh.setFont(font)
        self.pushCh.setObjectName("pushCh")
        self.radioButtonlin_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonlin_4.setGeometry(QtCore.QRect(10, 90, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonlin_4.setFont(font)
        self.radioButtonlin_4.setObjectName("radioButtonlin_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 170, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 151, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 141, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 80, 221, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushCh_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushCh_2.setGeometry(QtCore.QRect(170, 100, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushCh_2.setFont(font)
        self.pushCh_2.setObjectName("pushCh_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ММ(Циось)"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметризированные функции"))
        self.radioButtonlin.setText(_translate("MainWindow", "Линейная"))
        self.radioButtonlin_2.setText(_translate("MainWindow", "Экспоненциальная"))
        self.radioButtonlin_3.setText(_translate("MainWindow", "Кусочная \n"
"(равные части)"))
        self.pushCh.setText(_translate("MainWindow", "Далее"))
        self.radioButtonlin_4.setText(_translate("MainWindow", "4 графика функций"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Случайные числа"))
        self.radioButton.setText(_translate("MainWindow", "Простая генерация"))
        self.radioButton_3.setText(_translate("MainWindow", "Скачки значений"))
        self.radioButton_2.setText(_translate("MainWindow", "Сдвиг значений"))
        self.radioButton_4.setText(_translate("MainWindow", "Анализ последовательности"))
        self.pushCh_2.setText(_translate("MainWindow", "Далее"))

