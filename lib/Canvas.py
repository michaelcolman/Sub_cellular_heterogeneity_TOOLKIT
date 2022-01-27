import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import RectangleSelector

class Canvas(FigureCanvas):
	def __init__(self, parent = None, width = 5, height = 6, dpi = 100):
	
		self.fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = self.fig.add_subplot(111)

		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)

		self.toolbar = NavigationToolbar(self, self)
		self.toolbar.update()

		self.first_plot()
		self.fig.tight_layout()

		self.rectSelect = RectangleSelector(self.axes, self.line_select_callback,
                                            drawtype = 'box', useblit = False, button = [1],
                                            minspanx = 5, minspany = 5, spancoords = 'pixels',
                                            interactive = True)

		self.figure.canvas.mpl_connect('button_press_event', self.on_click)


	def first_plot(self):

		img = Image.open("lib/Images/Original.png")
		img.load()
		data = np.asarray(img, dtype = "uint8")
		self.axes.imshow(data)
		self.draw_idle()

		self.x1 = 0
		self.y1 = 0
		self.x2 = len(data[1])
		self.y2 = len(data[0])


	def on_click(self, event):

		if event.button == 1 or event.button == 3 and not self.rectSelect.active:
			self.rectSelect.set_active(True)
		else:
			self.rectSelect.set_active(False)

	def line_select_callback(self, eclick, erelease):

		self.x1, self.y1 = np.round(int(eclick.xdata)), np.round(int(eclick.ydata))
		self.x2, self.y2 = np.round(int(erelease.xdata)), np.round(int(erelease.ydata))

		print("(" + str(self.x1) + ", " + str(self.y1) + ")" + " (" + str(self.x2) + ", " +  str(self.y2) + ")")

	def replot_reset(self, mainUI):

		self.axes.clear()
		self.axes.imshow(mainUI.data)
		self.rectSelect = RectangleSelector(self.axes, self.line_select_callback,
                                            drawtype = 'box', useblit = False, button = [1],
                                            minspanx = 5, minspany = 5, spancoords = 'pixels',
                                            interactive = True)
		self.draw_idle()

		self.x1 = 0
		self.y1 = 0
		self.x2 = len(mainUI.data[1])
		self.y2 = len(mainUI.data[0])

	def replot_apply(self, mainUI):

		self.axes.clear()
		self.axes.imshow(mainUI.newData, cmap = 'gray')
		self.rectSelect = RectangleSelector(self.axes, self.line_select_callback,
                                            drawtype = 'box', useblit = False, button = [1],
                                            minspanx = 5, minspany = 5, spancoords = 'pixels',
                       						interactive = True)
		self.draw_idle()

	def replot_showData(self, mainUI):

		self.axes.clear()
		self.axes.imshow(mainUI.showData, cmap = 'gray')
		self.rectSelect = RectangleSelector(self.axes, self.line_select_callback,
											drawtype = 'box', useblit = False, button = [1],
											minspanx = 5, minspany = 5, spancoords = 'pixels',
											interactive = True)
		self.draw_idle()

		self.x1 = 0
		self.y1 = 0
		self.x2 = len(mainUI.showData[1])
		self.y2 = len(mainUI.showData[0])

	def update_crop_label(self, mainUI):

		mainUI.labelCoords.setText("Co-ordinates:	({}, {}), ({}, {})".format(self.x1, self.y1, self.x2, self.y2))
