from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Toolbar
from matplotlib.widgets import RectangleSelector
from lib.Themes import app_dark_mode
from lib.ID_Tab import create_tabID
from lib.Config_Tab import create_tabConfig
from lib.Vario_Tab import create_tabVario
from lib.SRF_Tab import create_tabSRF
from lib.Retranslation import retranslateUi
from lib.Canvas import *
from lib.CanvasSRF import *
from lib.CanvasVario import *
from lib.ID_Functions import *
from lib.Config_Functions import *
from lib.Vario_Functions import *
from lib.SRF_Functions import *
import webbrowser
from lib.database import *
import os, sys, json

class UI_MainWindow(object):

	def check_DB_exists(self):

		if os.path.isfile("HetKit_Database.json"):

			self.DB = {}
			self.DB = load_database()
			print("Database found!")
			return self.DB

		else:

			self.DB = {}
			save_database(self.DB)
			print("No database found! A new one has been made.")
			return self.DB

	def setupUi(self, MainWindow):

	# Produces the main window of the UI
	
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(792, 773)
		MainWindow.setFixedSize(792, 773)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.data = []

		# Creates the tabs and widgets
		self.create_tabs()

		# Assign functions to widgets
		self.assign_functions()
		
	def create_tabs(self):

	    # Creates tab widget which houses the individual tab frames

		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 751))
		self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
		self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.tabWidget.setObjectName("tabWidget")
		
		# Functions which produce each individual tab

		create_tabID(self)
		create_tabConfig(self)
		create_tabVario(self)
		create_tabSRF(self)

		# Window functions and UI retranslation

		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		retranslateUi(self, MainWindow)
		self.tabWidget.setCurrentIndex(0)	# Changing this changes default window
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	

	def assign_functions(self):

		self.vtkMode = 0

		canvas = Canvas(self.graphicConfig, width = 8, height = 4.5)
		canvasSRF = CanvasSRF(self.graphicSRF, width = 4, height = 4)
		canvasVario = CanvasVario(self.graphicVario, width = 8, height = 2.5)
		
		# Functions for ID Tab
		self.buttonBrowse.clicked.connect(lambda: getFile(self.buttonBrowse, self))
		self.buttonHelp1.clicked.connect(lambda: open_webbrowser())
		self.buttonContinue.clicked.connect(lambda: continue_button(self.buttonContinue, self, canvas))
		self.buttonLoad.clicked.connect(lambda: load_button(self.buttonLoad, self, canvas))
		self.buttonCreateSRF.clicked.connect(lambda: SRF_button(self.buttonCreateSRF, self))

		# Functions for Config Tab
		self.buttonHelp2.clicked.connect(lambda: open_webbrowser_config())
		self.buttonReset.clicked.connect(lambda: reset_button(self.buttonReset, self, canvas))
		self.buttonApply.clicked.connect(lambda: apply_button(self.buttonApply, self, canvas))
		self.buttonRotate.clicked.connect(lambda: rotate_button(self.buttonRotate, self, canvas))
		self.rbRed.toggled.connect(lambda: channel_radio(self.rbRed, self, canvas))
		self.rbGreen.toggled.connect(lambda: channel_radio(self.rbGreen, self, canvas))
		self.rbBlue.toggled.connect(lambda: channel_radio(self.rbBlue, self, canvas))
		self.rbAll.toggled.connect(lambda: channel_radio(self.rbAll, self, canvas))
		self.sliderStack.valueChanged.connect(lambda: stack_slider(self.sliderStack, self, canvas))
		self.buttonContinue2.clicked.connect(lambda: config_continue_button(self.buttonContinue2, self, canvasVario))

		# Functions for Variogram Tab
		self.buttonHelp3.clicked.connect(lambda: help_button_vario())
		self.buttonLoadVTK.clicked.connect(lambda: loadVTK_button(self.buttonLoadVTK, self))
		self.buttonStartVario.clicked.connect(lambda: analysis_button(self.buttonStartVario, self, canvasVario))
		self.buttonResults.clicked.connect(lambda: analysis_results_button(self.buttonResults, self))
		self.buttonContinue3.clicked.connect(lambda: vario_continue_button(self.buttonContinue3, self))

		# Functions for SRF Tab
		self.buttonGenSRF.clicked.connect(lambda: GenSRF_button(self.buttonGenSRF, self))
		self.buttonHelp4.clicked.connect(lambda: open_webbrowser_SRF())
		self.buttonSRFLocation.clicked.connect(lambda: OpenSRF_button(self.buttonSRFLocation, self))
		self.buttonGenPreview.clicked.connect(lambda: GenPreview_button(self.buttonGenPreview, self, canvasSRF))
		self.buttonUseResults.clicked.connect(lambda: UseResults_button(self.buttonUseResults, self))
		self.CB_SRFFull.stateChanged.connect(lambda: FullSizeCheck(self.CB_SRFFull, self))
		self.CB_SRFPart.stateChanged.connect(lambda: PartSizeCheck(self.CB_SRFPart, self))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app_dark_mode(app)
	MainWindow = QtWidgets.QMainWindow()
	ui = UI_MainWindow()
	ui.check_DB_exists()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

