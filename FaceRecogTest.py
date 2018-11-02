import cv2
import numpy as numpy
import tkinter
from tkinter import messagebox
import time
import csv
start_time = time.time()

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('trainingData.yml')

id = 0
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (0,0,255)
flag = 0
filename = "data/DBNames.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row[1])

num_row = csvreader.line_num - 1

id_map = rows

print(id_map)

cam = cv2.VideoCapture(0)
window = tkinter.Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        cv2.putText(img,str(id_map[id-1]) + '_' + str(conf),(x,y+h),fontFace,fontScale,fontColor)
        if conf >= 70 and conf<=100:
            print (conf)
            print (str(id_map[id-1]))
            flag = 1
    cv2.imshow("face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
    elif time.time() - start_time >= 100:
        break
    elif flag:
        cam.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Information","Access Granted")
        exit()
if flag == 0:
    cam.release()
    cv2.destroyAllWindows()
    messagebox.showerror("Information","Access Denied")
