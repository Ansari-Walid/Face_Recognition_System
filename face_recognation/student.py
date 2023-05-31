
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

#Set up Window
class Student:
    def __init__(self,root):
        #self.variable = ttk.StringVar()
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")
        
        #variables for database
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_div=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_city=StringVar()
        self.var_gender=StringVar()
        self.var_rollno=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()

        def Checkname():
            name=studentname_entry.get()
            if name.isalpha() == True:
                pass
            else:
                messagebox.showerror("Error","please enter a valid name")
        def Checkroll():
            rollno=studentrollno_entry.get()
            if len(rollno) == 9:
                pass
            else:
                messagebox.showerror("Error","Rollno should Contain 9 Characters Only")
        def Checkcity():
            city=Student_city_entry.get()
            if city.isalpha() == False:
                messagebox.showerror("Error","City Name Should Contain Alphabets Only")
        def phone():
            phno=studentphone_entry.get()
            if len(phno) > 10 or len(phno) < 10:
                messagebox.showerror("Error","Phone Number should Contain 10 digits Only")
          
        #Set Top Image Path
        # img=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\face-recognition.png")
        # img=img.resize((455,100),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # #Create Label
        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=455,height=100)

        # #Second Image
        # img1=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\smart-attendance.jpg")
        # img1=img1.resize((455,100),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=455,y=0,width=455,height=100)

        # #Third Image
        # img2=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\student3.jpg")
        # img2=img2.resize((455,100),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=910,y=0,width=455,height=100)

        #bg Image
        img3=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\bgimg.jpg")
        img3=img3.resize((1360,640),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1360,height=640)

        #title
        lbl_title= Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new romen",30,"bold"),bg="yellow",fg="red")
        lbl_title.place(x=0,y=0,width=1360,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=37,width=1355,height=700)

        #Left Label Frame
        left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romen",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=700)

        #image Left
        img_left=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Attendance.jpeg")
        img_left=img_left.resize((650,110),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=650,height=110)

        #current course info
        current_course = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new romen",12,"bold"))
        current_course.place(x=10,y=115,width=650,height=120)

        #Department
        dep_label=Label(current_course,text="Department",font=("times new romen",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new romen",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CMPN","INFT","EXTC","BIOM")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course,text="Year",font=("times new romen",13,"bold"),bg="white")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new romen",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","FE","SE","TE","BE")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Div
        div_label=Label(current_course,text="Division",font=("times new romen",13,"bold"),bg="white")
        div_label.grid(row=1,column=0,padx=10,sticky=W)

        div_combo=ttk.Combobox(current_course,textvariable=self.var_div,font=("times new romen",12,"bold"),state="readonly",width=20)
        div_combo["values"]=("Select Division","A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course,text="Semester",font=("times new romen",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new romen",12,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_student = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new romen",12,"bold"))
        class_student.place(x=10,y=240,width=650,height=300)

        #Studentid
        Studentid=Label(class_student,text="Student Id",font=("times new romen",13,"bold"),bg="white")
        Studentid.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        studentid_entry=ttk.Entry(class_student,textvariable=self.var_id,width=20,font=("times new romen",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        student_name=Label(class_student,text="Student Name",font=("times new romen",13,"bold"),bg="white")
        student_name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student,validatecommand=Checkname,validate="focusout",textvariable=self.var_name,width=20,font=("times new romen",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #City
        Student_city=Label(class_student,text="City",font=("times new romen",13,"bold"),bg="white")
        Student_city.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Student_city_entry=ttk.Entry(class_student,validatecommand=Checkcity,validate="focusout",textvariable=self.var_city,width=20,font=("times new romen",12,"bold"))
        Student_city_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Rollno
        Student_rollno=Label(class_student,text="Roll No",font=("times new romen",13,"bold"),bg="white")
        Student_rollno.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentrollno_entry=ttk.Entry(class_student,validatecommand=Checkroll,validate="focusout",textvariable=self.var_rollno,width=20,font=("times new romen",12,"bold"))
        studentrollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Student_gender=Label(class_student,text="Gender",font=("times new romen",13,"bold"),bg="white")
        Student_gender.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student,textvariable=self.var_gender,font=("times new romen",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        Student_dob=Label(class_student,text="Date Of Birth",font=("times new romen",13,"bold"),bg="white")
        Student_dob.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdob_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=20,font=("times new romen",12,"bold"))
        studentdob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        Student_email=Label(class_student,text="Email",font=("times new romen",13,"bold"),bg="white")
        Student_email.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentemail_entry=ttk.Entry(class_student,textvariable=self.var_email,width=20,font=("times new romen",12,"bold"))
        studentemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone
        Student_phone=Label(class_student,text="Phone No",font=("times new romen",12,"bold"),bg="white")
        Student_phone.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentphone_entry=ttk.Entry(class_student,validatecommand=phone,validate="focusout",textvariable=self.var_phone,width=20,font=("times new romen",12,"bold"))
        studentphone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #button frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=650,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new romen",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new romen",12,"bold"),bg="green",fg="White")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new romen",12,"bold"),bg="red",fg="White")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new romen",12,"bold"),bg="yellow",fg="White")
        reset_btn.grid(row=0,column=3)

        #button Frame 2
        btn_frame1= Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=210,width=650,height=30)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=65,font=("times new romen",12,"bold"),bg="blue",fg="White")
        take_photo_btn.grid(row=0,column=0)

        #update_photo_btn=Button(btn_frame1,text="Save",width=35,font=("times new romen",12,"bold"),bg="blue",fg="White")
        #update_photo_btn.grid(row=0,column=1)


        #Right Label Frame
        right_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romen",12,"bold"))
        right_frame.place(x=680,y=10,width=700,height=500)

        #Right Frame Image
        img_right=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\student.jpg")
        img_right=img_right.resize((700,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=650,height=100)

        #Search Frame
        Search_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        Search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new romen",15,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new romen",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Search By","Rollno","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new romen",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("times new romen",12,"bold"),bg="blue",fg="White")
        search_btn.grid(row=0,column=3,padx=4)


        #Table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=700,height=280)

        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","year","div","sem","id","name","city","rollno","gender","dob","email","phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("city",text="City")
        self.student_table.heading("rollno",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("city",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #add Data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_phone.get()=="" or self.var_email.get()=="" or self.var_dob.get()=="" or self.var_rollno.get()=="" or self.var_city.get()=="" or self.var_year.get()=="Select Year" or self.var_div.get()=="Select Division" or self.var_sem.get()=="Select Semester" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required to Fill",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Walid@541",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_year.get(),self.var_div.get(),self.var_sem.get(),self.var_id.get(),self.var_name.get(),self.var_city.get(),
                self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Walid@541",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    #  Click on Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_div.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_city.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),

    # Update Button Cursor
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_phone.get()=="" or self.var_email.get()=="" or self.var_dob.get()=="" or self.var_rollno.get()=="" or self.var_city.get()=="" or self.var_year.get()=="Select Year" or self.var_div.get()=="Select Division" or self.var_sem.get()=="Select Semester" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required to Fill",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update the Data",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Walid@541",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set `dep`=%s,`year`=%s,`div`=%s,`sem`=%s,`city`=%s,`name`=%s,`rollno`=%s,`gender`=%s,`dob`=%s,`email`=%s,`phone`=%s where `id`=%s",(
                    self.var_dep.get(),self.var_year.get(),self.var_div.get(),self.var_sem.get(),self.var_city.get(),self.var_name.get(),
                    self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_id.get()

                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete Button Cursor
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete This Data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Walid@541",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql= "delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_div.set("Select Division")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_city.set("")
        self.var_rollno.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")


    #generate Data set and Take photo Samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_phone.get()=="" or self.var_email.get()=="" or self.var_dob.get()=="" or self.var_rollno.get()=="" or self.var_city.get()=="" or self.var_year.get()=="Select Year" or self.var_div.get()=="Select Division" or self.var_sem.get()=="Select Semester" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required to Fill",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Walid@541",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                s_id=0
                for x in my_result:
                    s_id+=1
                my_cursor.execute("update student set `dep`=%s,`year`=%s,`div`=%s,`sem`=%s,`city`=%s,`name`=%s,`rollno`=%s,`gender`=%s,`dob`=%s,`email`=%s,`phone`=%s where `id`=%s",(
                self.var_dep.get(),self.var_year.get(),self.var_div.get(),self.var_sem.get(),self.var_city.get(),self.var_name.get(),
                self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_id.get()==s_id+1

                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #Load Predefined Data on Face from frontal from open cv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name="Data/user."+str(s_id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)#number on camera
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==27 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed Succssfully!!!")
            except Exception as es:
                messagebox.showerror("Error"f"Due To:{str(es)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
