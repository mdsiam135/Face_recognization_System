from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Details")
        
        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_batch=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        # Load and resize the image 1
        img1 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\s_header1.jpg")
        img1 = img1.resize((450, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Place the image on a label
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=450, height=128)
        

        # Load and resize the image 2
        img2 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\s_header2.jpg")
        img2 = img2.resize((450, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # Place the image on a label
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=450, y=0, width=450, height=128)
        
        # Load and resize the image 3
        img3 = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\s_header3.jpg")
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
        
        title_lbl = Label(bg_img, text= "STUDENT DETAILS SYSTEM", font=("times new roman", 30, "bold"), bg="white", fg ="darkblue")
        title_lbl.place(x=0,y=0, width=1366, height=45)
        
        
        
        # Back button
        
        #b2_1=Button(title_lbl, text= "Back", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg ="white")
        #b2_1.place(x=1230, y=2, width=80, height=35) 
        
        #frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=50, width=1333, height=520)
        
        #left label frame
        Left_frame= LabelFrame(main_frame,bd=2,bg="white", relief=RAISED, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=6, y=10, width=655, height=500)
        
        
        img_left = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\s_header4.jpeg")
        img_left = img_left.resize((635, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl4 = Label(Left_frame, image=self.photoimg_left)
        f_lbl4.place(x=5, y=0, width=640, height=60)
        
        #current course frame
        Current_course_frame= LabelFrame(Left_frame,bd=2,bg="white", relief=RAISED, text="Current course informatiom", font=("times new roman", 12, "bold"))
        Current_course_frame.place(x=5, y=60, width=640, height=107)
        
        
        # Department
        dep_label = Label(Current_course_frame, text="Department", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=0,column=0, padx="10", sticky=W)
        
        dep_combo= ttk.Combobox(Current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "CSE", "BBA", "ENG", "LLB", "TFD")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx="2", pady="10", sticky=W)
        
        
        # Course
        course_label = Label(Current_course_frame, text="Course", font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=0,column=2, padx="10", sticky=W)
        
        course_combo= ttk.Combobox(Current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "NN", "DBMS", "CA","AI", "TOC", "CD", "ECWD", "PI", "SDTT")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx="2", pady="10", sticky=W)
        
        
        
        # batch
        batch_label = Label(Current_course_frame, text="Batch", font=("times new roman", 13, "bold"),bg="white")
        batch_label.grid(row=1,column=0, padx="10", sticky=W)
        
        batch_combo= ttk.Combobox(Current_course_frame,textvariable=self.var_batch, font=("times new roman", 12, "bold"), state="readonly", width=20)
        batch_combo["values"] = ("Select Batch",  "22", "23", "24", "25", "26", "27", "28", "29")
        batch_combo.current(0)
        batch_combo.grid(row=1, column=1, padx="2", pady="10", sticky=W)
        
        
        # Semester
        semester_label = Label(Current_course_frame, text="Semester", font=("times new roman", 13, "bold"),bg="white")
        semester_label.grid(row=1,column=2, padx="10", sticky=W)
        
        semester_combo= ttk.Combobox(Current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2",  "Semester-3", "Semester-4",  "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx="2", pady="10", sticky=W)
        
        
        #class student informatiom
        Class_student_frame= LabelFrame(Left_frame,bd=2,bg="white", relief=RAISED, text="class student informatiom", font=("times new roman", 12, "bold"))
        Class_student_frame.place(x=5, y=170, width=640, height=305)
        
        # Student ID 
        StudentId_label = Label(Class_student_frame, text="StudentID: ", font=("times new roman", 13, "bold"),bg="white")
        StudentId_label.grid(row=0,column=0, padx=2, sticky=W)
        
        StudentId_entry = ttk.Entry(Class_student_frame, width=20,textvariable=self.var_stu_id, font=("times new roman", 12, "bold") )
        StudentId_entry.grid(row=0, column=1, padx=2,pady=5, sticky=W)
        
        # Student name 
        StudentName_label = Label(Class_student_frame, text="Student Name: ", font=("times new roman", 13, "bold"),bg="white")
        StudentName_label.grid(row=0,column=2, padx=10, sticky=W)
        
        StudentName_entry = ttk.Entry(Class_student_frame,textvariable=self.var_stu_name, font=("times new roman", 12, "bold") )
        StudentName_entry.grid(row=0, column=3, padx=2,pady=5, sticky=W)
        
        # class division
        class_div_label = Label(Class_student_frame, text="Class Division: ", font=("times new roman", 13, "bold"),bg="white")
        class_div_label.grid(row=1,column=0, padx=2, sticky=W)
        
        div_combo= ttk.Combobox(Class_student_frame,textvariable=self.var_div, font=("times new roman", 12, "bold"), state="readonly", width=15)
        div_combo["values"] = ("A",  "B")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx="2", pady="2", sticky=W)
        
        # Roll No
        rollNo_label = Label(Class_student_frame, text="Roll No: ", font=("times new roman", 13, "bold"),bg="white")
        rollNo_label.grid(row=1,column=2, padx=10, sticky=W)
        
        rollNo_entry = ttk.Entry(Class_student_frame, width=20,textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=2,pady=5, sticky=W)
        
        # Gender 
        Gender_label = Label(Class_student_frame, text="Gender: ", font=("times new roman", 13, "bold"),bg="white")
        Gender_label.grid(row=2,column=0, padx=2, sticky=W)
        
        #Gender_entry = ttk.Entry(Class_student_frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold") )
        #Gender_entry.grid(row=2, column=1, padx=2,pady=5, sticky=W)
        
        gender_combo= ttk.Combobox(Class_student_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=15)
        gender_combo["values"] = ("Male",  "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx="2", pady="2", sticky=W)
        
        # Date of birth
        dob_label = Label(Class_student_frame, text="Date of birth:", font=("times new roman", 13, "bold"),bg="white")
        dob_label.grid(row=2,column=2, padx=10, sticky=W)
        
        dob_entry = ttk.Entry(Class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold") )
        dob_entry.grid(row=2, column=3, padx=2,pady=5, sticky=W)
        
        # Email
        Email_label = Label(Class_student_frame, text="Email:", font=("times new roman", 13, "bold"),bg="white")
        Email_label.grid(row=3,column=0, padx=2, sticky=W)
        
        Email_entry = ttk.Entry(Class_student_frame, width=20,textvariable=self.var_email, font=("times new roman", 12, "bold") )
        Email_entry.grid(row=3, column=1, padx=2, pady=5, sticky=W)
        
        # Phone no
        rollNo_label = Label(Class_student_frame, text="Phone no: ", font=("times new roman", 13, "bold"),bg="white")
        rollNo_label.grid(row=3,column=2, padx=10, sticky=W)
        
        rollNo_entry = ttk.Entry(Class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold") )
        rollNo_entry.grid(row=3, column=3, padx=2, pady=5, sticky=W)
        
        # Address 
        Gender_label = Label(Class_student_frame, text="Address: ", font=("times new roman", 13, "bold"),bg="white")
        Gender_label.grid(row=4,column=0, padx=2, sticky=W)
        
        Gender_entry = ttk.Entry(Class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold") )
        Gender_entry.grid(row=4, column=1, padx=2, pady=5, sticky=W)
        
         # Teacher Name 
        Teacher_Name_label = Label(Class_student_frame, text="Teacher Name : ", font=("times new roman", 13, "bold"),bg="white")
        Teacher_Name_label.grid(row=4,column=2, padx=10, sticky=W)
        
        Teacher_Name_entry = ttk.Entry(Class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold") )
        Teacher_Name_entry.grid(row=4, column=3, padx=2,pady=5, sticky=W)
          
       
       
        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1= ttk.Radiobutton(Class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
         

        radiobtn2= ttk.Radiobutton(Class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)
        
        #buttons frame
        btn_frame = Frame(Class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=630, height=38)
        
        save_btn= Button(btn_frame, text="Save",command=self.add_data, width=15,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn= Button(btn_frame, text="Update",command=self.update_data, width=15,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn= Button(btn_frame, text="Delete",command=self.delete_data ,  width=15,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn= Button(btn_frame, text="Reset",width=15, command=self.reset_data, cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        reset_btn.grid(row=0, column=3)
        
        
        #buttons frame
        btn_frame1 = Frame(Class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=240, width=630, height=40)
        
        take_photo_btn= Button(btn_frame1, text="Take photo sample",command=self.generate_dataset, width=32,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        take_photo_btn.grid(row=0, column=0)
        
        update_photo_btn= Button(btn_frame1, text="Update photo sample",width=32,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        update_photo_btn.grid(row=0, column=1)
        
         
        
        #Right label frame
        Right_frame= LabelFrame(main_frame,bd=2,bg="white", relief=RAISED, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=671, y=10, width=655, height=500)
        
        
        img_right = Image.open(r"C:\Users\HP-NPC\Desktop\AI\Face_recognization_System\images\students.jpg")
        img_right = img_right.resize((635, 128), Image.Resampling.LANCZOS)  # Updated resizing method
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl5 = Label(Right_frame, image=self.photoimg_right)
        f_lbl5.place(x=5, y=0, width=627, height=60)
        
        # search frame
        Search_frame= LabelFrame(Right_frame,bd=2,bg="white", relief=RAISED, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=65, width=627, height=70)
        
        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0,column=0, padx=5, sticky=W)
           
           
        search_combo= ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select" ,"Student_Id", "Student_Name", "Class_Division", "Roll_No", "Gender", "Date of Birth","Email", "Phone_No", "Teacher_Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx="2", pady="10", sticky=W)   
        
        
        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold") )
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)
           
        select_btn= Button(Search_frame, text="Search",width=10,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        select_btn.grid(row=0, column=3, padx=3)
        
        showAll_btn= Button(Search_frame, text="Show All",width=10,cursor="hand2", font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        showAll_btn.grid(row=0, column=4, padx=3)
        
        
        
        #table frame
        table_frame= Frame(Right_frame, bd=2, bg="white", relief=RAISED)
        table_frame.place(x=5, y=135, width=627, height=340)
        
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "batch", "sem", "id", "name","div", "roll", "gender",  "dob", "email","phone", "address", "teacher", "photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]= "headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("batch", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
        
        # function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                self.conn = mysql.connector.connect(
                       host="localhost",
                       user="root",
                       password="",
                       database="face_recognition"
                        )
                
                my_cursor = self.conn.cursor()
                my_cursor.execute("INSERT INTO `student` VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                        
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_batch.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_stu_id.get(),
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get() 
                                                                    
                                                                    
                                                                                                                 ))
        
                self.conn.commit()
                self.fetch_data()
                self.conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent= self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
        
        # Fetch data
    def fetch_data(self):
            conn = mysql.connector.connect(
                       host="localhost",
                       username="root",
                       password="",
                       database="face_recognition"
                        )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data= my_cursor.fetchall()
            
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
                conn.close()   
        
     # get cursor
    def get_cursor(self,event=""):
            cursor_focus = self.student_table.focus()
            content= self.student_table.item(cursor_focus)
            data = content["values"]
            
            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_batch.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_stu_id.set(data[4]),
            self.var_stu_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])
    
    
    # Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error", "All Feilds are required", parent=self.root)        
        else:
            try:
                Update= messagebox.askyesno("Update", "Do you want to update this students details", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(
                       host="localhost",
                       username="root",
                       password="",
                       database="face_recognition"
                        )
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE `student` SET Dep=%s,course=%s, batch=%s, Semester=%s, Name=%s, Division=%s, Roll=%s,Gender=%s,Dob=%s,Email=%s, Phone=%s, Address=%s, Teacher=%s,  PhotoSample=%s WHERE Student_id=%s",(
                        
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_batch.get(),
                                                                                                                                                                                                                        self.var_semester.get(),                                                                                                                                                                                                                      
                                                                                                                                                                                                                        self.var_stu_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_stu_id.get(),    
                      
                        
                                                                                                                                                                                                                       ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()    
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
                
    #delete function
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student must be required ", parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Student Delete Page", "Do you want to delete this student details?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                       host="localhost",
                       username="root",
                       password="",
                       database="face_recognition"
                        )
                    my_cursor = conn.cursor()
                    sql="DELETE FROM `student` WHERE Student_id=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)           
        
        
    # Reset function
    def reset_data(self):
            self.var_dep.set("Select Department")
            self.var_course.set("Select Course")
            self.var_batch.set("Select Batch")
            self.var_semester.set("Select Semester")
            self.var_stu_id.set("")
            self.var_stu_name.set("")
            self.var_div.set("Select division")
            self.var_roll.set("")
            self.var_gender.set("Male")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
            self.var_radio1.set("")
    
    
     # Generate data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error", "All Feilds are required", parent=self.root)        
        else:
            try:
               
                conn = mysql.connector.connect(
                       host="localhost",
                       username="root",
                       password="",
                       database="face_recognition"
                        )
                my_cursor = conn.cursor()
                # id=0 # <<< Incorrect ID calculation removed
                # for x in myresult:
                #     id+=1 # <<< Incorrect ID calculation removed
                # Commenting out potentially incorrect UPDATE query during dataset generation
                # my_cursor.execute("UPDATE `student` SET Dep=%s,course=%s, batch=%s, Semester=%s, Name=%s, Division=%s, Roll=%s,Gender=%s,Dob=%s,Email=%s, Phone=%s, Address=%s, Teacher=%s,  PhotoSample=%s WHERE Student_id=%s",(
                #         
                #                                                                                                                                                                                                                         self.var_dep.get(),
                #                                                                                                                                                                                                                         self.var_course.get(),
                #                                                                                                                                                                                                                         self.var_batch.get(),
                #                                                                                                                                                                                                                         self.var_semester.get(),                                                                                                                                                                                                                      
                #                                                                                                                                                                                                                         self.var_stu_name.get(),
                #                                                                                                                                                                                                                         self.var_div.get(),
                #                                                                                                                                                                                                                         self.var_roll.get(),
                #                                                                                                                                                                                                                         self.var_gender.get(),
                #                                                                                                                                                                                                                         self.var_dob.get(),
                #                                                                                                                                                                                                                         self.var_email.get(),
                #                                                                                                                                                                                                                         self.var_phone.get(),
                #                                                                                                                                                                                                                         self.var_address.get(),
                #                                                                                                                                                                                                                         self.var_teacher.get(),
                #                                                                                                                                                                                                                         self.var_radio1.get(),
                #                                                                                                                                                                                                                         self.var_stu_id.get()== id+1,   # <<< Incorrect condition
                      
                        
                #                                                                                                                                                                                                                        ))
                # conn.commit()
                # self.fetch_data() # Data fetching might be better after generation completes
                # self.reset_data() # Resetting data might be better after generation completes
                # conn.close() # Connection should be closed after all operations are done
                
                # Get the actual student ID from the form
                student_id = self.var_stu_id.get()

                # Load pre-defined face classifier
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor= 1.3 
                    #Minimum Neighbor = 5 
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped 

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        # Use the correct student_id obtained from the form field
                        file_name_path = "data/user."+str(student_id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Press Enter to stop
                        break

                cap.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("Result", "Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
                
                            
        
if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()