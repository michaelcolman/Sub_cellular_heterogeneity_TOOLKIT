import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser
from PIL import Image
import numpy as np
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from lib.CanvasSRF import *
from lib.SRF import *

def open_webbrowser_SRF():
	
	webbrowser.open("https://github.com/MaxxHolmes/HetKit")

def GenPreview_button(self, mainUI, canvasSRF):

	mainUI.progressBarSRF.setValue(0)
	field = generate_preview(mainUI)
	mainUI.progressBarSRF.setValue(33)
	save_preview_to_file(field)
	mainUI.progressBarSRF.setValue(66)
	produce_preview_graphic(field)
	mainUI.progressBarSRF.setValue(99)
	CanvasSRF.reload_plot(canvasSRF)
	mainUI.progressBarSRF.setValue(100)

def OpenSRF_button(self, mainUI):

	path = os.getcwd()
	webbrowser.open('file://' + str(path) + "/SRFs")

def GenSRF_button(self, mainUI):

	create_SRFs(mainUI)

def UseResults_button(self, mainUI):

	resultsReply = QMessageBox.question(self, 'Message - SRF', 'Would you like to load the Isotropic Lengthscale?')

	if resultsReply == QMessageBox.Yes:
		mainUI.dSB_Transverse.setValue(mainUI.AV_Isotropic)
		mainUI.dSB_Longitudinal.setValue(mainUI.AV_Isotropic)
	
	else:
		
		anisoReply = QMessageBox.question(self, 'Message - SRF', 'Would you like to load the transverse and longitudinal lengthscales?')

		if anisoReply == QMessageBox.Yes:
			mainUI.dSB_Transverse.setValue(mainUI.AV_Transverse)
			mainUI.dSB_Longitudinal.setValue(mainUI.AV_Longitudinal)
		else:
			pass

def FullSizeCheck(self, mainUI):

	if mainUI.CB_SRFFull.isChecked():
		mainUI.SB_SRFDimX.setValue(15)
		mainUI.SB_SRFDimY.setValue(20)
		mainUI.SB_SRFDimZ.setValue(65)
	else:
		pass

def PartSizeCheck(self, mainUI):

	if mainUI.CB_SRFPart.isChecked():
		mainUI.SB_SRFDimX.setValue(5)
		mainUI.SB_SRFDimY.setValue(5)
		mainUI.SB_SRFDimZ.setValue(10)
	else:
		pass





