import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='optical flow tracker lucas-k method')
parser.add_argument('image', type=str, help='path to image file')
args = parser.parse_args()

cap = cv.VideoCapture(args.image)



# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))



# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  
   
    cv.imshow('frame',img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

   