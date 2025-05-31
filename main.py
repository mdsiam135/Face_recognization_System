from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from train import Train
import tkinter
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition
from student import Student
from attendance import Attendance
from developer import Developer
from help import Help

    
    
class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        # Load and resize the image 1
        img1 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\header1.jpg")
        img1 = img1.resize((450, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Place the image on a label
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=450, height=128)
        

        # Load and resize the image 2
        img2 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\header2.jpg")
        img2 = img2.resize((450, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # Place the image on a label
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=450, y=0, width=450, height=128)
        
        # Load and resize the image2
        img3 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\header3.jpg")
        img3 = img3.resize((466, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        # Place the image on a label
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=900, y=0, width=466, height=128)


         # background image
        img4 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\bg1.jpg")
        img4 = img4.resize((1366, 710), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        # Place the image on a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=128, width=1366, height=710)
        
        
        title_lbl = Label(bg_img, text= "SR FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 27, "bold"), bg="white", fg ="red")
        title_lbl.place(x=0,y=0, width=1366, height=45)
        
         #==== Time =====
        def time():
             string = strftime('%H:%M:%S %p')
             lbl.config(text = string)
             lbl.after(1000, time)
        
        
        lbl = Label(title_lbl, font=("times new roman", 15, "bold"), bg="white", fg ="red")
        lbl.place(x=10,y=0, width=110, height=50)
        time()
        
        # student Button
        img5 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\students.jpg")
        img5 = img5.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        
        b1=Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.student_details)
        b1.place(x=150, y=100, width=180, height =180) 
        
        b1_1=Button(bg_img, text= "Students Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b1_1.place(x=150, y=250, width=180, height=40) 
        
        
         # Detect face Button
        img6 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\face_detector1.png")
        img6 = img6.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        
        b2=Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.face_data)
        b2.place(x=400, y=100, width=180, height =180) 
        
        b2_1=Button(bg_img, text= "Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b2_1.place(x=400, y=250, width=180, height=40) 
        
        
         #Face Attendance Button
        img7 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\attendance.jpg")
        img7 = img7.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        
        b3=Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendance_data)
        b3.place(x=650, y=100, width=180, height =180) 
        
        b3_1=Button(bg_img, text= "Attendace", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b3_1.place(x=650, y=250, width=180, height=40) 
        
        
        
        
         #Help Button
        img8 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\help2.jpg")
        img8 = img8.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        
        b3=Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.help_data)
        b3.place(x=900, y=100, width=180, height =180) 
        
        b3_1=Button(bg_img, text= "Help center", cursor="hand2", command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b3_1.place(x=900, y=250, width=180, height=40) 
        
        
        
         #Train Button
        img9 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\train.jpg")
        img9 = img9.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        
        b3=Button(bg_img, image=self.photoimg9, cursor="hand2" ,command=self.train_data)
        b3.place(x=150, y=320, width=180, height =180) 
        
        b3_1=Button(bg_img, text= "Train image", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b3_1.place(x=150, y=470, width=180, height=40) 
        
        
        #Photos face Button
        img10 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\photos.jpg")
        img10 = img10.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        
        b3=Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
        b3.place(x=400, y=320, width=180, height=180)
        
        b3_1=Button(bg_img, text= "Photos ", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b3_1.place(x=400, y=470, width=180, height=40)
        
        
         #Developer Button
        img11 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\developer.jpg")
        img11 = img11.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        
        b3=Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.Developer_data)
        b3.place(x=650, y=320, width=180, height =180) 
        
        b3_1=Button(bg_img, text= "Developer", cursor="hand2", command=self.Developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b3_1.place(x=650, y=470, width=180, height=40) 
        
        
        
         #Exit Button
        img12 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\exit.jpg")
        img12 = img12.resize((180, 180), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        
        b3=Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.iExit )
        b3.place(x=900, y=320, width=180, height =180)
        
        b3_1=Button(bg_img, text= "Exit", cursor="hand2", command=self.iExit , font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        b3_1.place(x=900, y=470, width=180, height=40)  

    def open_img(self):
        os.startfile("data")
   
   
   # Function
    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
       
    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window) 
    
    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app= Face_Recognition(self.new_window)
       
       
    def attendance_data(self):
       self.new_window=Toplevel(self.root)
       self.app= Attendance(self.new_window)
       
       
    def Developer_data(self):
       self.new_window=Toplevel(self.root)
       self.app= Developer(self.new_window)
       
    def help_data(self):
       self.new_window=Toplevel(self.root)
       self.app= Help(self.new_window)
   
    def iExit(self):
       self.iExit= tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent= self.root)
       if self.iExit>0:
          self.root.destroy()
       else:
          return   




if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
