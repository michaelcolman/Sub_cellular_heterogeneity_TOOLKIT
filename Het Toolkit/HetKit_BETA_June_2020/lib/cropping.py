from PIL import Image
import numpy as np

def crop_data(data, x1, x2, y1, y2):

	return data[y1:y2, x1:x2]


