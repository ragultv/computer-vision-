import cv2

#load the image
img_path = (r"C:\Users\tragu\PycharmProjects\pythonProject\jolie.jpg")
img = cv2.imread(img_path)
cv2.imshow('img', img)
cv2.waitKey(0)

#convert to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey(0)

#bluring image
blur=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT,)
cv2.imshow('blur',blur)
cv2.waitKey(0)

#edge cascade
canny=cv2.Canny(img,120,120)
cv2.imshow('canny',canny)
cv2.waitKey(0)

#dilating image
dilated=cv2.dilate(img,(5,5),iterations=2)
cv2.imshow('dilate',dilated)
cv2.waitKey(0)

#eroding image
erode=cv2.erode(img,(3,3),iterations=3)
cv2.imshow('eroded',erode)
cv2.waitKey(0)

#resize the image
resized =cv2.resize(img,(200,200))
cv2.imshow('resized',resized)
cv2.waitKey(0)

#cropping the image
cropped=img[50:200,100:200]
cv2.imshow('cropped',cropped)
cv2.waitKey(0)