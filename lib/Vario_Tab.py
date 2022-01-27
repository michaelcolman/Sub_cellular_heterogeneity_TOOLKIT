from PyQt5 import QtCore, QtGui, QtWidgets
from lib.Themes import app_dark_mode
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as Toolbar
from matplotlib.widgets import RectangleSelector

def create_tabVario(self):

	self.tabWidget.addTab(self.tabConfig, "")
	self.tabVario = QtWidgets.QWidget()
	self.tabVario.setObjectName("tabVario")

	# Progress Bar
	self.progressVario = QtWidgets.QProgressBar(self.tabVario)
	self.progressVario.setGeometry(QtCore.QRect(10, 550, 771, 41))
	self.progressVario.setMaximum(100)
	self.progressVario.setProperty("value", 0)
	self.progressVario.setObjectName("progressVario")

	# Graphics widget to display canvas
	self.graphicVario = QtWidgets.QGraphicsView(self.tabVario)
	self.graphicVario.setGeometry(QtCore.QRect(10, 200, 771, 251))
	self.graphicVario.setObjectName("graphicVario")

	# Analysis Settings Frame
	self.frameAnalSetting = QtWidgets.QFrame(self.tabVario)
	self.frameAnalSetting.setGeometry(QtCore.QRect(10, 20, 381, 161))
	self.frameAnalSetting.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameAnalSetting.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameAnalSetting.setLineWidth(2)
	self.frameAnalSetting.setObjectName("frameAnalSetting")

	# Analysis frame title label
	self.labelAnalTitle = QtWidgets.QLabel(self.frameAnalSetting)
	self.labelAnalTitle.setGeometry(QtCore.QRect(20, 10, 201, 20))
	font = QtGui.QFont()
	font.setPointSize(13)
	font.setBold(True)
	font.setUnderline(False)
	font.setWeight(75)
	self.labelAnalTitle.setFont(font)
	self.labelAnalTitle.setObjectName("labelAnalTitle")

	# Bin Count Label
	self.labelBinCount = QtWidgets.QLabel(self.frameAnalSetting)
	self.labelBinCount.setGeometry(QtCore.QRect(20, 40, 121, 20))
	self.labelBinCount.setObjectName("labelBinCount")

	# Bin Size Label
	self.labelBinSize = QtWidgets.QLabel(self.frameAnalSetting)
	self.labelBinSize.setGeometry(QtCore.QRect(20, 70, 121, 20))
	self.labelBinSize.setObjectName("labelBinSize")

	# Bin Count and Bin Label Spin Boxes
	self.spinBC1 = QtWidgets.QSpinBox(self.frameAnalSetting)
	self.spinBC1.setGeometry(QtCore.QRect(180, 40, 62, 21))
	self.spinBC1.setObjectName("spinBC1")
	self.spinBC1.setSingleStep(1)
	self.spinBC1.setMinimum(1)
	self.spinBC1.setMaximum(1000)
	
	self.spinBS1 = QtWidgets.QSpinBox(self.frameAnalSetting)
	self.spinBS1.setGeometry(QtCore.QRect(180, 70, 62, 21))
	self.spinBS1.setObjectName("spinBS1")
	self.spinBS1.setSingleStep(1)
	self.spinBS1.setMinimum(1)
	self.spinBS1.setMaximum(1000)

	self.spinBS2 = QtWidgets.QSpinBox(self.frameAnalSetting)
	self.spinBS2.setGeometry(QtCore.QRect(290, 70, 62, 21))
	self.spinBS2.setObjectName("spinBS2")
	self.spinBS2.setSingleStep(1)
	self.spinBS2.setMinimum(1)
	self.spinBS2.setMaximum(1000)

	self.spinBC2 = QtWidgets.QSpinBox(self.frameAnalSetting)
	self.spinBC2.setGeometry(QtCore.QRect(290, 40, 62, 21))
	self.spinBC2.setObjectName("spinBC2")
	self.spinBC2.setSingleStep(5)
	self.spinBC2.setMinimum(5)
	self.spinBC2.setMaximum(1000)

	# "to" labels between bin spin boxes
	self.labelBCTo = QtWidgets.QLabel(self.frameAnalSetting)
	self.labelBCTo.setGeometry(QtCore.QRect(260, 40, 31, 20))
	self.labelBCTo.setObjectName("labelBCTo")
	self.labelBCto2 = QtWidgets.QLabel(self.frameAnalSetting)
	self.labelBCto2.setGeometry(QtCore.QRect(260, 70, 31, 20))
	self.labelBCto2.setObjectName("labelBCto2")

	# Load VTK Button
	self.buttonLoadVTK = QtWidgets.QPushButton(self.frameAnalSetting)
	self.buttonLoadVTK.setGeometry(QtCore.QRect(20, 110, 191, 41))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonLoadVTK.setFont(font)
	self.buttonLoadVTK.setObjectName("buttonLoadVTK")

	# Output Settings Frame
	self.frameOutput = QtWidgets.QFrame(self.tabVario)
	self.frameOutput.setGeometry(QtCore.QRect(400, 20, 391, 161))
	self.frameOutput.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameOutput.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameOutput.setLineWidth(2)
	self.frameOutput.setMidLineWidth(0)
	self.frameOutput.setObjectName("frameOutput")

	# Output Settings Title Label
	self.labelOutSettings = QtWidgets.QLabel(self.frameOutput)
	self.labelOutSettings.setGeometry(QtCore.QRect(10, 10, 201, 20))
	font = QtGui.QFont()
	font.setPointSize(13)
	font.setBold(True)
	font.setItalic(False)
	font.setUnderline(False)
	font.setWeight(75)
	font.setStrikeOut(False)
	self.labelOutSettings.setFont(font)
	self.labelOutSettings.setObjectName("labelOutSettings")

	# Checkboxes for various output settings.
	self.checkOPDefault = QtWidgets.QCheckBox(self.frameOutput)
	self.checkOPDefault.setGeometry(QtCore.QRect(10, 40, 111, 25))
	self.checkOPDefault.setObjectName("checkOPDefault")
	self.checkOPRotate = QtWidgets.QCheckBox(self.frameOutput)
	self.checkOPRotate.setGeometry(QtCore.QRect(10, 80, 93, 25))
	self.checkOPRotate.setObjectName("checkOPRotate")
	self.checkOPCropped = QtWidgets.QCheckBox(self.frameOutput)
	self.checkOPCropped.setGeometry(QtCore.QRect(120, 80, 93, 25))
	self.checkOPCropped.setObjectName("checkOPCropped")
	self.checkOPDownsample = QtWidgets.QCheckBox(self.frameOutput)
	self.checkOPDownsample.setGeometry(QtCore.QRect(240, 80, 131, 25))
	self.checkOPDownsample.setObjectName("checkOPDownsample")
	self.checkOPVario = QtWidgets.QCheckBox(self.frameOutput)
	self.checkOPVario.setGeometry(QtCore.QRect(190, 120, 101, 25))
	self.checkOPVario.setObjectName("checkOPVario")
	self.checkOPHist = QtWidgets.QCheckBox(self.frameOutput)
	self.checkOPHist.setGeometry(QtCore.QRect(60, 120, 101, 25))
	self.checkOPHist.setObjectName("checkOPHist")

	# Help button for vario tab
	self.buttonHelp3 = QtWidgets.QPushButton(self.tabVario)
	self.buttonHelp3.setGeometry(QtCore.QRect(10, 610, 131, 81))
	font = QtGui.QFont()
	font.setPointSize(15)
	self.buttonHelp3.setFont(font)
	self.buttonHelp3.setObjectName("buttonHelp3")

	# Start Variogram Analysis Button
	self.buttonStartVario = QtWidgets.QPushButton(self.tabVario)
	self.buttonStartVario.setGeometry(QtCore.QRect(10, 470, 771, 71))
	font = QtGui.QFont()
	font.setPointSize(15)
	self.buttonStartVario.setFont(font)
	self.buttonStartVario.setObjectName("buttonStartVario")

	self.buttonContinue3 = QtWidgets.QPushButton(self.tabVario)
	self.buttonContinue3.setGeometry(QtCore.QRect(650, 610, 131, 81))
	font = QtGui.QFont()
	font.setPointSize(15)
	self.buttonContinue3.setFont(font)
	self.buttonContinue3.setObjectName("buttonContinue3")

	self.buttonResults = QtWidgets.QPushButton(self.tabVario)
	self.buttonResults.setGeometry(QtCore.QRect(170, 610, 451, 81))
	font = QtGui.QFont()
	font.setPointSize(15)
	self.buttonResults.setFont(font)
	self.buttonResults.setObjectName("buttonResults")


