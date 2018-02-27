# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
#video_src = 'dataset/video1.avi'
video_src = 'dataset/video1.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
count = 0


while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    cv2.line(img,(0,100),(640,100),(0,0,255),1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.line(img,(x+(w/2),y+(h/2)),(x+(w/2),y+(h/2)),(0,255,0),2)

        if (100<y+(h/2)<105):
  			count +=1
  			print(count)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()






