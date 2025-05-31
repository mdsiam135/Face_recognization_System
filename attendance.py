from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata= []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance System")
        
        # variables
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_batch=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()
        
       # 1st image
        img_top = Image.open(r"images\attend1.jpeg")
        img_top = img_top.resize((700, 200), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl4 = Label(self.root, image=self.photoimg_top)
        f_lbl4.place(x=0, y=0, width=700, height=200)
        
      
        # 2nd image
        img_bottom = Image.open(r"images\students.jpg")
        img_bottom = img_bottom.resize((700, 200), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl4 = Label(self.root, image=self.photoimg_bottom)
        f_lbl4.place(x=700, y=0, width=700, height=200)  
        
        
         # background image
        img4 = Image.open(r"images\bg1.jpg")
        img4 = img4.resize((1366, 710), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        # Place the image on a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1366, height=500)
        
        title_lbl = Label(self.root, text= "ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"), bg="white", fg ="green")
        title_lbl.place(x=0,y=200, width=1366, height=25)
        
        #frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=25, width=1333, height=470)
        
        #left label frame
        Left_frame= LabelFrame(main_frame,bd=2,bg="white", relief=RAISED, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=6, y=5, width=655, height=460)
        
        img_left = Image.open(r"images\s_header4.jpeg")
        img_left = img_left.resize((635, 100), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl4 = Label(Left_frame, image=self.photoimg_left)
        f_lbl4.place(x=5, y=0, width=635, height=100)
        
        left_inside_frame = Frame(Left_frame, bd=2,relief=RAISED, bg="white")
        left_inside_frame.place(x=10, y=105, width=630, height=330)
        
        # Label and entries 
        # Student ID 
        AttendanceId_label = Label(left_inside_frame, text="AttendanceID: ", font=("times new roman", 13, "bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0, padx=2, sticky=W)
        
        AttendanceId_entry = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_atten_id, font=("times new roman", 12, "bold") )
        AttendanceId_entry.grid(row=0, column=1, padx=2,pady=5, sticky=W)
        
        # Student name 
        StudentName_label = Label(left_inside_frame, text="Student Name: ", font=("times new roman", 13, "bold"),bg="white")
        StudentName_label.grid(row=0,column=2, padx=2, sticky=W)
        
        StudentName_entry = ttk.Entry( left_inside_frame,textvariable=self.var_atten_name, font=("times new roman", 12, "bold") )
        StudentName_entry.grid(row=0, column=3, padx=2,pady=5, sticky=W)
        
        # batch
        batch_label = Label(left_inside_frame, text="Batch:", font=("times new roman", 13, "bold"),bg="white")
        batch_label.grid(row=1,column=0, padx="5", sticky=W)
        
        batch_combo= ttk.Combobox(left_inside_frame,textvariable=self.var_atten_batch, font=("times new roman", 12, "bold"), state="readonly", width=17)
        batch_combo["values"] = ("Select Batch",  "22", "23", "24", "25", "26", "27", "28", "29")
        batch_combo.current(0)
        batch_combo.grid(row=1, column=1, padx="2", pady="5", sticky=W)
        
        # Department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=1,column=2, padx="5", sticky=W)
        
        dep_combo= ttk.Combobox(left_inside_frame,textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"), state="readonly", width=17)
        dep_combo["values"] = ("Select Department", "CSE", "BBA", "ENG", "LLB", "TFD")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx="2", pady="5", sticky=W)
        
        # time
        time_label = Label(left_inside_frame, text="Time: ", font=("times new roman", 13, "bold"),bg="white")
        time_label.grid(row=2,column=0, padx=2, sticky=W)
        
        time_entry = ttk.Entry(left_inside_frame, width=17,textvariable=self.var_time, font=("times new roman", 12, "bold") )
        time_entry.grid(row=2, column=1, padx=2,pady=2, sticky=W)
        
        # date 
        date_label = Label(left_inside_frame, text="Date: ", font=("times new roman", 13, "bold"),bg="white")
        date_label.grid(row=2,column=2, padx=5, sticky=W)
        
        date_entry = ttk.Entry( left_inside_frame,textvariable=self.var_date, font=("times new roman", 12, "bold") )
        date_entry.grid(row=2, column=3, padx=2,pady=5, sticky=W)
        
        # Attendance
        attend_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"),bg="white")
        attend_label.grid(row=3,column=0, padx="5", sticky=W)
        
        attend_combo= ttk.Combobox(left_inside_frame,textvariable=self.var_attendance, font=("times new roman", 12, "bold"), state="readonly", width=17)
        attend_combo["values"] = ("Status", "Present", "Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3, column=1, padx="2", pady="5", sticky=W)
        
         #buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=5, y=260, width=620, height=40)
        
        import_btn= Button(btn_frame, text="Import csv", command=self.importCsv, width=15,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        import_btn.grid(row=4, column=0)
        
        export_btn= Button(btn_frame, text="Export csv",command=self.exportCsv, width=15,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        export_btn.grid(row=4, column=1)
        
        update_btn= Button(btn_frame, text="Update",  width=15,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        update_btn.grid(row=4, column=2)
        
        reset_btn= Button(btn_frame, text="Reset",width=15,command=self.reset_data, cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        reset_btn.grid(row=4, column=3)
        
        
        #Right label frame
        Right_frame= LabelFrame(main_frame,bd=2,bg="white", relief=RAISED, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=671, y=5, width=655, height=460)
        
         #buttons frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=645, height=430)
        
        
        #scroll bar 
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendanceReportTable_table = ttk.Treeview(table_frame, column=( "id", "name","department", "batch", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable_table.xview)
        scroll_y.config(command=self.AttendanceReportTable_table.yview)
        
        
       
        self.AttendanceReportTable_table.heading("id", text="Attendance_ID")
        self.AttendanceReportTable_table.heading("name", text="Name")
        self.AttendanceReportTable_table.heading("department", text="Department")
        self.AttendanceReportTable_table.heading("batch", text="Batch")
        self.AttendanceReportTable_table.heading("time", text="Time")
        self.AttendanceReportTable_table.heading("date", text="Date")
        self.AttendanceReportTable_table.heading("attendance", text="Attendance")
        
        self.AttendanceReportTable_table["show"]= "headings"
        self.AttendanceReportTable_table.column("id", width=100)
        self.AttendanceReportTable_table.column("name", width=100)
        self.AttendanceReportTable_table.column("department", width=100)
        self.AttendanceReportTable_table.column("batch", width=100)
        self.AttendanceReportTable_table.column("time", width=100)
        self.AttendanceReportTable_table.column("date", width=100)
        self.AttendanceReportTable_table.column("attendance", width=100)
        
        self.AttendanceReportTable_table.pack(fill = BOTH, expand=1)
        self.AttendanceReportTable_table.bind("<ButtonRelease>", self.get_cursor)
     #fetch data 
    def fetchData(self,rows):
        self.AttendanceReportTable_table.delete(*self.AttendanceReportTable_table.get_children())
        for i in rows:
            self.AttendanceReportTable_table.insert("", END, values=i)
    
    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
        initialdir=os.getcwd(), 
        title="Open CSV", 
        filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], 
        parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(), 
            title="Open CSV", 
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], 
            parent=self.root)
            
            with open(fln, mode="w", newline="") as myfile:
                csvwrite= csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                    messagebox.showinfo("Data Export", "Your data exported to  "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)        
     
     
    # get cursor
    def get_cursor(self,event=""):
            cursor_focus = self.AttendanceReportTable_table.focus()
            content= self.AttendanceReportTable_table.item(cursor_focus)
            data = content["values"]
            
            self.var_atten_id.set(data[0])
            self.var_atten_name.set(data[1])
            self.var_atten_dep.set(data[2])
            self.var_atten_batch.set(data[3])
            self.var_time.set(data[4])
            self.var_date.set(data[5])
            self.var_attendance.set(data[6])
     
     # Reset function
    def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_batch.set("")
            self.var_time.set("")
            self.var_date.set("")
            self.var_attendance.set("")
            
    
        
        
        
        
        
        

if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()