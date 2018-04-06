import cv2
import numpy as np

img_rgb = cv2.imread('123.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('1 (2).jpg',0)
w, h = template.shape[::-1]

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray,img_gray,cv2.TM_CCOEFF_NORMED)
    threshold = 0.4
    loc = np.where( res >= threshold)
    print(loc)
    for pt in zip(*loc[::-1]):
        
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
    
    cv2.imshow('Detected',frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break