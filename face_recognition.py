from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from time import strftime
from datetime import datetime
import cv2
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Training System")
        
        title_lbl = Label(self.root, text= "FACE  RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg ="green")
        title_lbl.place(x=0,y=0, width=1366, height=45)
        
        
        # 1st image
        img_top = Image.open(r"images\face5.webp")
        img_top = img_top.resize((666, 700), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl4 = Label(self.root, image=self.photoimg_top)
        f_lbl4.place(x=0, y=50, width=666, height=700)
        
      
        # 2nd image
        img_bottom = Image.open(r"images\face2.jpg")
        img_bottom = img_bottom.resize((700, 700), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl4 = Label(self.root, image=self.photoimg_bottom)
        f_lbl4.place(x=666, y=50, width=700, height=700)  
        
        # Button 
        b1_1=Button(self.root, text= "Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 17, "bold"), bg="darkblue", fg ="white")
        b1_1.place(x=600, y=600, width=200, height=60)  
        
        
        #=====Attendance =====
    def mark_attendance(self, i,n,d,b):
        with open("si.csv", "r+", newline="\n") as f:
            myDataList= f.readlines()
            name_list=[]
            for line in myDataList:
                entry= line.split((","))
                name_list.append(entry[0])
                
            if((i not  in name_list)) and (n not  in name_list) and (d not  in name_list) and (b not  in name_list):
                now= datetime.now()
                d1= now.strftime("%d/%m/%Y")
                dtString= now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{b},{dtString},{d1},Present")
    
       
        # face recognition
        
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor, minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 3)
                id,predict= clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(
                       host="localhost",
                       username="root",
                       password="",
                       database="face_recognition"
                        )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name FROM `student` WHERE Student_id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)
                my_cursor.execute("SELECT Student_id FROM `student` WHERE Student_id="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)
                my_cursor.execute("SELECT Dep FROM `student` WHERE Student_id="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)
                my_cursor.execute("SELECT batch FROM `student` WHERE Student_id="+str(id))
                b = my_cursor.fetchone()
                b="+".join(b)
                
                
                if confidence>80:
                     cv2.putText(img, f"ID: {i}",(x,y-90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                     cv2.putText(img, f"Name: {n}",(x,y-60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                     cv2.putText(img, f"Department: {d}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                     cv2.putText(img, f"Batch: {b}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                     self.mark_attendance(i,n,d,b)
                else:
                     cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 2)
                     cv2.putText(img, "Unknown Face",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 3)
                
                coord=[x,y,w,h]
                
            return coord             
            
        def recognize(img, clf, faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10, (255,25,255), "Face", clf)
            return img
        
        faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap= cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img= recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
        


                                                                          
                                                                                 
                                                                                 
                                                                                 
                                                                                 
if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()