import numpy as np

def downsample_data(data, downX, downY, imageX, imageY):

	new_dims = [int(np.around((data.shape[0] * imageX) / downX)), int(np.around(((data.shape[1] * imageY) / downY)))]
	downsample_data = np.around(compress_and_average(data, new_dims), 3)

	return downsample_data

def compress_rows(old_dimension, new_dimension):

	# Name: compress_rows
	# Description:
	#	This function produces an array to downsample data to given dimensions.
	#	The new dimension does not have to be a factor of the new dimension


	print(new_dimension, old_dimension)

	dim_compressor 	= np.zeros((int(new_dimension), int(old_dimension)))
	bin_size 		= float(old_dimension) / new_dimension
	next_bin_break	= bin_size
	which_row 		= 0
	which_column	= 0

	while which_row < dim_compressor.shape[0] and which_column < dim_compressor.shape[1]:
		if round(next_bin_break - which_column, 10) >= 1:
			dim_compressor[which_row, which_column] = 1
			which_column += 1
		elif next_bin_break == which_column:
			which_row += 1
			next_bin_break += bin_size
		else:
			partial_credit = next_bin_break - which_column
			dim_compressor[which_row, which_column] = partial_credit
			which_row += 1
			dim_compressor[which_row, which_column] = 1 - partial_credit
			which_column += 1
			next_bin_break += bin_size

	dim_compressor /= bin_size
	return dim_compressor

def compress_columns(old_dimension, new_dimension):

	# Name: compress_columns
	# Description:
	#	Uses compress_rows on the transposed dataset.

	return compress_rows(old_dimension, new_dimension).transpose()

def compress_and_average(data, new_shape):

	# Name: compress_and_average
	# Description:
	#	This function downsamples data by calling compress_rows and compress_columns to produce to matrices
	#	to multiply the data matrix by to downsample it to the specified dimensions / scale.

	return np.mat(compress_rows(data.shape[0], new_shape[0])) * \
		   np.mat(data) * \
		   np.mat(compress_columns(data.shape[1], new_shape[1]))


