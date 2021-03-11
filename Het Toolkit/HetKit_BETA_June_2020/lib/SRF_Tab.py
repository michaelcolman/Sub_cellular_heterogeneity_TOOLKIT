from PyQt5 import QtCore, QtGui, QtWidgets
from lib.Themes import app_dark_mode
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as Toolbar
from matplotlib.widgets import RectangleSelector
from lib.ID_Tab import create_tabID
from lib.Config_Tab import create_tabConfig
from lib.Vario_Tab import create_tabVario

def create_tabSRF(self):

	# Set up SRF tab
	self.tabWidget.addTab(self.tabVario, "")
	self.tabSRF = QtWidgets.QWidget()
	self.tabSRF.setObjectName("tabSRF")

	# SRF Frame Setup	
	self.frameSRF = QtWidgets.QFrame(self.tabSRF)
	self.frameSRF.setGeometry(QtCore.QRect(0, 10, 781, 681))
	self.frameSRF.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameSRF.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameSRF.setLineWidth(2)
	self.frameSRF.setObjectName("frameSRF")

	# SRF Title Label
	self.labelSRFTitle = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFTitle.setGeometry(QtCore.QRect(190, 0, 451, 51))
	font = QtGui.QFont()
	font.setPointSize(20)
	font.setBold(True)
	font.setWeight(75)
	self.labelSRFTitle.setFont(font)
	self.labelSRFTitle.setObjectName("labelSRFTitle")

	# SRF Name Label
	self.labelSRFName = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFName.setGeometry(QtCore.QRect(10, 110, 121, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelSRFName.setFont(font)
	self.labelSRFName.setObjectName("labelSRFName")

	self.labelSRFNum = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFNum.setGeometry(QtCore.QRect(10, 160, 161, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelSRFNum.setFont(font)
	self.labelSRFNum.setObjectName("labelSRFNum")

	self.labelSRFDimensions = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFDimensions.setGeometry(QtCore.QRect(550, 60, 201, 31))
	font = QtGui.QFont()
	font.setPointSize(14)
	font.setUnderline(True)
	self.labelSRFDimensions.setFont(font)
	self.labelSRFDimensions.setObjectName("labelSRFDimensions")

	self.labelSRFDimX = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFDimX.setGeometry(QtCore.QRect(530, 200, 21, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelSRFDimX.setFont(font)
	self.labelSRFDimX.setObjectName("labelSRFDimX")

	self.labelSRFDimY = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFDimY.setGeometry(QtCore.QRect(610, 200, 21, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelSRFDimY.setFont(font)
	self.labelSRFDimY.setObjectName("labelSRFDimY")

	self.labelSRFDimZ = QtWidgets.QLabel(self.frameSRF)
	self.labelSRFDimZ.setGeometry(QtCore.QRect(690, 200, 21, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelSRFDimZ.setFont(font)
	self.labelSRFDimZ.setObjectName("labelSRFDimZ")

	self.SB_SRFDimX = QtWidgets.QSpinBox(self.frameSRF)
	self.SB_SRFDimX.setGeometry(QtCore.QRect(550, 200, 51, 31))
	self.SB_SRFDimX.setObjectName("SB_SRFDimX")
	
	self.SB_SRFDimY = QtWidgets.QSpinBox(self.frameSRF)
	self.SB_SRFDimY.setGeometry(QtCore.QRect(630, 200, 51, 31))
	self.SB_SRFDimY.setObjectName("SB_SRFDimY")
	
	self.SB_SRFDimZ = QtWidgets.QSpinBox(self.frameSRF)
	self.SB_SRFDimZ.setGeometry(QtCore.QRect(710, 200, 51, 31))
	self.SB_SRFDimZ.setObjectName("SB_SRFDimZ")
	
	self.SB_SRFNum = QtWidgets.QSpinBox(self.frameSRF)
	self.SB_SRFNum.setGeometry(QtCore.QRect(180, 160, 91, 32))
	self.SB_SRFNum.setObjectName("SB_SRFNum")
	self.SB_SRFNum.setMinimum(1)
	self.SB_SRFNum.setMaximum(100)

	self.EntrySRFName = QtWidgets.QLineEdit(self.frameSRF)
	self.EntrySRFName.setGeometry(QtCore.QRect(110, 110, 161, 31))
	self.EntrySRFName.setObjectName("lineEdit_7")

	self.buttonGenSRF = QtWidgets.QPushButton(self.frameSRF)
	self.buttonGenSRF.setGeometry(QtCore.QRect(390, 430, 371, 71))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonGenSRF.setFont(font)
	self.buttonGenSRF.setObjectName("pushButton_10")

	self.progressBarSRF = QtWidgets.QProgressBar(self.frameSRF)
	self.progressBarSRF.setGeometry(QtCore.QRect(390, 520, 381, 41))
	self.progressBarSRF.setMaximum(100)
	self.progressBarSRF.setProperty("value", 0)
	self.progressBarSRF.setObjectName("progressBar_2")

	self.CB_SRFFull = QtWidgets.QCheckBox(self.frameSRF)
	self.CB_SRFFull.setGeometry(QtCore.QRect(530, 100, 221, 41))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.CB_SRFFull.setFont(font)
	self.CB_SRFFull.setObjectName("checkBox_4")

	self.CB_SRFPart = QtWidgets.QCheckBox(self.frameSRF)
	self.CB_SRFPart.setGeometry(QtCore.QRect(530, 140, 221, 41))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.CB_SRFPart.setFont(font)
	self.CB_SRFPart.setObjectName("checkBox_5")

	self.line_6 = QtWidgets.QFrame(self.frameSRF)
	self.line_6.setGeometry(QtCore.QRect(270, 50, 20, 261))
	self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
	self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.line_6.setObjectName("line_6")

	self.line_7 = QtWidgets.QFrame(self.frameSRF)
	self.line_7.setGeometry(QtCore.QRect(510, 50, 20, 261))
	self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
	self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.line_7.setObjectName("line_7")

	self.labelLengthscales = QtWidgets.QLabel(self.frameSRF)
	self.labelLengthscales.setGeometry(QtCore.QRect(340, 60, 121, 31))
	font = QtGui.QFont()
	font.setPointSize(16)
	font.setBold(False)
	font.setUnderline(True)
	font.setWeight(50)
	self.labelLengthscales.setFont(font)
	self.labelLengthscales.setObjectName("label_18")

	self.labelLenTransverse = QtWidgets.QLabel(self.frameSRF)
	self.labelLenTransverse.setGeometry(QtCore.QRect(290, 210, 91, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelLenTransverse.setFont(font)
	self.labelLenTransverse.setObjectName("label_19")

	self.labelLenLong = QtWidgets.QLabel(self.frameSRF)
	self.labelLenLong.setGeometry(QtCore.QRect(290, 260, 101, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelLenLong.setFont(font)
	self.labelLenLong.setObjectName("label_20")

	self.buttonUseResults = QtWidgets.QPushButton(self.frameSRF)
	self.buttonUseResults.setGeometry(QtCore.QRect(300, 110, 201, 41))
	font = QtGui.QFont()
	font.setPointSize(13)
	self.buttonUseResults.setFont(font)
	self.buttonUseResults.setObjectName("buttonUseResults")

	self.dSB_Transverse = QtWidgets.QDoubleSpinBox(self.frameSRF)
	self.dSB_Transverse.setGeometry(QtCore.QRect(430, 210, 81, 32))
	self.dSB_Transverse.setObjectName("doubleSpinBox_3")
	self.dSB_Transverse.setMinimum(1.00)
	self.dSB_Transverse.setMaximum(50.00)

	self.dSB_Longitudinal = QtWidgets.QDoubleSpinBox(self.frameSRF)
	self.dSB_Longitudinal.setGeometry(QtCore.QRect(430, 260, 81, 32))
	self.dSB_Longitudinal.setObjectName("doubleSpinBox_4")
	self.dSB_Longitudinal.setMinimum(1.00)
	self.dSB_Longitudinal.setMaximum(50.00)

	self.labelLenCustom = QtWidgets.QLabel(self.frameSRF)
	self.labelLenCustom.setGeometry(QtCore.QRect(300, 170, 201, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelLenCustom.setFont(font)
	self.labelLenCustom.setObjectName("label_21")

	self.graphicSRF = QtWidgets.QGraphicsView(self.frameSRF)
	self.graphicSRF.setGeometry(QtCore.QRect(20, 320, 351, 351))
	self.graphicSRF.setObjectName("graphicsView")

	self.line = QtWidgets.QFrame(self.frameSRF)
	self.line.setGeometry(QtCore.QRect(0, 300, 771, 20))
	self.line.setFrameShape(QtWidgets.QFrame.HLine)
	self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.line.setObjectName("line")

	self.line_3 = QtWidgets.QFrame(self.frameSRF)
	self.line_3.setGeometry(QtCore.QRect(0, 40, 771, 20))
	self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
	self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.line_3.setObjectName("line_3")

	self.buttonGenPreview = QtWidgets.QPushButton(self.frameSRF)
	self.buttonGenPreview.setGeometry(QtCore.QRect(390, 340, 371, 71))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonGenPreview.setFont(font)
	self.buttonGenPreview.setObjectName("pushButton_11")

	self.buttonHelp4 = QtWidgets.QPushButton(self.frameSRF)
	self.buttonHelp4.setGeometry(QtCore.QRect(530, 250, 231, 51))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonHelp4.setFont(font)
	self.buttonHelp4.setObjectName("pushButton_12")

	self.buttonSRFLocation = QtWidgets.QPushButton(self.frameSRF)
	self.buttonSRFLocation.setGeometry(QtCore.QRect(390, 590, 371, 71))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonSRFLocation.setFont(font)
	self.buttonSRFLocation.setObjectName("pushButton_13")

	self.labelOptions = QtWidgets.QLabel(self.frameSRF)
	self.labelOptions.setGeometry(QtCore.QRect(100, 60, 81, 31))
	font = QtGui.QFont()
	font.setPointSize(16)
	font.setBold(False)
	font.setUnderline(True)
	font.setWeight(50)
	self.labelOptions.setFont(font)
	self.labelOptions.setObjectName("label_24")

	self.labelNeighbour = QtWidgets.QLabel(self.frameSRF)
	self.labelNeighbour.setGeometry(QtCore.QRect(10, 210, 171, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelNeighbour.setFont(font)
	self.labelNeighbour.setObjectName("labelNeighbour")

	self.labelMeanExp = QtWidgets.QLabel(self.frameSRF)
	self.labelMeanExp.setGeometry(QtCore.QRect(10, 260, 171, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelMeanExp.setFont(font)
	self.labelMeanExp.setObjectName("labelMeanExp")

	self.SB_NeighbourVar = QtWidgets.QDoubleSpinBox(self.frameSRF)
	self.SB_NeighbourVar.setGeometry(QtCore.QRect(180, 210, 91, 31))
	self.SB_NeighbourVar.setObjectName("SB_NeighbourVar")
	self.SB_NeighbourVar.setValue(0.50)
	self.SB_NeighbourVar.setMinimum(0.00)
	self.SB_NeighbourVar.setMaximum(1.00)

	self.SB_MeanExp = QtWidgets.QDoubleSpinBox(self.frameSRF)
	self.SB_MeanExp.setGeometry(QtCore.QRect(180, 260, 91, 31))
	self.SB_MeanExp.setObjectName("SB_MeanExp")
	self.SB_MeanExp.setValue(1.00)
	self.SB_MeanExp.setMinimum(0.00)
	self.SB_MeanExp.setMaximum(5.00)

	self.tabWidget.addTab(self.tabSRF, "")

