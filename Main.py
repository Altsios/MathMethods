# -*- coding: utf-8 -*-
import sys
from form import *
from linear import *
from Model import *
from InOut import *
from partwin import *
from rand import *
from fgr import *
from spik import *
from Analysis import *

from PyQt5.QtWidgets import  QVBoxLayout,QLabel,QGridLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.pyplot import figure

def limx(slim1,slim2,s,e,ee):
    try:
        lim1, lim2 = float(slim1), float(slim2)
    except ValueError:
        lim1, lim2 = None, None

    x = np.arange(s,e,ee)

    return lim1,lim2,x

class MyGrsWin(QtWidgets.QDialog):
    def __init__(self, parent=None,func=None,opt=[0,10]):
        super(MyGrsWin, self).__init__(parent)

        self.figure = figure(num=2,figsize=(50, 5))
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout(self)

        self.font = QtGui.QFont()
        self.font.setPointSize(11)
        self.font.setBold(True)
        self.font.setUnderline(False)
        self.font.setWeight(75)


        self.label = QLabel("*",self)


        self.label.setFont(self.font)
        self.label.setObjectName("label")


        self.layout.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.canvas)



        self.setWindowTitle('Анализ')
        self.Calc(func, opt)

    def Calc(self,func,opt):

        self.font.setBold(False)
        self.font.setPointSize(11)
        if  opt[0]==0:
            self.labeltxt = QLabel("*", self)
            self.labeltxt.setFont(self.font)
            self.labeltxt.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.labeltxt)

            self.labeltxt.setObjectName("labeltxt")

            self.label.setText("Стационарность")
            if Stationarity(func,opt[1]):

                self.labeltxt.setText("Процесс стационарен!")
            else:
                self.labeltxt.setText("Процесс не стационарен!")
        else:
            self.label.setText("Статистика")
            positions = [(i, j) for i in range(4) for j in range(6)]
            values=Statisticks(func)
            grid = QGridLayout()

            for position, val in zip(positions,values):
                label=QLabel(str(val))
                label.setFont(self.font)
                if(position[1])%2!=0:
                    label.setStyleSheet("background-color: #ffffff")
                else:
                    label.setStyleSheet("background-color: #D3D3D3")
                grid.addWidget(label,*position)

            self.layout.addLayout(grid)
        self.MyPlot(func)

    def MyPlot(self,f):

        ax = self.figure.add_subplot(111)
        ax.grid(True)
        ax.plot(f.x,f.y,linewidth=1,alpha=0.7,color='b')
        self.canvas.draw()

#анализ
class AnlsWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_anls()
        self.ui.setupUi(self)
        self.ui.linbutt.clicked.connect(self.Show)

    def Show(self):

        lim1,lim2,x=limx(self.ui.lim1.toPlainText(), self.ui.lim2.toPlainText(),
                         float(self.ui.textEditSpar.toPlainText()),
                         float(self.ui.textEditEpar.toPlainText()),
                         float(self.ui.textEditEEpar.toPlainText()))

        if self.ui.radioButton.isChecked():
            fr=Rand(x,  float(self.ui.textEditEEpar_2.toPlainText()),tit="Исходная последовательность")
        else:
            fr =SelfRandom(x, float(self.ui.textEditEEpar_2.toPlainText()),tit="Исходная последовательность")

        if self.ui.radioButton_3.isChecked():
            grWin = MyGrsWin(self,fr,[0,int(self.ui.intlim.toPlainText())])
            grWin.show()
        elif self.ui.radioButton_4.isChecked():
            grWin = MyGrsWin(self, fr, [1,int(self.ui.intlim.toPlainText())])
            grWin.show()
        elif self.ui.radioButton_5.isChecked():
            Barf(fr.y,int(self.ui.intlim.toPlainText()),tit='Плотность вероятности')
        else:
            Barf(Disp(fr.y,int(self.ui.intlim.toPlainText())),notmy=False,tit='Плотность вероятности')

#разброс
class SpikWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Ui_spik()
        self.ui.setupUi(self)
        self.ui.linbutt.clicked.connect(self.Show)

    def Show(self):

        lim1,lim2,x=limx(self.ui.lim1.toPlainText(), self.ui.lim2.toPlainText(),
                         float(self.ui.textEditSpar.toPlainText()),
                         float(self.ui.textEditEpar.toPlainText()),
                         float(self.ui.textEditEEpar.toPlainText()))

        if self.ui.radioButton.isChecked():
            fr=Rand(x,  float(self.ui.textEditEEpar_2.toPlainText()))
        else:
            fr =SelfRandom(x, float(self.ui.textEditEEpar_2.toPlainText()))

        plotF(fr.Spikes(float(self.ui.lim1_2.toPlainText()),
                   float(self.ui.lim1_3.toPlainText()),
                   float(self.ui.lim1_4.toPlainText())),tit="Выбросы",lim=[lim1, lim2] if lim1 is not None and lim2 is not None else None)


#сдвиг
class Shift(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_rand()
        self.ui.setupUi(self)
        self.ui.radioButton_3.deleteLater()
        self.ui.label.setText("Сдвиг")
        self.ui.frame.setGeometry(QtCore.QRect(140, 70, 151, 41))
        self.ui.label.setGeometry(QtCore.QRect(130, 10, 141, 21))
        self.ui.label_3 = QtWidgets.QLabel(self.ui.centralwidget)
        self.ui.label_3 = QtWidgets.QLabel(self.ui.centralwidget)
        self.ui.label_3.setGeometry(QtCore.QRect(140, 122, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ui.label_3.setFont(font)
        self.ui.label_3.setObjectName("label_3")
        self.ui.label_3.setText("Сдвиг=")
        self.ui.textlim= QtWidgets.QTextEdit(self.ui.centralwidget)
        self.ui.textlim.setGeometry(QtCore.QRect(210, 120, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ui.textlim.setFont(font)
        self.ui.textlim.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.textlim.setUndoRedoEnabled(True)
        self.ui.textlim.setAcceptRichText(True)
        self.ui.textlim.setObjectName("textlim")
        self.ui.textlim.setText("1.5")
        self.ui.textlim.setPlaceholderText("1.5")

        self.ui.linbutt.clicked.connect(self.Show)

    def Show(self):

        lim1,lim2,x=limx(self.ui.lim1.toPlainText(), self.ui.lim2.toPlainText(),
                         float(self.ui.textEditSpar.toPlainText()),
                         float(self.ui.textEditEpar.toPlainText()),
                         float(self.ui.textEditEEpar.toPlainText()))

        sht=float(self.ui.textlim.toPlainText())
            # Проверка выбранного
        if self.ui.radioButton.isChecked():
            fr=Rand(x,  float(self.ui.textEditEEpar_2.toPlainText()),tit="Исходная последовательность")
        else:
            fr =SelfRandom(x, float(self.ui.textEditEEpar_2.toPlainText()),tit="Исходная последовательность")

        frs = Dummy()
        frs.CopyShift(fr,sht)

        frsmin=min(frs.y)
        frsmax = max(frs.y)
        mmin = min(fr.y)
        mmax = max(fr.y)

        if frsmin<mmin:
            mmin=frsmin
        if frsmax>mmax:
            mmax=frsmax

        subplotFs([fr,frs], 2, 1,
                  lim=[lim1, lim2] if lim1 is not None and lim2 is not None else None,
                  ylim=[mmin,mmax])

# график случайных чисел
class Rseq(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_rand()
        self.ui.setupUi(self)
        self.ui.linbutt.clicked.connect(self.Show)

    def Show(self):

        lim1,lim2,x=limx(self.ui.lim1.toPlainText(), self.ui.lim2.toPlainText(),
                         float(self.ui.textEditSpar.toPlainText()),
                         float(self.ui.textEditEpar.toPlainText()),
                         float(self.ui.textEditEEpar.toPlainText()))

            # Проверка выбранного
        if self.ui.radioButton.isChecked():
            plotF(Rand(x,
                       float(self.ui.textEditEEpar_2.toPlainText())), tit='Встроенный генератор',
                  lim=[lim1, lim2] if lim1 is not None and lim2 is not None else None)

        elif self.ui.radioButton_2.isChecked():
            plotF(SelfRandom(x,
                       float(self.ui.textEditEEpar_2.toPlainText())), tit='Свой генератор',
                  lim=[lim1, lim2] if lim1 is not None and lim2 is not None else None)

        else:
            subplotFs([Rand(x,
                       float(self.ui.textEditEEpar_2.toPlainText())),
            SelfRandom(x,float(self.ui.textEditEEpar_2.toPlainText())) ],2,1,
                      lim=[lim1, lim2] if lim1 is not None and lim2 is not None else None)

# 4 графика
class Fgr(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = FgrWindow()
        self.ui.setupUi(self)
        self.ui.make.clicked.connect(self.Show)

    def Show(self):
        x=np.arange(float(self.ui.textEditSpar.toPlainText())
                                ,float(self.ui.textEditEpar.toPlainText()),
                                float(self.ui.textEditEEpar.toPlainText()))
        subplotFs([LinearF(x,
                      float(self.ui.textEditk1.toPlainText()),
                      float(self.ui.textEditb1.toPlainText()),self.ui.textEditSpar_2.toPlainText()),
                   LinearF(x,
                           float(self.ui.textEditk2.toPlainText()),
                           float(self.ui.textEditb2.toPlainText()),self.ui.textEditSpar_3.toPlainText()),
                   ExpF(x,float(self.ui.textEdita1.toPlainText()),self.ui.textEditSpar_4.toPlainText()),
                   ExpF(x, float(self.ui.textEdita2.toPlainText()),self.ui.textEditSpar_5.toPlainText())
                   ], 2, 2)

#Смешанная функция

class CompF(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_PartWin()
        self.ui.setupUi(self)
        self.ui.linbutt.clicked.connect(self.Show)

    def Show(self):
        s=float(self.ui.textEditSpar.toPlainText())
        e=float(self.ui.textEditEpar.toPlainText())
        plotF(CmpsF(np.arange(s,e,float(self.ui.textEditEEpar.toPlainText())),
                    s,e,
                      float(self.ui.textEditKpar.toPlainText()),
                      float(self.ui.textEditEpar_2.toPlainText()),
                      float(self.ui.textEditKpar_2.toPlainText()),
                      float(self.ui.textEditEpar_3.toPlainText()),
                      float(self.ui.textEditKpar_3.toPlainText()),
                      float(self.ui.textEditEpar_4.toPlainText()),
                      float(self.ui.textEditKpar_5.toPlainText()),
                      float(self.ui.textEditEpar_5.toPlainText()),
                      float(self.ui.textEditKpar_4.toPlainText()),
                      float(self.ui.textEditEpar_6.toPlainText())),
              "Задание *")

#Экспонента

class CexpF(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.paEtxt_2.deleteLater()
        self.ui.textEditEpar_2.deleteLater()
        self.ui.label.setText("y=e^a")
        self.ui.parktxt.setText("a=")
        self.ui.textEditKpar.setText("5")
        self.ui.textEditKpar.setPlaceholderText("5")

        self.ui.linbutt.clicked.connect(self.Show)

    def Show(self):
        plotF(ExpF(np.arange(float(self.ui.textEditSpar.toPlainText())
                                ,float(self.ui.textEditEpar.toPlainText()),
                                float(self.ui.textEditEEpar.toPlainText())),
                      float(self.ui.textEditKpar.toPlainText())),
              "Экспоненциальная функция")

#Линейная функция

class LinF(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.linbutt.clicked.connect(self.Show)


    def Show(self):
        plotF(LinearF(np.arange(float(self.ui.textEditSpar.toPlainText())
                                ,float(self.ui.textEditEpar.toPlainText()),
                                float(self.ui.textEditEEpar.toPlainText())),
                      float(self.ui.textEditKpar.toPlainText()),
                      float(self.ui.textEditEpar_2.toPlainText())),
              "Линейная функция")

# Главное окно
class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #окна
        self.linf= LinF(self)
        self.expf = CexpF(self)
        self.ptwin=CompF(self)
        self.fwin=Fgr(self)
        self.rwin= Rseq(self)
        self.shiftw=Shift(self)
        self.spikewin=SpikWin(self)
        self.awin=AnlsWin(self)

        #кнопки
        self.ui.pushCh.clicked.connect(self.ClickGr)
        self.ui.pushCh_2.clicked.connect(self.ClickRand)

    def ClickRand(self):
        if self.ui.radioButton.isChecked():
            self.rwin.show()
        elif self.ui.radioButton_2.isChecked():
            self.shiftw.show()
        elif self.ui.radioButton_3.isChecked():
            self.spikewin.show()
        elif self.ui.radioButton_4.isChecked():
            self.awin.show()

    def ClickGr(self):

        # Проверка выбранного
        if self.ui.radioButtonlin.isChecked():
            self.linf.show()
        elif self.ui.radioButtonlin_2.isChecked():
            self.expf.show()
        elif self.ui.radioButtonlin_3.isChecked():
            self.ptwin.show()
        else:
            self.fwin.show()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
