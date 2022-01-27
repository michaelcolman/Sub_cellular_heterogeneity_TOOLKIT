import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from gstools import SRF, Gaussian
import os
import sys
from datetime import datetime


def scale(x, max_CRU, exp):

	out_range = ((0.95 * (1 - (max_CRU - 1)) * exp), (0.95 * max_CRU) * exp)
	domain = np.min(x), np.max(x)
	y = (x - (domain[1] + domain[0]) / 2) / (domain[1] - domain[0])
	return y * (out_range[1] - out_range[0]) + (out_range[1] + out_range[0]) / 2

def generate_preview(mainUI):

	var = 1.0
	X = 40
	Y = 40
	Z = 1
	len_long = float(mainUI.dSB_Longitudinal.value())
	len_trans = float(mainUI.dSB_Transverse.value())
	CRU_var = 1.0
	MeanExp = 1.0
	max_CRU = 1.5
	min_CRU = 0.5

	x = range(X)
	y = range(Y)

	model = Gaussian(dim = 2, var = var, len_scale = (len_long, len_trans))
	srf = SRF(model)
	field = srf((x, y), mesh_type = 'structured')

	map_total = np.sum(field)
	if map_total != X*Y*MeanExp:
		field = field * ((X*Y*MeanExp) / map_total)

	field = scale(field, max_CRU, MeanExp)
	field = field + (MeanExp - np.mean(field))

	return field

def save_preview_to_file(field):

	X = 40
	Y = 40

	with open("SRFs/PreviewSRF.vtk", "w") as vtkfile:
		with open("SRFs/PreviewSRF.dat", "w") as datfile:

			vtkfile.write("# vtk DataFile Version 3.0\n"
			+	"vtk output\n"
			+	"ASCII\n"
			+	"DATASET STRUCTURED_POINTS\n"
			+	"DIMENSIONS 40 40 1\n"
			+	"SPACING 1 1 1\n"
			+	"ORIGIN 0 0 0\n"
			+	"POINT_DATA 2500\n"
			+	"SCALARS Image float 1\n"
			+	"LOOKUP_TABLE default\n")

			for j in range(Y):
				for i in range(X):
					vtkfile.write(str(field[i][j]) + " ")
					datfile.write(str(field[i][j]) + " ")
				vtkfile.write("\n")
				datfile.write("\n")
			vtkfile.close()
			datfile.close()

def produce_preview_graphic(field):

	contour_data = (field - np.amin(field)) / (np.amax(field) - np.amin(field))

	fig1 = plt.Figure(facecolor = 'white', figsize = (30, 30), dpi = 100)
	lY = len(field)
	lX = len(field[0])
	x = np.linspace(0, lX, lX)
	y = np.linspace(0, lY, lY)
	X, Y = np.meshgrid(x, y)
	ax1 = fig1.add_subplot(1, 1, 1)
	V = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	D = ax1.contourf(X, Y, contour_data, V, alpha = 1, cmap = "coolwarm", vmin = 0, vmax = 1.0)
	C = ax1.contour(X, Y, contour_data, V, colors = 'black', linewidths = .5, vmin = 0, vmax = 1.0)
	ax1.set_xticklabels('', visible = False)
	ax1.set_yticklabels('', visible = False)
	plt.Figure.subplots_adjust(fig1, left = 0.0, bottom = 0.0, right = 1.0, top = 1.0, wspace = 0.0, hspace = 0.0)
	fig_name = 'SRFs/PreviewSRFContour.png'
	plt.Figure.savefig(fig1, fig_name)

def produce_preview_graphic_vario(field):

	contour_data = (field - np.amin(field)) / (np.amax(field) - np.amin(field))

	fig1 = plt.Figure(facecolor = 'white', figsize = (10, 10), dpi = 100)
	lY = len(field)
	lX = len(field[0])
	x = np.linspace(0, lX, lX)
	y = np.linspace(0, lY, lY)
	X, Y = np.meshgrid(x, y)
	ax1 = fig1.add_subplot(1, 1, 1)
	V = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	D = ax1.contourf(X, Y, contour_data, V, alpha = 1, cmap = "coolwarm", vmin = 0, vmax = 1.0)
	C = ax1.contour(X, Y, contour_data, V, colors = 'black', linewidths = .5, vmin = 0, vmax = 1.0)
	ax1.set_xticklabels('', visible = False)
	ax1.set_yticklabels('', visible = False)
	plt.Figure.subplots_adjust(fig1, left = 0.0, bottom = 0.0, right = 1.0, top = 1.0, wspace = 0.0, hspace = 0.0)
	fig_name = 'SRFs/PreviewVarioContour.png'
	plt.Figure.savefig(fig1, fig_name)

def create_SRFs(mainUI):

	mainUI.progressBarSRF.setValue(0)
	name = str(mainUI.EntrySRFName.text())
	var = 1.0
	X = int(mainUI.SB_SRFDimX.value())
	Y = int(mainUI.SB_SRFDimY.value())
	Z = int(mainUI.SB_SRFDimZ.value())
	num = int(mainUI.SB_SRFNum.value())
	CRU_var = float(mainUI.SB_NeighbourVar.value())
	MeanExp = float(mainUI.SB_MeanExp.value())
	len_long = float(mainUI.dSB_Longitudinal.value())
	len_trans = float(mainUI.dSB_Transverse.value())

	progress_full = (num * 3) + 2

	max_CRU = MeanExp + CRU_var
	min_CRU = MeanExp - CRU_var

	x = range(X)
	y = range(Y)
	z = range(Z)

	print("Name: " + str(name) + "\n"
	+	"Variation: " + str(var) + "\n"
	+	"Lengthscale: " + str(len_long) + ", " + str(len_trans) + "\n"
	+	"Total Expression: " + str(MeanExp) + "\n"
	+	"CRU Expression Max: " + str(max_CRU) + "\n"
	+	"CRU Expression Min: " + str(min_CRU) + "\n"
	+ 	"Dimensions : X " + str(X) + " Y " + str(Y) + " Z " + str(Z))

	count = 0
	progress = 1
	mainUI.progressBarSRF.setValue(np.rint((progress/progress_full) * 100))
	while count < num:
	
		print("Generating SRF {}".format(count + 1))

		SRF_check = 0
		while SRF_check == 0:

			model = Gaussian(dim = 3, var = var, len_scale = (len_long, len_trans))
			srf = SRF(model)
			field = srf((x, y, z), mesh_type = 'structured')
			map_total = np.sum(field)
			if map_total != X*Y*Z*MeanExp:
				field = field * ((X*Y*Z*MeanExp) / map_total)
			field = scale(field, max_CRU, MeanExp)
			field = field + (MeanExp - np.mean(field))
			if np.mean(field) == MeanExp:
				if np.max(field) < (max_CRU * 1.05):
					if np.min(field) > (min_CRU * 0.95):
						SRF_check = 1
		progress += 1
		mainUI.progressBarSRF.setValue(np.rint((progress/progress_full) * 100))
		count += 1
		output_name = "SRFs/" + str(name) + "_" + str(count) + "_"
		output_SRF(field, output_name, X, Y, Z)
		progress += 1
		mainUI.progressBarSRF.setValue(np.rint((progress/progress_full) * 100))

	mainUI.outputSRF = "SRFs/" + str(name) + "_1_VTK.vtk"
	print("SRF Generation Completed")
	mainUI.progressBarSRF.setValue(100)

def output_SRF(field, name, X, Y, Z):

	with open(name + "VTK.vtk", "w") as vtkfile:
		with open(name + "DAT.dat", "w") as datfile:

			vtkfile.write("# vtk DataFile Version 3.0\n"
			+ "vtk output\n"
			+ "ASCII\n"
			+ "DATASET STRUCTURED_POINTS\n"
			+ "DIMENSIONS {} {} {}\n".format(X, Y, Z)
			+ "SPACING 1 1 1\n"
			+ "ORIGIN 0 0 0\n"
			+ "POINT_DATA {}\n".format(X*Y*Z)
			+ "SCALARS Image float 1\n"
			+ "LOOKUP_TABLE default\n")

			for k in range(Z):
				for j in range(Y):
					for i in range(X):
						vtkfile.write(str(field[i][j][k]) + " ")
						datfile.write(str(field[i][j][k]) + " ")
					vtkfile.write("\n")
					datfile.write("\n")
				vtkfile.write("\n")
				datfile.write("\n")
			vtkfile.close()
			datfile.close()

