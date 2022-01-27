import os, sys, csv, matplotlib
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from gstools import vario_estimate_unstructured, vario_estimate_structured, Exponential, SRF
from gstools.covmodel.plot import plot_variogram
from datetime import datetime
from lib.channels import channel_splitter
from lib.rotation import rotate_data
from lib.downsample import downsample_data
matplotlib.use('Agg')

def vtk2numpy(filename, dtype = None, verbose = False):

	try:
		with open(filename, 'rb') as in_file:
	
			grid = {}
			if verbose:
				print(('\n	Reading file: "{0}"'.format(file_name)))
			
			# Skip the first three lines
			line = in_file.readline()
			line = in_file.readline()
			line = in_file.readline()

			# This line should contain the description of the dataset
			line = in_file.readline()
			line_split = line.split()

			if line_split[1] != b"STRUCTURED_POINTS":
				print("	Error: 'vtk2numpy' can read only ", end = "")
				print("	`STRUCTURED_POINTS` datasets.")

			# The order of the following keywords can be generic

			for i in range(4):
				line = in_file.readline()
				line_split = line.split()
				if line_split[0] == b'DIMENSIONS':
					grid['nx'] = int(line_split[1])
					grid['ny'] = int(line_split[2])
					grid['nz'] = int(line_split[3])
				elif line_split[0] == b'ORIGIN':
					grid['ox'] = int(line_split[1])
					grid['oy'] = int(line_split[2])
					grid['oz'] = int(line_split[3])
				elif line_split[0] == b'SPACING':
					grid['dx'] = int(line_split[1])
					grid['dy'] = int(line_split[2])
					grid['dz'] = int(line_split[3])
				elif line_split[0] == b'POINT_DATA':
					grid['type'] = 'points'
					grid['points'] = int(line_split[1])
				elif line_split[0] == b'CELL_DATA':
					grid['type'] = 'cells'
					grid['cells'] = int(line_split[1])
				else:
					print("	Error in 'vtk2numpy'. Check your VTK keywords.")

			# Read the data type
			line = in_file.readline()
			line_split = line.split()
			data_type = line_split[2]
			if not dtype:
				# if dtype is provided as an argument, it overwrites the dtype of the dataset
				if data_type in (b'int',):
					dtype = np.int32
				elif data_type in (b'float',):
					dtype = np.float64
				else:
					dtype = None

			# Skip the line containing information about the LOOKUP_TABLE
			line = in_file.readline()

			# Read the data as a CSV file
			data_tmp = pd.read_csv(in_file, dtype = dtype, sep = " ", header = None).values
			data_tmp = data_tmp[np.logical_not(np.isnan(data_tmp))]
			data = np.reshape(data_tmp, (grid['nx'], grid['ny'], grid['nz']), order = 'F')

		return data, grid

	except IOError:
		print(('	Error reading file "{0}"'.format(file_name)))
		print('	Check if the file exists...')

def create_unstructured_grid(x_s, y_s):

	x_u, y_u = np.meshgrid(x_s, y_s)
	len_unstruct = len(x_s) * len(y_s)
	x_u = np.reshape(x_u, len_unstruct)
	y_u = np.reshape(y_u, len_unstruct)

	return x_u, y_u

def normalise_dataset(data):

	min_data = np.min(data)
	max_data = np.max(data)
	normal_data = (data - min_data) / (max_data - min_data)

	return normal_data

def zeroth_filter(data):

	zeroth_data = np.where(data == 0, 0.0000000001, data)

	return zeroth_data

def create_structured_grid_vtk(grid):

	x_s = np.arange(grid['ox'], grid['nx'] * grid['dx'], grid['dx'])
	y_s = np.arange(grid['oy'], grid['ny'] * grid['dy'], grid['dy'])
	z_s = np.arange(grid['oz'], grid['nz'] * grid['dz'], grid['dz'])

	return x_s, y_s, z_s

def create_structured_grid(data):

	x_s = np.arange(0, data.shape[0], 1)
	y_s = np.arange(0, data.shape[1], 1)
	z_s = np.arange(0, data.shape[2], 1)

	return x_s, y_s, z_s

def integration3D(mainUI):

	if mainUI.vtkMode == 1:
		log_data = np.log(np.sum(mainUI.dataArray, axis = 2) * mainUI.vtkGrid['dz'])
	else:
		log_data = np.log(np.sum(mainUI.dataArray, axis = 2) * 1)

	return log_data


def set_bins(mainUI):

	space_1 = mainUI.spinBS1.value()
	space_2 = mainUI.spinBS2.value()
	count_1 = mainUI.spinBC1.value()
	count_2 = mainUI.spinBC2.value()

	bin_space = np.arange(space_1, space_2, 5)
	bin_no = np.arange(count_1, count_2, 5)

	return bin_space, bin_no


def output_unstructured(fit_model, bin_center, gamma, output_name):

	plt.plot(bin_center, gamma)
	plot_variogram(fit_model, x_max = bins[-1])
	plt.savefig(output_name + ".png")
	plt.close()

def output_variogram(fit_model, fit_model_x, fit_model_y, gamma, gamma_x, gamma_y, bin_center, x_s, y_s, output_name):

	plt.figure(figsize = (10, 10))
	
	line, = plt.plot(bin_center, gamma, label = 'Estimated Variogram (ISO)')
	plt.plot(bin_center, fit_model.variogram(bin_center), color = line.get_color(), linestyle = '--',
			 label = 'Exp. Variogram (ISO)')
	
	line, = plt.plot(x_s, gamma_x, label = 'Estimated Variogram (X)')
	plt.plot(x_s, fit_model_x.variogram(x_s), color = line.get_color(), linestyle = '--',
			 label = 'Exp. Variogram (X)')

	line, = plt.plot(y_s, gamma_y, label = 'Estimated Variogram (Y)')
	plt.plot(y_s, fit_model_y.variogram(y_s), color = line.get_color(), linestyle = '--',
			 label = 'Exp. Variogram (Y)')

	plt.legend()
	plt.savefig(output_name + ".png")
	plt.close()

	














