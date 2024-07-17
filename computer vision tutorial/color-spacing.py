import cv2
import numpy as np

image=(r"C:\Users\tragu\PycharmProjects\pythonProject\jolie.jpg")
img=cv2.imread(image)
cv2.imshow('img',img)
cv2.waitKey(0)

#converting bgr to gray scale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey(0)

#converting to  bgr to hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)

#conerting to lab
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow('lab',lab)
cv2.waitKey(0)

#converting bgr to rgb
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('rgb',rgb)
cv2.waitKey(0)