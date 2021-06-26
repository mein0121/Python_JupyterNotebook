import cv2
import sys
url = 'http://192.168.0.38:9999/?action=stream'
cap=cv2.VideoCapture(url)

if not cap.isOpened():
    sys.exit()
while True:
    ret, img = cap.read()
    if ret:
        img = cv2.flip(img,1)
        cv2.imshow('img', img)

        if cv2.waitKey(1) > 0:
            break


cap.release()
cv2.destroyAllWindows()