import os, sys, csv, matplotlib
import numpy as np 
from matplotlib import pyplot as plt
from gstools import vario_estimate_unstructured, vario_estimate_structured, Exponential, SRF
from gstools.covmodel.plot import plot_variogram
from datetime import datetime
matplotlib.use('Agg')
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from lib.Canvas import *
from lib.channels import channel_splitter
from lib.cropping import crop_data
from lib.rotation import rotate_data
from lib.downsample import downsample_data
from lib.variogram import *
from lib.SRF import *
from gstools import vario_estimate_unstructured, vario_estimate_structured, Exponential, SRF
from gstools.covmodel.plot import plot_variogram

def help_button_vario():
	webbrowser.open("https://github.com/MaxxHolmes/HetKit")

def loadVTK_button(self, mainUI):

	vtkReply = QMessageBox.question(self, 'Message - VTK', 'Are you sure you would like to load a .vtk file?\n'
										+ 'This will overwrite any current datafiles.')

	if vtkReply == QMessageBox.Yes:
		
		vtkOptions = QFileDialog.Options()
		vtkOptions |= QFileDialog.DontUseNativeDialog
		vtkfname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options = vtkOptions)

		mainUI.LoadVTKPath = vtkfname
		mainUI.vtkData, mainUI.vtkGrid = vtk2numpy(mainUI.LoadVTKPath)
		mainUI.vtkMode = 1

	else:

		pass

def prepare_data(mainUI):

	# Channel Splitting & Outputs
	mainUI.dataChannel = channel_splitter(mainUI.dataTemp, mainUI.DB[mainUI.ID]["Channel"])
	
	# Rotation & Outputs
	mainUI.dataRotated = rotate_data(mainUI.dataChannel, mainUI.DB[mainUI.ID]["Rotation Angle"])
	if mainUI.OPRotate == 1:
		output_slice_data(mainUI, mainUI.dataRotated,
						  "Analysis/" + mainUI.ID + "/Slices/Rotated_" + str(mainUI.processCount) + ".vtk",
						  "Analysis/" + mainUI.ID + "/Slices/Rotated_" + str(mainUI.processCount) + ".dat")
	if mainUI.OPHist == 1:
		output_hist_data(mainUI, mainUI.dataRotated,
						 "Analysis/" + mainUI.ID + "/Histograms/Rotated_" + str(mainUI.processCount) + ".png",
						 "Analysis/" + mainUI.ID + "/Histograms/Rotated_" + str(mainUI.processCount) + ".dat")

	# Cropping & Outputs
	mainUI.dataCropped = crop_data(mainUI.dataRotated, mainUI.DB[mainUI.ID]["Crop X1"], mainUI.DB[mainUI.ID]["Crop X2"],
												 mainUI.DB[mainUI.ID]["Crop Y1"], mainUI.DB[mainUI.ID]["Crop Y2"])
	if mainUI.OPCropped == 1:
		output_slice_data(mainUI, mainUI.dataCropped,
						  "Analysis/" + mainUI.ID + "/Slices/Cropped_" + str(mainUI.processCount) + ".vtk",
						  "Analysis/" + mainUI.ID + "/Slices/Cropped_" + str(mainUI.processCount) + ".dat")
	if mainUI.OPHist == 1:
		output_hist_data(mainUI, mainUI.dataCropped,
						 "Analysis/" + mainUI.ID + "/Histograms/Cropped_" + str(mainUI.processCount) + ".png",
						 "Analysis/" + mainUI.ID + "/Histograms/Cropped_" + str(mainUI.processCount) + ".dat")

	# Downsampling & Outputs
	mainUI.dataDownsampled = downsample_data(mainUI.dataCropped, mainUI.DB[mainUI.ID]["Downsample X"],
													   mainUI.DB[mainUI.ID]["Downsample Y"],
													   mainUI.DB[mainUI.ID]["Scale X"],
													   mainUI.DB[mainUI.ID]["Scale Y"])
	if mainUI.OPDownsample == 1:
		output_slice_data(mainUI, mainUI.dataDownsampled,
						  "Analysis/" + mainUI.ID + "/Slices/Downsampled_" + str(mainUI.processCount) + ".vtk",
						  "Analysis/" + mainUI.ID + "/Slices/Downsampled_" + str(mainUI.processCount) + ".dat")
	if mainUI.OPHist == 1:
		output_hist_data(mainUI, mainUI.dataDownsampled,
						 "Analysis/" + mainUI.ID + "/Histograms/Downsampled_" + str(mainUI.processCount) + ".png",
						 "Analysis/" + mainUI.ID + "/Histograms/Downsampled_" + str(mainUI.processCount) + ".dat")

def output_slice_data(mainUI, data, vtkname, datname):

	X = data.shape[0]
	Y = data.shape[1]
	try:
		Z = data.shape[2]
	except IndexError:
		data = np.reshape(data, (data.shape[0], data.shape[1], 1))
		Z = data.shape[2]
	
	with open(vtkname, "w") as vtkfile:	
		with open(datname, "w") as datfile:
			
			vtkfile.write("# vtk DataFile Version 3.0\n"
			+   "vtk output\n"
			+   "ASCII\n"
			+   "DATASET STRUCTURED_POINTS\n"
			+   "DIMENSIONS {} {} {}\n".format(X, Y, Z)
			+   "SPACING 1 1 1\n"
			+   "ORIGIN 0 0 0\n"
			+   "POINT_DATA {}\n".format(X*Y*Z)
			+   "SCALARS Image float 1\n"
			+   "LOOKUP_TABLE default\n")

			for k in range(Z):
				for j in range(Y):
					for i in range(X):
						vtkfile.write(str(data[i][j][k]) + " ")
						datfile.write(str(data[i][j][k]) + " ")
					vtkfile.write("\n")
					datfile.write("\n")
				vtkfile.write("\n")
				datfile.write("\n")
			vtkfile.close()
			datfile.close()

def output_hist_data(mainUI, data, hist_name, hist_dat_name):

	data = np.asarray(data)
	hist, bins = np.histogram(data.flatten(), 20)
	figure = plt.figure(figsize = (10, 10))
	plt.bar(bins[:-1], hist, width = (bins[-1]-bins[-2]), align = "edge")
	plt.xlabel("Pixel Value (Intensity)")
	plt.ylabel("Count")
	plt.savefig(str(hist_name))
	plt.close()

	for q in range(len(bins)-1):
		if q == 0:
			hist_data = [bins[q+1], hist[q]]
		else:
			hist_new = [bins[q+1], hist[q]]
			hist_data = np.vstack([hist_data, hist_new])

	hist_data = np.asarray(hist_data)
	with open(str(hist_dat_name), "w") as histfile:
		for y in range(hist_data.shape[1]):
			for x in range(hist_data.shape[0]):
				histfile.write(str(hist_data[x][y]) + " ")
			histfile.write("\n")
		histfile.close()

def output_checkboxes(mainUI):

	mainUI.OPRotate = 0
	mainUI.OPCropped = 0
	mainUI.OPDownsample = 0
	mainUI.OPVario = 0
	mainUI.OPHist = 0

	if mainUI.checkOPDefault.isChecked() == True:
		mainUI.OPRotate = 1
		mainUI.OPCropped = 1
		mainUI.OPDownsample = 1
		mainUI.OPVario = 1
		mainUI.OPHist = 1

	if mainUI.checkOPRotate.isChecked() == True:
		mainUI.OPRotate = 1
	if mainUI.checkOPCropped.isChecked() == True:
		mainUI.OPCropped = 1
	if mainUI.checkOPDownsample.isChecked() == True:
		mainUI.OPDownsample = 1
	if mainUI.checkOPVario.isChecked() == True:
		mainUI.OPVario = 1
	if mainUI.checkOPHist.isChecked() == True:
		mainUI.OPHist = 1

def analysis_button(self, mainUI, canvasVario):

	mainUI.processCount = 0
	mainUI.progressVario.setValue(0)

	output_checkboxes(mainUI)

	# Check for loaded VTK settings

	tempArray = []

	if mainUI.vtkMode == 1:
		mainUI.dataArray = mainUI.vtkData

	else:

		for image in mainUI.dataPathList:
			img = Image.open(image)
			img.load()
			mainUI.dataTemp = np.asarray(img, dtype = "int32")
			prepare_data(mainUI)
			tempArray.append(mainUI.dataDownsampled)
			mainUI.dataArray = np.dstack(tempArray)
			mainUI.processCount += 1

	mainUI.dataArray = normalise_dataset(mainUI.dataArray)
	mainUI.dataArray = zeroth_filter(mainUI.dataArray)
	if mainUI.dataArray.ndim < 3:
		mainUI.dataArray = np.reshape(mainUI.dataArray, (mainUI.dataArray[0], mainUI.dataArray[1], 1))
	
	# Variogram Preparation

	if mainUI.vtkMode == 1:
		mainUI.x_s, mainUI.y_s, mainUI.z_s = create_structured_grid_vtk(mainUI.vtkGrid)
	else:
		mainUI.x_s, mainUI.y_s, mainUI.z_s = create_structured_grid(mainUI.dataArray)

	X, Y, Z = len(mainUI.x_s), len(mainUI.y_s), len(mainUI.z_s)

	mainUI.dataArrayLog = integration3D(mainUI)
	x_u, y_u = create_unstructured_grid(mainUI.x_s, mainUI.y_s)

	bin_space, bin_no = set_bins(mainUI)

	total_cells = len(mainUI.x_s) * len(mainUI.y_s)
	total_itrs = len(bin_space) * len(bin_no)
	
	progress = 10
	progress_full = 10 + (total_itrs * 3) + 1
	mainUI.progressVario.setValue(np.rint((progress/progress_full) * 100))

	# Variogram Fitting Loop
	
	progress_full = 10 + (total_itrs * 3) + 1
	count = 0
	for i in range(len(bin_no)):
		for j in range(len(bin_space)):
			
			bins = np.linspace(0, bin_space[j], bin_no[i])
			
			# Unstructured Fit
			
			mainUI.bin_center, mainUI.gamma = vario_estimate_unstructured((x_u, y_u),
															mainUI.dataArrayLog.flatten(),
															bins,
															sampling_size = total_cells)
			mainUI.fit_model = Exponential(dim = 2)
			mainUI.fit_model.fit_variogram(mainUI.bin_center, mainUI.gamma, nugget = False)

			# Update progress bar
			progress += 1
			mainUI.progressVario.setValue(np.rint((progress/progress_full) * 100))

			# Structured Fit

			mainUI.gamma_x = vario_estimate_structured(mainUI.dataArrayLog, direction = 'x')
			mainUI.gamma_y = vario_estimate_structured(mainUI.dataArrayLog, direction = 'y')
			mainUI.fit_model_x = Exponential(dim = 2)
			mainUI.fit_model_y = Exponential(dim = 2)
			mainUI.fit_model_x.fit_variogram(mainUI.x_s, mainUI.gamma_x, nugget = False)
			mainUI.fit_model_y.fit_variogram(mainUI.y_s, mainUI.gamma_y, nugget = False)

			# Update progress bar
			progress += 1
			mainUI.progressVario.setValue(np.rint((progress/progress_full) * 100))		

			# Output Variograms

			if mainUI.OPVario == 1:
			
				output_variogram(mainUI, "Analysis/" + mainUI.ID + "/Variograms/Plot_BS_" + str(bin_space[j]) + "_BC_" + str(bin_no[i]) + ".png")

			if count == 0:
				mainUI.varioParams = extract_variogram_params(mainUI, bin_space[j], bin_no[i])			
			varioTemp = extract_variogram_params(mainUI, bin_space[j], bin_no[i])
			mainUI.varioParams = np.vstack([mainUI.varioParams, varioTemp])

			for x in range(len(mainUI.bin_center)):
				if x == 0:
					out_data = [mainUI.bin_center[x], mainUI.gamma[x]]
				else:
					out_new = [mainUI.bin_center[x], mainUI.gamma[x]]
					out_data = np.vstack([out_data, out_new])

			for x in range(len(mainUI.x_s)):
				if x == 0:
					outx_data = [mainUI.x_s[x], mainUI.gamma_x[x]]
				else:
					outx_new = [mainUI.x_s[x], mainUI.gamma_x[x]]
					outx_data = np.vstack([outx_data, outx_new])

			for x in range(len(mainUI.y_s)):
				if x == 0:
					outy_data = [mainUI.y_s[x], mainUI.gamma_y[x]]
				else:
					outy_new = [mainUI.y_s[x], mainUI.gamma_y[x]]
					outy_data = np.vstack([outy_data, outy_new])


			structured_outname = "Analysis/" + mainUI.ID + "/Variograms/Data_BS_" + str(bin_space[j]) + "_BC_" + str(bin_no[i]) + ".dat" 
			with open(structured_outname, 'w') as outfile:
				for m in range(len(mainUI.bin_center)):
					for n in range(len(out_data[m])):
						outfile.write(str(out_data[m][n]) + " ")
					outfile.write("\n")
				outfile.close()

			structured_y = "Analysis/" + mainUI.ID + "/Variograms/Data_X.dat"
			structured_x = "Analysis/" + mainUI.ID + "/Variograms/Data_Y.dat"

			with open(structured_x, "w") as outfile:
				for m in range(len(mainUI.x_s)):
					for n in range(len(outx_data[m])):
						outfile.write(str(outx_data[m][n]) + " ")
					outfile.write("\n")
				outfile.close()

			with open(structured_y, "w") as outfile:
				for m in range(len(mainUI.y_s)):
					for n in range(len(outy_data[m])):
						outfile.write(str(outy_data[m][n]) + " ")
					outfile.write("\n")
				outfile.close()

			params_outname = "Analysis/" + mainUI.ID + "Variogram_Results.dat"
			with open(params_outname, "w") as outfile:
				for m in range(len(mainUI.varioParams)):
					for n in range(len(mainUI.varioParams[0])):
						outfile.write(str(mainUI.varioParams[m][n]) + " ")
					outfile.write("\n")
				outfile.close()

			# Update progress bar
			progress += 1
			mainUI.progressVario.setValue(np.rint((progress/progress_full) * 100))
			count += 1

	calculate_best_params(mainUI)
	srf = SRF(mainUI.fit_model)
	testSRF = srf((mainUI.x_s, mainUI.y_s), mesh_type = "structured")
	testSRF = np.reshape(testSRF, (len(mainUI.x_s), len(mainUI.y_s), 1))
	output_SRF(testSRF, "SRFs/" + str(mainUI.ID) + "_TestSRF_", len(mainUI.x_s), len(mainUI.y_s), 1)
	mainUI.progressVario.setValue(100)

def calculate_best_params(mainUI):

	results_output = "Analysis/" + mainUI.ID + "/Full_Results.dat"
	with open(results_output, "w") as resultfile:
		for m in range(len(mainUI.varioParams)):
			for n in range(len(mainUI.varioParams[0])):
				resultfile.write(str(mainUI.varioParams[m][n]) + " ")
			resultfile.write("\n")
		resultfile.close()



	fit_var 			= mainUI.varioParams.T[3].astype(float)
	fit_len 			= mainUI.varioParams.T[4].astype(float)
	fit_var_x 			= mainUI.varioParams.T[5].astype(float)
	fit_len_x 			= mainUI.varioParams.T[6].astype(float)
	fit_var_y 			= mainUI.varioParams.T[7].astype(float)
	fit_len_y 			= mainUI.varioParams.T[8].astype(float)

	mean_fit_var 		= np.mean(fit_var[fit_var <= 20])
	mean_fit_len 		= np.mean(fit_len[fit_len <= 50])
	mean_fit_var_x 		= np.mean(fit_var_x[fit_var_x <= 20])
	mean_fit_len_x 		= np.mean(fit_len_x[fit_len_x <= 50])
	mean_fit_var_y 		= np.mean(fit_var_y[fit_var_y <= 20])
	mean_fit_len_y 		= np.mean(fit_len_y[fit_len_y <= 50])

	if mainUI.vtkMode == 1:
		
		scaled_fit_var		= mean_fit_var
		scaled_fit_len		= mean_fit_len
		scaled_fit_var_x	= mean_fit_var_X
		scaled_fit_len_x	= mean_fit_len_x
		scaled_fit_var_y	= mean_fit_var_y
		scaled_fit_len_y	= mean_fit_len_y

	else:
	
		scaled_fit_var      = mean_fit_var * np.mean([float(mainUI.DB[mainUI.ID]["Downsample X"]),
													  float(mainUI.DB[mainUI.ID]["Downsample Y"])])
		scaled_fit_len      = mean_fit_len * np.mean([float(mainUI.DB[mainUI.ID]["Downsample X"]),
                                                      float(mainUI.DB[mainUI.ID]["Downsample Y"])])

		scaled_fit_var_x    = mean_fit_var_x * float(mainUI.DB[mainUI.ID]["Downsample X"])
		scaled_fit_len_x    = mean_fit_len_x * float(mainUI.DB[mainUI.ID]["Downsample X"])
		scaled_fit_var_y    = mean_fit_var_y * float(mainUI.DB[mainUI.ID]["Downsample Y"])
		scaled_fit_len_y    = mean_fit_var_y * float(mainUI.DB[mainUI.ID]["Downsample Y"])

	output_matrix = [
	["Type", "Mean Fit Var", "Mean Fit Len", "Mean Fit Var X", "Mean Fit Len X", "Mean Fit Var Y", "Mean Fit Len Y"],
	["Mean Outputs", float(mean_fit_var), float(mean_fit_len), float(mean_fit_var_x), float(mean_fit_len_x),
	 float(mean_fit_var_y), float(mean_fit_len_y)],
	["Scaled Outputs", float(scaled_fit_var), float(scaled_fit_len), float(scaled_fit_var_x), float(scaled_fit_len_x),
     float(scaled_fit_var_y), float(scaled_fit_len_y)]]

	results_output = "Analysis/" + mainUI.ID + "/Final_Results.dat"
	with open(results_output, "w") as resultfile:
		for m in range(len(output_matrix)):
			for n in range(len(output_matrix[0])):
				resultfile.write(str(output_matrix[m][n]) + " ")
			resultfile.write("\n")
		resultfile.close()

	mainUI.AV_Isotropic = scaled_fit_len
	mainUI.AV_Transverse = scaled_fit_len_x
	mainUI.AV_Longitudinal = scaled_fit_len_y


def analysis_results_button(self, mainUI):

	path = os.getcwd()
	webbrowser.open('file://' + str(path) + '/Analysis/' + str(mainUI.ID))
	print('file://' + str(path) + 'Analysis/' + str(mainUI.ID))
	

def vario_continue_button(self, mainUI):

# ------- Incomplete

	mainUI.tabWidget.setCurrentIndex(4)


def output_variogram(mainUI, varioname):

	plt.figure(figsize = (10, 10))

	line, = plt.plot(mainUI.bin_center, mainUI.gamma, label = 'Estimated Variogram (ISO)')
	plt.plot(mainUI.bin_center, mainUI.fit_model.variogram(mainUI.bin_center), color = line.get_color(), linestyle = "--", label = 'Exp. Variogram (ISO)')
	line, = plt.plot(mainUI.x_s, mainUI.gamma_x, label = 'Estimated Variogram (X)')
	plt.plot(mainUI.x_s, mainUI.fit_model_x.variogram(mainUI.x_s), color = line.get_color(), linestyle = "--",
			 label = 'Exp. Variogram (X)')
	line, = plt.plot(mainUI.y_s, mainUI.gamma_y, label = 'Estimated Variogram (Y)')
	plt.plot(mainUI.y_s, mainUI.fit_model_y.variogram(mainUI.y_s), color = line.get_color(), linestyle = "--",
			 label = 'Exp. Variogram (Y)')

	plt.legend()
	plt.savefig(varioname)
	plt.close()


def extract_variogram_params(mainUI, bin_space, bin_no):

	info = [mainUI.ID, bin_space, bin_no, float(np.round(mainUI.fit_model.var, 3)), 
			float(np.round(mainUI.fit_model.len_scale, 3)), float(np.round(mainUI.fit_model_x.var, 3)),
			float(np.round(mainUI.fit_model_x.len_scale, 3)), float(np.round(mainUI.fit_model_y.var, 3)),
			float(np.round(mainUI.fit_model_y.len_scale, 3))]

	return info
