import numpy as np
import cv2 as cv
import glob
# # termination criteria
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# objp = np.zeros((6*8,3), np.float32)
# objp[:,:2] = np.mgrid[0:6,0:8].T.reshape(-1,2)

# # Arrays to store object points and image points from all the images.
# objpoints = [] # 3d point in real world space
# imgpoints = [] # 2d points in image plane.

# images = glob.glob('*.png')

# for fname in images:
#     img = cv.imread(fname)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # Find the chess board corners
#     ret, corners = cv.findChessboardCornersSB(gray, (6,8), None)
#     # If found, add object points, image points (after refining them)
#     if ret == True:
#         objpoints.append(objp)
#         corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
#         imgpoints.append(corners2)
#         # Draw and display the corners
#         cv.drawChessboardCorners(img, (6,8), corners2, ret)
#         #cv.namedWindow('img', cv.WINDOW_NORMAL)
#         cv.imshow('img', img)
        
#         cv.waitKey(500)
#     else:
#         print(fname)
        
# cv.destroyAllWindows()

# ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# print("ret:\n", ret, "\n mtx:\n", mtx, "\n dist:\n",dist,"\n rvecs:\n", rvecs, "\n tvecs:\n",tvecs)

mtx =  np.array([[613.88367983, 0, 319.21787006],[0, 614.31059499, 202.28879716],[0, 0, 1]])
dist =  np.array([[-0.37703544,  0.31425025, -0.00366991, -0.00103216, -0.28197977]])

# cap = cv.VideoCapture(1)  # 0 for the first webcam, 1 for the second one, etc.
# ret, img = cap.read()  # read a new frame from video
# cap.release()  # after capturing the image, release the camera

# if not ret:
#     print("Unable to capture image")
# h,  w = img.shape[:2]
# newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

import time

import cv2 as cv
import numpy as np

# Assuming mtx and dist are defined somewhere else in the code
# mtx is the camera matrix
# dist is the distortion coefficients

cap = cv.VideoCapture(1)  # 0 for the first webcam, 1 for the second one, etc.

while True:
    ret, img = cap.read()  # read a new frame from video

    if not ret:  # if frame read successfully
        print("Unable to capture image")
        break

    h,  w = img.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    print(newcameramtx)

    # undistort
    dst = cv.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]

    cv.imshow('calibresult', dst)

    if cv.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
        break

cap.release()
cv.destroyAllWindows()


# img = cv.imread('output.png')
# h,  w = img.shape[:2]
# print(w,h)
# newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# # undistort
# dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('calibresult2.png', dst)











