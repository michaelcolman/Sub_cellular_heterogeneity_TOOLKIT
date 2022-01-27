import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import RectangleSelector

class CanvasSRF(FigureCanvas):

	def __init__(self, parent = None, width = 10, height = 10, dpi = 100):

		self.fig = Figure(figsize = (width, height), dpi = dpi)
		self.axes = self.fig.add_subplot(111)
		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)

		self.first_plot()

	def first_plot(self):

		image = plt.imread("lib/Images/defaultPreview.png")
		imgData = np.asarray(image)
		self.axes.imshow(imgData, aspect = 'auto')
		ax = plt.Axes(self.fig, [0., 0., 1., 1.])
		ax.set_axis_off()
		self.fig.add_axes(ax)
		self.axes.axis('off')
		self.fig.subplots_adjust(left = 0.0, bottom = 0.0, right = 1.0, top = 1.0, wspace = None, hspace = None)
		self.draw_idle()

	def reload_plot(self):

		image = plt.imread("SRFs/PreviewSRFContour.png")
		imgData = np.asarray(image)
		self.axes.imshow(imgData, aspect = 'auto')
		ax = plt.Axes(self.fig, [0., 0., 1., 1.])
		ax.set_axis_off()
		self.fig.add_axes(ax)
		self.axes.axis('off')
		self.fig.subplots_adjust(left = 0.0, bottom = 0.0, right = 1.0, top = 1.0, wspace = 0.0, hspace = 0.0)
		self.draw_idle()
