#!/usr/bin/env python
import cv2
import numpy as np
import time
import sys
def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape)/2)
  rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_LINEAR)
  return result

def printMouseCoordinates(event, x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDBLCLK:
    print "Mouse: ",x,y


#angle = float(sys.argv[1])
winName = "water counter"
winName2 = "digit"
#cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
#cv2.namedWindow(winName2, cv2.CV_WINDOW_AUTOSIZE)
cam = cv2.VideoCapture(0)
cv2.setMouseCallback(winName,printMouseCoordinates)
cc = 0
while True:
  print cc
  #img = cv2.cvtColor(cam.read()[1],cv2.COLOR_RGB2GRAY)
  img = cam.read()[1]
  #img2 = rotateImage(img,angle)
  #img3 = img2[39:63,13:131]
  #img3 = img2[26:49,59:179]
  #scale = 4
  #img4 = cv2.resize(img3,(img3.shape[1]*scale, img3.shape[0]*scale),interpolation=cv2.INTER_LANCZOS4 )
  #img5 = cv2.adaptiveThreshold(img4,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,0)
  #img3 = img2[41:50,48:58]
  #cv2.imshow(winName,img)
  #cv2.imshow(winName2,img3)
  cv2.imwrite("images/image_{0:05d}.png".format(cc),img)
  time.sleep(0.5)
  cc += 1
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break


#Mouse:  41 48
#Mouse:  50 58


