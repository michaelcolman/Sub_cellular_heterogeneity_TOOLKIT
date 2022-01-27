import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from lib.Canvas import *
from lib.CanvasVario import *
from lib.CanvasSRF import *
from lib.SRF import *
from lib.channels import channel_splitter
from lib.cropping import crop_data
from lib.rotation import rotate_data
from lib.downsample import downsample_data
from lib.database import *

def open_webbrowser_config():
	webbrowser.open("https://github.com/MaxxHolmes/HetKit")

def rotate_button(self, mainUI, canvas):

	# Get Rotation Value

	mainUI.showData = np.asarray(mainUI.data)
	channel_radio(self, mainUI, canvas)
	degreesValue = mainUI.spinDegrees.value()
	mainUI.showData = rotate_data(mainUI.showData, degreesValue)	
	canvas.replot_showData(mainUI)

def channel_radio(self, mainUI, canvas):

	# Get channel value

	mainUI.showData = np.asarray(mainUI.data)

	if mainUI.rbRed.isChecked():
		mainUI.channelValue = "Red"
	elif mainUI.rbGreen.isChecked():
		mainUI.channelValue = "Green"
	elif mainUI.rbBlue.isChecked():
		mainUI.channelValue = "Blue"
	elif mainUI.rbAll.isChecked():
		mainUI.channelValue = "None"
	else:
		mainUI.channelValue = "None"

	mainUI.showData = channel_splitter(mainUI.showData, mainUI.channelValue)
	canvas.replot_showData(mainUI)

def apply_button(self, mainUI, canvas):

	# Get Channel Value

	if mainUI.rbRed.isChecked():
		mainUI.channelValue = "Red"
	elif mainUI.rbGreen.isChecked():
		mainUI.channelValue = "Green"
	elif mainUI.rbBlue.isChecked():
		mainUI.channelValue = "Blue"
	elif mainUI.rbAll.isChecked():
		mainUI.channelValue = "None"
	else:
		mainUI.channelValue = "None"

	# Get Rotation Value

	degreesValue = mainUI.spinDegrees.value()

	# Get Downsampling Values

	try:
		DSImageX = float(mainUI.entryX1.text())
		DSImageY = float(mainUI.entryY1.text())
		DSNewX = float(mainUI.entryX2.text())
		DSNewY = float(mainUI.entryY2.text())

	except:
		DSImageX = 1.0
		DSImageY = 1.0
		DSNewX = 1.0
		DSNewY = 1.0

	# Get Crop Values
	try:
		mainUI.X1 = int(canvas.x1)
		mainUI.X2 = int(canvas.x2)
		mainUI.Y1 = int(canvas.y1)
		mainUI.Y2 = int(canvas.y2)
	except:
		mainUI.X1 = 1.0
		mainUI.X2 = 1.0
		mainUI.Y1 = 1.0
		mainUI.Y2 = 1.0

	current_data = np.asarray(mainUI.data)
	current_data = channel_splitter(current_data, mainUI.channelValue)
	current_data = rotate_data(current_data, degreesValue)
	current_data = crop_data(current_data, mainUI.X1, mainUI.X2, mainUI.Y1, mainUI.Y2)
	current_data = downsample_data(current_data, DSNewX, DSNewY, DSImageX, DSImageY)

	mainUI.newData = current_data
	canvas.replot_apply(mainUI)
	mainUI.labelCoords.setText("Co-ordinates:	({}, {}), ({}, {})".format(mainUI.X1, mainUI.Y1, mainUI.X2, mainUI.Y2))

	mainUI.DB[mainUI.ID]["Channel"] = mainUI.channelValue
	mainUI.DB[mainUI.ID]["Rotation Angle"] = mainUI.spinDegrees.value()

	mainUI.DB[mainUI.ID]["Crop X1"] = int(mainUI.X1)
	mainUI.DB[mainUI.ID]["Crop X2"] = int(mainUI.X2)
	mainUI.DB[mainUI.ID]["Crop Y1"] = int(mainUI.Y1)
	mainUI.DB[mainUI.ID]["Crop Y2"] = int(mainUI.Y2)

	try:
		mainUI.DB[mainUI.ID]["Scale X"] = float(mainUI.entryX1.text())
		mainUI.DB[mainUI.ID]["Scale Y"] = float(mainUI.entryY1.text())
		mainUI.DB[mainUI.ID]["Downsample X"] = float(mainUI.entryX2.text())
		mainUI.DB[mainUI.ID]["Downsample Y"] = float(mainUI.entryY2.text())
	except:
		mainUI.DB[mainUI.ID]["Scale X"] = 1.0
		mainUI.DB[mainUI.ID]["Scale Y"] = 1.0
		mainUI.DB[mainUI.ID]["Downsample X"] = 1.0
		mainUI.DB[mainUI.ID]["Downsample Y"] = 1.0

	save_database(mainUI.DB)


def reset_button(self, mainUI, canvas):

	canvas.replot_reset(mainUI)

def config_continue_button(self, mainUI, canvasVario):

	mainUI.DB[mainUI.ID]["Channel"] = mainUI.channelValue
	mainUI.DB[mainUI.ID]["Rotation Angle"] = mainUI.spinDegrees.value()
	mainUI.DB[mainUI.ID]["Crop X1"] = int(mainUI.X1)
	mainUI.DB[mainUI.ID]["Crop X2"] = int(mainUI.X2)
	mainUI.DB[mainUI.ID]["Crop Y1"] = int(mainUI.Y1)
	mainUI.DB[mainUI.ID]["Crop Y2"] = int(mainUI.Y2)
	mainUI.DB[mainUI.ID]["Scale X"] = float(mainUI.entryX1.text())
	mainUI.DB[mainUI.ID]["Scale Y"] = float(mainUI.entryY1.text())
	mainUI.DB[mainUI.ID]["Downsample X"] = float(mainUI.entryX2.text())
	mainUI.DB[mainUI.ID]["Downsample Y"] = float(mainUI.entryY2.text())
	save_database(mainUI.DB)

	produce_preview_graphic_vario(mainUI.newData)	
	canvasVario.reload_plot()

	mainUI.tabWidget.setCurrentIndex(2)

def stack_slider(self, mainUI, canvas):

	mainUI.labelStack.setText("Current Image in Stack: {}".format(mainUI.sliderStack.value() + 1))
	img = Image.open(mainUI.dataPathList[mainUI.sliderStack.value()])
	img.load()
	mainUI.data = np.asarray(img, dtype = "int32")
	canvas.replot_reset(mainUI)


