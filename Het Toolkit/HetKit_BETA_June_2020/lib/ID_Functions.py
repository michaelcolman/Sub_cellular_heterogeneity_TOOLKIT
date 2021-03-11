import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser
from PIL import Image
import numpy as np
from lib.database import *

def getFile(self, mainUI):

	options = QFileDialog.Options()
	options |= QFileDialog.DontUseNativeDialog
	fname, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "All Files (*)", options = options)
	
	mainUI.labelPath.setText(fname[0])
	mainUI.dataPathList = fname
	mainUI.sliderStack.setMaximum(len(mainUI.dataPathList)-1)

	return fname

def open_webbrowser():
	webbrowser.open('https://github.com/MaxxHolmes/HetKit')

def load_data(self, mainUI):

	img = Image.open(mainUI.dataPathList[0])
	img.load()
	mainUI.data = np.asarray(img, dtype = "int32")

def SRF_button(self, mainUI):

	mainUI.tabWidget.setCurrentIndex(3)

def continue_button(self, mainUI, canvas):

	load_data(self, mainUI)
	mainUI.tabWidget.setCurrentIndex(1)
	canvas.replot_reset(mainUI)

	mainUI.ID = mainUI.entryID.text()
	mainUI.DB[mainUI.ID]["Data Paths"] = mainUI.dataPathList
	save_database(mainUI.DB)	

def load_button(self, mainUI, canvas):

	print("ID: " + mainUI.entryID.text())
	mainUI.ID = mainUI.entryID.text()
	if str(mainUI.entryID.text()) in mainUI.DB:
		IDReply = QMessageBox.question(self, 'Message - ID', 'ID found! Load previous settings?')
		if IDReply == QMessageBox.Yes:
		
			mainUI.labelPath.setText(mainUI.DB[mainUI.ID]["Data Paths"][0])
			mainUI.dataPathList = mainUI.DB[mainUI.ID]["Data Paths"]
			mainUI.sliderStack.setMaximum(len(mainUI.dataPathList)-1)
			mainUI.channelValue = mainUI.DB[mainUI.ID]["Channel"]
			mainUI.spinDegrees.setValue(mainUI.DB[mainUI.ID]["Rotation Angle"])
			mainUI.X1 = mainUI.DB[mainUI.ID]["Crop X1"]
			mainUI.X2 = mainUI.DB[mainUI.ID]["Crop X2"]
			mainUI.Y1 = mainUI.DB[mainUI.ID]["Crop Y1"]
			mainUI.Y2 = mainUI.DB[mainUI.ID]["Crop Y2"]
			mainUI.entryX1.setText(str(mainUI.DB[mainUI.ID]["Scale X"]))
			mainUI.entryY1.setText(str(mainUI.DB[mainUI.ID]["Scale Y"]))
			mainUI.entryX2.setText(str(mainUI.DB[mainUI.ID]["Downsample X"]))
			mainUI.entryY2.setText(str(mainUI.DB[mainUI.ID]["Downsample Y"]))

			img = Image.open(mainUI.dataPathList[0])
			img.load()
			mainUI.data = np.asarray(img, dtype = "int32")

			if mainUI.channelValue == "Red":
				mainUI.rbRed.setChecked(True)
			elif mainUI.channelValue == "Green":
				mainUI.rbGreen.setChecked(True)
			elif mainUI.channelValue == "Blue":
				mainUI.rbBlue.setChecked(True)
			else:
				mainUI.rbAll.setChecked(True)

		if IDReply == QMessageBox.No:
			pass
	else:
		IDReply = QMessageBox.question(self, 'Message - ID', 'ID not found! Create a new analysis?')
		if IDReply == QMessageBox.Yes:
			mainUI.DB[mainUI.ID] = {}
			try:
				os.mkdir("Analysis")
			except FileExistsError:
				pass

			try:
				os.mkdir("Analysis/" + mainUI.ID)
			except FileExistsError:
				pass

			try:
				os.mkdir("Analysis/" + mainUI.ID + "/Variograms")
			except FileExistsError:
				pass

			try:
				os.mkdir("Analysis/" + mainUI.ID + "/Histograms")
			except FileExistsError:
				pass

			try:
				os.mkdir("Analysis/" + mainUI.ID + "/Slices")
			except FileExistsError:
				pass

		if IDReply == QMessageBox.No:
			pass



















	
