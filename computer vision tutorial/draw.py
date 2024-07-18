import cv2
import numpy as np

blank=np.zeros(img.shape[:2],dtype='unit8')
cv2.imshow(blank)
cv2.waitKey(0)

#draw reatcangle in the image
rect=cv2.rectangle(blank,(0,0),(255,255),(0,0,255),2)
cv2.imshow(rect)
cv2.waitKey(0)

#draw circle in the image
cicle=cv2.circle(blank,(255,255),100,(0,255,0),3)
cv2.imshow(circle)
cv2.waitKey(0)

#draw the line in the image
line=cv2.line(blank,(0,0),(255,255),(255,0,0),2)
cv2.imshow(line)
cv2.waitKey(0)

