import numpy as np

def channel_splitter(data, channel):

	if data.ndim > 2:

		if channel == "Red":
			new_data = data[:,:,0]
		elif channel == "Green":
			new_data = data[:,:,1]
		elif channel == "Blue":
			new_data = data[:,:,2]
		else:
			new_data = np.asarray(data)

		return new_data
	
	else:
		return data
