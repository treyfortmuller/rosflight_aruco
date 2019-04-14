# Aruco Tracking

### Scripts

Currently does not include ROS functionality, development switched to the UAVs@Berkeley v2v-comm-v2 repository. 

1. **camera_calibration.py** : Shows the steps required to calibrate a camera using opencv default calibration images and writes the value to a file.
2. **extract_calibration.py**  : This script shows how to open and extract the calibration values from a file.
3. **pose_estimation.py**  : Steps to extract pose of a checkerboard for calibration.
4. **aruco_tracker.py** : Extracts pose of multiple aruco markers from a webcam stream.
5. **create_marker.py** : Creates an aruco marker based on the library and size specification, saves the library to a directory.

### Dependencies

- Python 3.x
- Numpy
- OpenCV 3.3+ 
- OpenCV 3.3+ Contrib modules

 

 

