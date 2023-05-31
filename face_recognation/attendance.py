from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
#Set up Window
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")

        #Text Variable
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()






        # img=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\smart-attendance.jpg")
        # img=img.resize((680,100),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # #Create Label
        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=680,height=100)

        # #Second Image
        # img1=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\student3.jpg")
        # img1=img1.resize((680,100),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=680,y=0,width=680,height=100)

        img3=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\bgimg.jpg")
        img3=img3.resize((1360,640),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1360,height=640)

        lbl_title= Label(bg_img,text="ATTENDNCE SYSTEM",font=("times new romen",30,"bold"),bg="yellow",fg="red")
        lbl_title.place(x=0,y=3,width=1360,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=1360,height=560)

        left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new romen",14,"bold"))
        left_frame.place(x=10,y=20,width=640,height=550)

        img_left=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Attendance.jpeg")
        img_left=img_left.resize((640,110),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=640,height=110)

        left_inside=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside.place(x=0,y=135,width=630,height=410)

        Attendanceid=Label(left_inside,text="Attendance Id",font=("times new romen",13,"bold"),bg="white")
        Attendanceid.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside,textvariable=self.var_atten_id,width=15,font=("times new romen",13,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        rollLabel=Label(left_inside,text="Roll",font=("times new romen",13,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside,textvariable=self.var_atten_roll,width=15,font=("times new romen",13,"bold"))
        roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        nameLabel=Label(left_inside,text="Name",font=("times new romen",13,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside,textvariable=self.var_atten_name,width=15,font=("times new romen",12,"bold"))
        name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        deptLabel=Label(left_inside,text="Department",font=("times new romen",13,"bold"),bg="white")
        deptLabel.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        dept_entry=ttk.Entry(left_inside,textvariable=self.var_atten_dep,width=15,font=("times new romen",12,"bold"))
        dept_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        timeLabel=Label(left_inside,text="Time",font=("times new romen",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside,textvariable=self.var_atten_time,width=15,font=("times new romen",12,"bold"))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        dateLabel=Label(left_inside,text="Date",font=("times new romen",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside,textvariable=self.var_atten_date,width=15,font=("times new romen",12,"bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        attendanceLabel=Label(left_inside,text="Attendance Status",bg="white",font=("times new romen",13,"bold"))
        attendanceLabel.grid(row=3,column=0)

        self.attend_status=ttk.Combobox(left_inside,textvariable=self.var_atten_attendance,width=15,font=("times new romen",12,"bold"))
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.grid(row=3,column=1,padx=10,pady=10)
        self.attend_status.current(0)

        btn_frame=Frame(left_inside,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=650,height=177)

        save_btn=Button(btn_frame,text="Import",command=self.importCsv,width=15,font=("times new romen",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export",command=self.exportCsv,width=15,font=("times new romen",12,"bold"),bg="dark green",fg="White")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new romen",12,"bold"),bg="yellow",fg="White")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new romen",12,"bold"),bg="Red",fg="White")
        reset_btn.grid(row=0,column=3)

        #Right Frame
        right_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new romen",14,"bold"))
        right_frame.place(x=665,y=15,width=715,height=500)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=695,height=445)

        #Scroll Bar and Table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #Fetch Date
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Date","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Date Exported Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")









if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
  
