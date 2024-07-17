import cv2
img_path = (r"C:\Users\tragu\PycharmProjects\pythonProject\jolie.jpg")
img = cv2.imread(img_path)
cv2.imshow('img', img)
cv2.waitKey(0)

video_path=(r"C:\Users\tragu\OneDrive\Documents\animal detection.mp4")

video=cv2.VideoCapture(video_path)

while  True:
    isTrue,frame= video.read()
    cv2 .imshow('video',frame)
    if cv2.waitKey(25)&0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()