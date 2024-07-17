import cv2
import numpy as np

image=(r"C:\Users\tragu\PycharmProjects\pythonProject\jolie.jpg")
img=cv2.imread(image)
#cv2.imshow('img',img)
cv2.waitKey(0)

#define translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMat,dimension)

#translate the image
translated=translate(img,-30,25)
cv2.imshow('translated',translated)
cv2.waitKey(0)

#rotate the image
rotated=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotated',rotated)
cv2.waitKey(0)

#flipping the image
flip=cv2.flip(img,1)
cv2.imshow('fliped',flip)
cv2.waitKey(0)