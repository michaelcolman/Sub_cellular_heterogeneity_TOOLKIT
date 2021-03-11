    
from PyQt5.QtGui import QPalette, QColor


def app_dark_mode(app):

	"""
	Dark Mode Palette for PyQt5 GUI Applications
	Call this function to put the app into "dark mode" 
	
	"""

	app.setStyle("Fusion")
	dark_palette = QPalette()
	dark_palette.setColor(QPalette.Window, QColor(51, 57, 59))
	dark_palette.setColor(QPalette.WindowText, QColor(238, 238, 236))
	dark_palette.setColor(QPalette.Base, QColor(35, 39, 41))
	dark_palette.setColor(QPalette.AlternateBase, QColor(35, 39, 41))
	dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
	dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
	dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
	dark_palette.setColor(QPalette.Button, QColor(51, 57, 59))
	dark_palette.setColor(QPalette.ButtonText, QColor(238, 238, 236))
	dark_palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
	dark_palette.setColor(QPalette.Link, QColor(0, 0, 255))
	dark_palette.setColor(QPalette.Highlight, QColor(33, 93, 156))
	dark_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
	dark_palette.setColor(QPalette.Light, QColor(63, 71, 74))
	dark_palette.setColor(QPalette.Midlight, QColor(203, 199, 196))
	dark_palette.setColor(QPalette.Dark, QColor(42, 47, 49))
	dark_palette.setColor(QPalette.Mid, QColor(184, 181, 178))
	dark_palette.setColor(QPalette.Shadow, QColor(39, 44, 45))
	dark_palette.setColor(QPalette.LinkVisited, QColor(255, 0, 255))
	app.setPalette(dark_palette)
	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")



