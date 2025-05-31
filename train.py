from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Training System")
        
        
        title_lbl = Label(self.root, text= "TRAIN DATA SET", font=("times new roman", 30, "bold"), bg="white", fg ="purple")
        title_lbl.place(x=0,y=0, width=1366, height=45)
        # Back button
        
       # b2_1=Button(title_lbl, text= "Back", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
       # b2_1.place(x=1230, y=2, width=80, height=35)
        
        img_top = Image.open(r"images\train2.jpg")
        img_top = img_top.resize((1366, 320), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl4 = Label(self.root, image=self.photoimg_top)
        f_lbl4.place(x=0, y=50, width=1366, height=320)
        
        # Button 
        b1_1=Button(self.root, text= "TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg ="white")
        b1_1.place(x=0, y=370, width=1366, height=60) 
        
        img_bottom = Image.open(r"images\train4.jpg")
        img_bottom = img_bottom.resize((1366, 320), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl4 = Label(self.root, image=self.photoimg_bottom)
        f_lbl4.place(x=0, y=430, width=1366, height=320)
        
        
    def train_classifier(self):
        data_dir = ("data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprehensive 
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img= Image.open(image).convert('L')  #gray scale image
            imageNp= np.array(img, 'uint8')
            id= int(os.path.split(image)[1].split('.')[1])
        
        
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
                       
        ids= np.array(ids)   # NumPY for RMA convert . its give 88& performance batter 
        
        # train the classifier And Save===============
        
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!", parent= self.root)
        
            
        
    

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()