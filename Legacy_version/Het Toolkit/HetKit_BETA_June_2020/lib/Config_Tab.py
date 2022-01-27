from PyQt5 import QtCore, QtGui, QtWidgets
from lib.Themes import app_dark_mode
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as Toolbar
from matplotlib.widgets import RectangleSelector
from lib.ID_Tab import create_tabID

def create_tabConfig(self):

	# Set up configuration tab      
	self.tabWidget.addTab(self.tabID, "")
	self.tabConfig = QtWidgets.QWidget()
	self.tabConfig.setObjectName("tabConfig")

	self.X1 = 0
	self.X2 = 0
	self.Y1 = 0
	self.Y2 = 0

	# ----- Channel Frame -----#

	# Set up RGB frame, which contains channel isolation & switching functionality. 
	self.frameRGB = QtWidgets.QFrame(self.tabConfig)
	self.frameRGB.setGeometry(QtCore.QRect(10, 20, 381, 71))
	self.frameRGB.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameRGB.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameRGB.setLineWidth(2)
	self.frameRGB.setObjectName("frameRGB")

	# RGB frame label
	self.labelRGB = QtWidgets.QLabel(self.frameRGB)
	self.labelRGB.setGeometry(QtCore.QRect(10, 10, 221, 20))
	font = QtGui.QFont()
	font.setPointSize(13)
	font.setBold(True)
	font.setWeight(75)
	self.labelRGB.setFont(font)
	self.labelRGB.setObjectName("labelRGB")

	# RGB radiobuttons (Red/Green/Blue/All)
	self.rbRed = QtWidgets.QRadioButton(self.frameRGB)
	self.rbRed.setGeometry(QtCore.QRect(20, 40, 51, 25))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.rbRed.setFont(font)
	self.rbRed.setObjectName("rbRed")
	self.rbGreen = QtWidgets.QRadioButton(self.frameRGB)
	self.rbGreen.setGeometry(QtCore.QRect(100, 40, 71, 25))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.rbGreen.setFont(font)
	self.rbGreen.setObjectName("rbGreen")
	self.rbBlue = QtWidgets.QRadioButton(self.frameRGB)
	self.rbBlue.setGeometry(QtCore.QRect(200, 40, 61, 25))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.rbBlue.setFont(font)
	self.rbBlue.setObjectName("rbBlue")
	self.rbAll = QtWidgets.QRadioButton(self.frameRGB)
	self.rbAll.setGeometry(QtCore.QRect(290, 40, 61, 25))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.rbAll.setFont(font)
	self.rbAll.setObjectName("rbAll")

	# ----- Cropping Frame ----- #

	# Set up crop frame which contains crop information. Functionality for crop is in the graphics widget.
	self.frameCrop = QtWidgets.QFrame(self.tabConfig)
	self.frameCrop.setGeometry(QtCore.QRect(10, 100, 381, 131))
	self.frameCrop.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameCrop.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameCrop.setLineWidth(2)
	self.frameCrop.setObjectName("frameCrop")

	# Label which titles the crop frame 
	self.labelCropTitle = QtWidgets.QLabel(self.frameCrop)
	self.labelCropTitle.setGeometry(QtCore.QRect(10, 10, 81, 20))
	font = QtGui.QFont()
	font.setPointSize(13)
	font.setBold(True)
	font.setWeight(75)
	self.labelCropTitle.setFont(font)
	self.labelCropTitle.setObjectName("labelCropTitle")

	# Label giving instruction on how to set a crop region
	self.labelCrop = QtWidgets.QLabel(self.frameCrop)
	self.labelCrop.setGeometry(QtCore.QRect(40, 40, 291, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelCrop.setFont(font)
	self.labelCrop.setObjectName("labelCrop")

	# Label giving crop co-ordinate information. This is saved as a variable.
	self.labelCoords = QtWidgets.QLabel(self.frameCrop)
	self.labelCoords.setGeometry(QtCore.QRect(40, 70, 291, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelCoords.setFont(font)
	self.labelCoords.setObjectName("labelCoords")

	# Set up graphics widget
	self.graphicConfig = QtWidgets.QGraphicsView(self.tabConfig)
	self.graphicConfig.setGeometry(QtCore.QRect(0, 290, 801, 441))
	self.graphicConfig.setObjectName("graphicConfig")

	# ----- Downsampling Frame ----- #

	# Set up downsampling frame, which contains downsampling functionality
	self.frameDownsample = QtWidgets.QFrame(self.tabConfig)
	self.frameDownsample.setGeometry(QtCore.QRect(400, 100, 381, 131))
	self.frameDownsample.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameDownsample.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameDownsample.setLineWidth(2)
	self.frameDownsample.setObjectName("frameDownsample")

	# Label for DS frame title.
	self.labelDS = QtWidgets.QLabel(self.frameDownsample)
	self.labelDS.setGeometry(QtCore.QRect(10, -1, 141, 31))
	font = QtGui.QFont()
	font.setPointSize(13)
	font.setBold(True)
	font.setWeight(75)
	self.labelDS.setFont(font)
	self.labelDS.setObjectName("labelDS")

	# Labels and Entries for downsampling functionality.        
	self.entryY1 = QtWidgets.QLineEdit(self.frameDownsample)
	self.entryY1.setGeometry(QtCore.QRect(70, 90, 113, 32))
	self.entryY1.setObjectName("entryY1")
	self.entryX1 = QtWidgets.QLineEdit(self.frameDownsample)
	self.entryX1.setGeometry(QtCore.QRect(70, 50, 113, 32))
	self.entryX1.setObjectName("entryX1")
	self.entryX2 = QtWidgets.QLineEdit(self.frameDownsample)
	self.entryX2.setGeometry(QtCore.QRect(250, 50, 113, 32))
	self.entryX2.setObjectName("entryX2")
	self.entryY2 = QtWidgets.QLineEdit(self.frameDownsample)
	self.entryY2.setGeometry(QtCore.QRect(250, 90, 113, 32))
	self.entryY2.setObjectName("entryY2")
	self.labelDSImage = QtWidgets.QLabel(self.frameDownsample)
	self.labelDSImage.setGeometry(QtCore.QRect(90, 30, 91, 20))
	self.labelDSImage.setObjectName("labelDSImage")
	self.labelDSNew = QtWidgets.QLabel(self.frameDownsample)
	self.labelDSNew.setGeometry(QtCore.QRect(250, 30, 111, 20))
	self.labelDSNew.setObjectName("labelDSNew")
	self.labelDSX1 = QtWidgets.QLabel(self.frameDownsample)
	self.labelDSX1.setGeometry(QtCore.QRect(10, 50, 62, 31))
	self.labelDSX1.setObjectName("labelDSX1")
	self.labelDSX2 = QtWidgets.QLabel(self.frameDownsample)
	self.labelDSX2.setGeometry(QtCore.QRect(190, 50, 62, 31))
	self.labelDSX2.setObjectName("labelDSX2")
	self.labelDSY2 = QtWidgets.QLabel(self.frameDownsample)
	self.labelDSY2.setGeometry(QtCore.QRect(190, 90, 62, 31))
	self.labelDSY2.setObjectName("labelDSY2")
	self.labelDSY1 = QtWidgets.QLabel(self.frameDownsample)
	self.labelDSY1.setGeometry(QtCore.QRect(10, 90, 62, 31))
	self.labelDSY1.setObjectName("labelDSY1")

	# ----- Rotation Frame ----- #

	# Set up rotation frame which contains rotation functionality.
	self.frameRotate = QtWidgets.QFrame(self.tabConfig)
	self.frameRotate.setGeometry(QtCore.QRect(400, 20, 381, 71))
	self.frameRotate.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameRotate.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameRotate.setLineWidth(2)
	self.frameRotate.setObjectName("frameRotate")

	# Label which titles rotational frame
	self.labelRotate = QtWidgets.QLabel(self.frameRotate)
	self.labelRotate.setGeometry(QtCore.QRect(10, 10, 151, 20))
	font = QtGui.QFont()
	font.setPointSize(13)
	font.setBold(True)
	font.setWeight(75)
	self.labelRotate.setFont(font)
	self.labelRotate.setObjectName("labelRotate")

	# Spinbox for selecting degrees of rotation
	self.spinDegrees = QtWidgets.QSpinBox(self.frameRotate)
	self.spinDegrees.setGeometry(QtCore.QRect(160, 30, 71, 31))
	self.spinDegrees.setObjectName("spinDegrees")
	self.spinDegrees.setMinimum(-360)
	self.spinDegrees.setMaximum(360)

	# Label for degree selection
	self.labelDegrees = QtWidgets.QLabel(self.frameRotate)
	self.labelDegrees.setGeometry(QtCore.QRect(10, 29, 161, 31))
	font = QtGui.QFont()
	font.setPointSize(12)
	self.labelDegrees.setFont(font)
	self.labelDegrees.setObjectName("labelDegrees")

	# Rotation Button
	self.buttonRotate = QtWidgets.QPushButton(self.frameRotate)
	self.buttonRotate.setGeometry(QtCore.QRect(250, 30, 111, 31))
	self.buttonRotate.setObjectName("ButtonRotate")

	# ----- Buttons ----- #

	# Help Button -> Produces pop-up window with tab information
	self.buttonHelp2 = QtWidgets.QPushButton(self.tabConfig)
	self.buttonHelp2.setGeometry(QtCore.QRect(440, 240, 71, 41))
	self.buttonHelp2.setObjectName("buttonHelp2")

	# Reset Button -> Resets image to original state
	self.buttonReset = QtWidgets.QPushButton(self.tabConfig)
	self.buttonReset.setGeometry(QtCore.QRect(520, 240, 71, 41))
	self.buttonReset.setObjectName("buttonReset")

	# Apply Button -> Applys all channel, rotation, crop and downsampling settings to original image.
	self.buttonApply = QtWidgets.QPushButton(self.tabConfig)
	self.buttonApply.setGeometry(QtCore.QRect(600, 240, 71, 41))
	self.buttonApply.setObjectName("buttonApply")

	# Continue Button -> Save all settings and proceed to variogram analysis tab
	self.buttonContinue2 = QtWidgets.QPushButton(self.tabConfig)
	self.buttonContinue2.setGeometry(QtCore.QRect(680, 240, 101, 41))
	self.buttonContinue2.setObjectName("buttonContinue2")

	# ----- Image Stack Frame ----- #

	# Sets up the stack frame, which includes stack-based processing functionality.
	self.frameStack = QtWidgets.QFrame(self.tabConfig)
	self.frameStack.setGeometry(QtCore.QRect(10, 240, 421, 41))
	self.frameStack.setFrameShape(QtWidgets.QFrame.Panel)
	self.frameStack.setFrameShadow(QtWidgets.QFrame.Sunken)
	self.frameStack.setLineWidth(2)
	self.frameStack.setObjectName("frameStack")

	# Label for stack frame
	self.labelStack = QtWidgets.QLabel(self.frameStack)
	self.labelStack.setGeometry(QtCore.QRect(10, 0, 201, 41))
	font = QtGui.QFont()
	font.setPointSize(13)
	self.labelStack.setFont(font)
	self.labelStack.setObjectName("labelStack")

	# Slider to choose which image to display from a stack
	self.sliderStack = QtWidgets.QSlider(self.frameStack)
	self.sliderStack.setGeometry(QtCore.QRect(220, 0, 191, 41))
	self.sliderStack.setMaximum(10)
	self.sliderStack.setOrientation(QtCore.Qt.Horizontal)
	self.sliderStack.setObjectName("sliderStack")

