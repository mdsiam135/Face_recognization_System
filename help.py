from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help Center")
        
        
        title_lbl = Label(self.root, text= "HELP CENTER", font=("times new roman", 30, "bold"), bg="white", fg ="darkblue")
        title_lbl.place(x=0,y=0, width=1366, height=45)
        
        img_top = Image.open(r"images\help2.jpg")
        img_top = img_top.resize((1366, 600), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl4 = Label(self.root, image=self.photoimg_top)
        f_lbl4.place(x=0, y=50, width=1366, height=600) 
        
        
        title_lbl = Label(f_lbl4, text= "Email: mdsimonsarkar135@gmail.com", font=("times new roman", 30, "bold"), bg="white", fg ="blue")
        title_lbl.place(x=370,y=320)
        title_lbl1 = Label(f_lbl4, text= "WhatsApp: 01796-775714", font=("times new roman", 30, "bold"), bg="white", fg ="blue")
        title_lbl1.place(x=440,y=380)
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Help(root)
    root.mainloop()