'''
calibrate a camera using a directory of images including the 
calibration checkerboard, write the calibration to a yaml file
'''

import numpy as np
import cv2
import glob

WAIT_TIME = 250 # time to view the rendered image (milliseconds)

# note checkerboard dimensions are counted by the block intersections
# not the blocks themselves
CHECKER_DIM = [9, 6] # dimensions of the checkerboard

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CHECKER_DIM[1]*CHECKER_DIM[0],3), np.float32)
objp[:,:2] = np.mgrid[0:CHECKER_DIM[0],0:CHECKER_DIM[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

image_count = 1
images = glob.glob('calib_images/*.jpg')

for fname in images:

    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (CHECKER_DIM[0],CHECKER_DIM[1]),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        print("Found object points in image: " + str(image_count))

        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (CHECKER_DIM[0],CHECKER_DIM[1]), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(WAIT_TIME)

    image_count += 1



cv2.destroyAllWindows()
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

"""
print (mtx)

data = {"camera_matrix": mtx.tolist(), "dist_coeff": dist.tolist()}
fname = "calib_images/data.yaml"
with open(fname, "w") as f:
    yaml.dump(data, f)

print("Calibration Successful ! Written values to a file !")
"""

cv_file = cv2.FileStorage("calib_images/calibration.yaml", cv2.FILE_STORAGE_WRITE)

cv_file.write("camera_matrix", mtx)
cv_file.write("dist_coeff", dist)

print("Wrote calibration to file.")

# note you *release* you don't close() a FileStorage object
cv_file.release()


