from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Developer Details")
        
        
        title_lbl = Label(self.root, text= "DEVELOPERS", font=("times new roman", 30, "bold"), bg="white", fg ="blue")
        title_lbl.place(x=0,y=0, width=1366, height=45)
        
        img_top = Image.open(r"images\dev2.jpg")
        img_top = img_top.resize((1366, 600), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl4 = Label(self.root, image=self.photoimg_top)
        f_lbl4.place(x=0, y=50, width=1366, height=600) 
        
        
        # frame
        main_frame = Frame(f_lbl4, bd=2, bg="white")
        main_frame.place(x=830, y=20, width=510, height=550)
        
        """
        img_d1 = Image.open(r"images\d2.jpg")
        img_d1 = img_d1.resize((250, 300), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_d1 = ImageTk.PhotoImage(img_d1)
        
        f_lbl4 = Label(main_frame, image=self.photoimg_d1)
        f_lbl4.place(x=0, y=0, width=250, height=300)
        img_d2 = Image.open(r"images\d1.jpeg")
        img_d2 = img_d2.resize((250, 300), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_d2 = ImageTk.PhotoImage(img_d2)
        
        f_lbl4 = Label(main_frame, image=self.photoimg_d2)
        f_lbl4.place(x=260, y=0, width=250, height=300)
        """
        
        # label
        dep_label = Label(main_frame, text="Name:Md. Siam ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label.place(x=150, y=150)
        dep_label2 = Label(main_frame, text="Batch: 23 ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label2.place(x=150, y=180)
        dep_label5 = Label(main_frame, text="ID: 21300043 ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label5.place(x=150, y=210)

        # label
        dep_label = Label(main_frame, text="Name: Navid Hossain  ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label.place(x=10, y=320)
        dep_label2 = Label(main_frame, text="Batch: 23 ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label2.place(x=10, y=350)
        dep_label5 = Label(main_frame, text="ID: 21300059 ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label5.place(x=10, y=380)

        # label
        dep_label3 = Label(main_frame, text="Name: Afroza Akter ", font=("times new roman", 17, "bold"),bg="white", fg="darkblue")
        dep_label3.place(x=260, y=320)
        dep_label4 = Label(main_frame, text="Batch: 23 ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label4.place(x=260, y=350)
        dep_label6 = Label(main_frame, text="ID: 21300083 ", font=("times new roman", 17, "bold"),bg="white",fg="darkblue")
        dep_label6.place(x=260, y=380)
        
        
        dep_label7 = Label(main_frame, text="R. P. SHAHA UNIVERSITY ", font=("times new roman", 20, "bold"),bg="white",fg="Red")
        dep_label7.place(x=95, y=440)

if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()