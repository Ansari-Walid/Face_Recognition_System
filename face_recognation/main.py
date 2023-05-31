from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from recognition import Recognition
from attendance import Attendance
from developer import Developer
from help import Help

#Set up Window
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")

        #Set Top Image Path
        img=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Stanford.jpg")
        img=img.resize((455,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        #Create Label
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=455,height=130)

        #Second Image
        img1=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\facialrecognition.png")
        img1=img1.resize((455,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=455,y=0,width=455,height=130)

        #Third Image
        img2=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\u.jpg")
        img2=img2.resize((455,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=910,y=0,width=455,height=130)

        # #bg Image
        img3=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\R.jpg")
        img3=img3.resize((1360,640),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1360,height=640)

        #title
        lbl_title= Label(bg_img,text="STUDENTIN- An Attendance System With Face Detection",font=("times new romen",26,"bold"),bg="yellow",fg="red")
        lbl_title.place(x=0,y=0,width=1360,height=35)

        #Student Button
        img4=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=100,y=260,width=200,height=30)
        
        #Detect Face Button
        img5=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\face_detector1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",command=self.face_data)
        b1_1.place(x=400,y=260,width=200,height=30)

        #Attendance Button
        img6=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Attendance.jpeg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=700,y=260,width=200,height=30)

        #Help Button
        img7=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Help.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1000,y=260,width=200,height=30)

        #Train Model Button
        img8=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Train.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=100,y=520,width=200,height=30)

        #Photos Model Button
        img9=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\photos.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=400,y=520,width=200,height=30)

        #Developer Model Button
        img10=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\Developer.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=700,y=520,width=200,height=30)

        #Exit Button
        img11=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1000,y=520,width=200,height=30)

    def open_img(self):
        os.startfile("Data")

        #Function Button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
    
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Recognition(self.new_window)

    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do You Want To Exit The Window",parent=self.root)
         if self.iExit > 0:
              self.root.destroy()
         else:
            return









if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        


