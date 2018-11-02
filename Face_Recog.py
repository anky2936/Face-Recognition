import numpy as np
import cv2
import pandas as pd
import getpass

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sampleNum = 0

attempt = 0
while(attempt!=3):
    password = getpass.getpass("Enter the password: ")
    if(password == "admin"):
        #df = pd.DataFrame(columns = ['UId','Name','Age','Phone No','Email Address'])
        #df.to_csv("data/DBNames.csv", index = False)

        uid = input("Enter your UserId : ")
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        phone = input("Enter your Phone No. : ")
        email = input("Enter your Email Address : ")

        rawData = {
            'UId' : [uid],
            'Name' : [name],
            'Age' : [age],
            'Phone No' : [phone],
            'Email Address' : [email]
        }
        df2 = pd.DataFrame(rawData)

        with open("data/DBNames.csv",'a') as file:
            df2.to_csv(file,index = False,header = False)
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
            if sampleNum>50 :
                break
        cam.release()
        cv2.destroyAllWindows()
        import FaceRecogTrain
        break
    else:
        attempt = attempt+1
        if attempt==3:
            print('You have tried maximum no. of times')

