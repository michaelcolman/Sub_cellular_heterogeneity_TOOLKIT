from PIL import Image
import numpy as np

def load_image(path):

	img = Image.open(path)
	img.load()
	data = np.asarray(img, dtype = "int32")

	return data


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
			data_tmp = pd.read_csv(in_file, dtype = dtype, sep = " ", header = -1).values
			data_tmp = data_tmp[np.logical_not(np.isnan(data_tmp))]
			data = np.reshape(data_tmp, (grid['nx'], grid['ny'], grid['nz']), order = 'F')

		return data, grid

	except IOError:
		print(('	Error reading file "{0}"'.format(file_name)))
		print('	Check if the file exists...')































