import numpy as np
import imutils

def rotate_data(data, angle):

	rotated_data = np.asarray(data, dtype = "uint8")
	rotated_data = imutils.rotate_bound(rotated_data, angle)
	return rotated_data
