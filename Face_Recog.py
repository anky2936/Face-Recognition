import numpy as np
import cv2

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sampleNum = 0
uid = input('enter user id : ')
cam = cv2.VideoCapture(0)

while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)#it will create image pyramid, it will scale the distance of object from camera
    for (x,y,w,h) in faces:
        sampleNum += 1
        cv2.imwrite('dataset/' + str(uid) + '_' + str(sampleNum) + '.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow('face',img)
    cv2.waitKey(1)
    if(sampleNum>50):
        break

cam.release()
cv2.destroyAllWindows()
