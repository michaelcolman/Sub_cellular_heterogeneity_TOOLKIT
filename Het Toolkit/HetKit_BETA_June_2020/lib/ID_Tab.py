# Test to see if I can use individual scripts to build a UI

from PyQt5 import QtCore, QtGui, QtWidgets
from lib.Themes import app_dark_mode
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as Toolbar
from matplotlib.widgets import RectangleSelector

def create_tabID(self):

	# NOTE: Text is NOT set within this function. See retranslation.

	# The ID tab is the first thing a user will see
	# It contains a title frame containing information on the toolkit, various links and contact information
	# Users will load / create analysis IDs here and load data using a broswer feature
	# Other than this, it contains shortcuts to the SRF creation feature and a helpful pop up box.


	# Create the tab
	self.tabID = QtWidgets.QWidget()
	self.tabID.setObjectName("tabID")

	# ----- Introduction Frame ----- #

	# Introduction frame creation and settings
	self.frameIntro = QtWidgets.QFrame(self.tabID)
	self.frameIntro.setGeometry(QtCore.QRect(10, 30, 771, 231))
	self.frameIntro.setFrameShape(QtWidgets.QFrame.Box)
	self.frameIntro.setFrameShadow(QtWidgets.QFrame.Raised)
	self.frameIntro.setLineWidth(2)
	self.frameIntro.setObjectName("frameIntro")

	# Label title
	self.labelTitle = QtWidgets.QLabel(self.frameIntro)
	self.labelTitle.setGeometry(QtCore.QRect(10, 10, 621, 51))
	font = QtGui.QFont()
	font.setPointSize(24)
	font.setBold(True)
	font.setWeight(75)
	self.labelTitle.setFont(font)
	self.labelTitle.setObjectName("labelTitle")

	# First of two documentation labels
	self.labelDoc1 = QtWidgets.QLabel(self.frameIntro)
	self.labelDoc1.setGeometry(QtCore.QRect(10, 170, 251, 21))
	font = QtGui.QFont()
	font.setPointSize(11)
	self.labelDoc1.setFont(font)
	self.labelDoc1.setObjectName("labelDoc1")

	# Developer label
	self.labelMaxx = QtWidgets.QLabel(self.frameIntro)
	self.labelMaxx.setGeometry(QtCore.QRect(10, 80, 431, 31))
	font = QtGui.QFont()
	font.setPointSize(13)
	self.labelMaxx.setFont(font)
	self.labelMaxx.setObjectName("labelMaxx")

	# Second of two documentation labels
	self.labelDoc2 = QtWidgets.QLabel(self.frameIntro)
	self.labelDoc2.setGeometry(QtCore.QRect(10, 190, 751, 41))
	font = QtGui.QFont()
	font.setPointSize(11)
	self.labelDoc2.setFont(font)
	self.labelDoc2.setObjectName("labelDoc2")

	# Email correspondance label
	self.labelEmail = QtWidgets.QLabel(self.frameIntro)
	self.labelEmail.setGeometry(QtCore.QRect(10, 110, 401, 31))
	font = QtGui.QFont()
	font.setPointSize(13)
	self.labelEmail.setFont(font)
	self.labelEmail.setObjectName("labelEmail")


	self.graphicsLogo = QtWidgets.QGraphicsView(self.frameIntro)
	self.graphicsLogo.setGeometry(QtCore.QRect(500, 60, 261, 141))
	self.graphicsLogo.setObjectName("graphicsLogo")
	self.logo = QtGui.QPixmap("lib/Images/clean_logo.png")
	self.logo_item = QtWidgets.QGraphicsPixmapItem(self.logo)
	self.logo_scene = QtWidgets.QGraphicsScene()
	self.logo_scene.addItem(self.logo_item)
	self.graphicsLogo.setScene(self.logo_scene)
	self.graphicsLogo.show()

	# ----- ID and Data Frame ----- #

	# Setting up frame for ID and Load Data functions
	self.frameID = QtWidgets.QFrame(self.tabID)
	self.frameID.setGeometry(QtCore.QRect(10, 300, 771, 141))
	self.frameID.setFrameShape(QtWidgets.QFrame.Box)
	self.frameID.setFrameShadow(QtWidgets.QFrame.Raised)
	self.frameID.setLineWidth(2)
	self.frameID.setObjectName("frameID")

	# Label identifing where the user enters ID information 
	self.labelID = QtWidgets.QLabel(self.frameID)
	self.labelID.setGeometry(QtCore.QRect(50, 30, 101, 31))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.labelID.setFont(font)
	self.labelID.setObjectName("labelID")

	# ID entry field
	self.entryID = QtWidgets.QLineEdit(self.frameID)
	self.entryID.setGeometry(QtCore.QRect(160, 30, 371, 32))
	self.entryID.setObjectName("entryID")

	# ID load data button
	self.buttonLoad = QtWidgets.QPushButton(self.frameID)
	self.buttonLoad.setGeometry(QtCore.QRect(560, 30, 151, 31))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonLoad.setFont(font)
	self.buttonLoad.setObjectName("buttonLoad")

	# Label identifying the current data path
	self.labelData = QtWidgets.QLabel(self.frameID)
	self.labelData.setGeometry(QtCore.QRect(50, 90, 91, 31))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.labelData.setFont(font)
	self.labelData.setObjectName("labelData")

	# Label displaying current data path
	self.labelPath = QtWidgets.QLabel(self.frameID)
	self.labelPath.setGeometry(QtCore.QRect(160, 90, 381, 31))
	font = QtGui.QFont()
	font.setPointSize(14)
	font.setItalic(True)
	self.labelPath.setFont(font)
	self.labelPath.setObjectName("labelPath")

	# File dialog button to find data files
	self.buttonBrowse = QtWidgets.QPushButton(self.frameID)
	self.buttonBrowse.setGeometry(QtCore.QRect(560, 90, 151, 31))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonBrowse.setFont(font)
	self.buttonBrowse.setObjectName("buttonBrowse")

	# ----- Buttons ----- #

	# Help button - pressing will bring up a pop-up window
	self.buttonHelp1 = QtWidgets.QPushButton(self.tabID)
	self.buttonHelp1.setGeometry(QtCore.QRect(30, 510, 151, 91))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonHelp1.setFont(font)
	self.buttonHelp1.setObjectName("buttonHelp1")

	# Continue button - pressing will move you to configuration tab (conditional?)
	self.buttonContinue = QtWidgets.QPushButton(self.tabID)
	self.buttonContinue.setGeometry(QtCore.QRect(600, 510, 151, 91))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonContinue.setFont(font)
	self.buttonContinue.setObjectName("buttonContinue")

	# Create SRF button - pressing you moves you to SRF creation tab
	self.buttonCreateSRF = QtWidgets.QPushButton(self.tabID)
	self.buttonCreateSRF.setGeometry(QtCore.QRect(310, 510, 151, 91))
	font = QtGui.QFont()
	font.setPointSize(14)
	self.buttonCreateSRF.setFont(font)
	self.buttonCreateSRF.setObjectName("buttonCreateSRF")

