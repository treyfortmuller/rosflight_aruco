'''
Generate all the aruco markers in the 4X4_50 dictionary
and save them to a directory, will throw an error if the
directory already exists
'''

import numpy as np
import cv2
import cv2.aruco as aruco
import os

# create a directory to fill with the markers
dirname = "markers"
os.mkdir(dirname)
 
# aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250) # for the 6x6 dictionary
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

for i in range(0, 50):
	# generate markers (dictionary to use, ID number, pixels)
	img = aruco.drawMarker(aruco_dict, i, 500)
	cv2.imwrite(os.path.join(dirname, "4x4marker_" + str(i) + ".png"), img)