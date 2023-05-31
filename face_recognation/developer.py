from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


#Set up Window
class Developer:
    def __init__(self,root):
        #self.variable = ttk.StringVar()
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Developer",font=("times new romen",35,"bold"),fg="red")
        title_lbl.place(x=0,y=0,width=1360,height=40)

        img=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\wbackground.jpg")
        img=img.resize((1360,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=42,width=1360,height=700)

        #Developer info 3
        main_frame3=Frame(f_lbl,bd=2,bg="moccasin")
        main_frame3.place(x=900,y=95,width=400,height=450)

        img1=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\female.png")
        img1=img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(main_frame3,image=self.photoimg1,justify=LEFT)
        f_lbl1.place(x=100,y=42,width=200,height=200)

        lbl_title= Label(main_frame3,text="NAME:",font=("times new romen",12,"bold"),bg="white",fg="black",justify=CENTER)
        lbl_title.place(x=40,y=270,width=100,height=20)

        lbl_name3=Label(main_frame3,text="Zobia Ansari",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        lbl_name3.place(x=180,y=270,width=110,height=20)

        roll_title1= Label(main_frame3,text="Roll NO :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        roll_title1.place(x=40,y=315,width=100,height=20)

        roll_name=Label(main_frame3,text="20102A2010",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        roll_name.place(x=180,y=315,width=110,height=20)

        dept_title1= Label(main_frame3,text="DEPT :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        dept_title1.place(x=40,y=360,width=100,height=20)

        dept_name=Label(main_frame3,text="CMPN",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        dept_name.place(x=180,y=360,width=110,height=20)

        div_title1= Label(main_frame3,text="DIV :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        div_title1.place(x=40,y=400,width=100,height=20)

        div_name=Label(main_frame3,text="A",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        div_name.place(x=180,y=400,width=110,height=20)


        #Developer info 2
        #dev_label=Label(main_frame3,font=("times new romen",12,"bold"),bg="white")
        #ev_label.place(x=0,y=5)

        main_frame2=Frame(f_lbl,bd=2,bg="moccasin")
        main_frame2.place(x=480,y=95,width=400,height=450)

        img2=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\female.png")
        img2=img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(main_frame2,image=self.photoimg2,justify=CENTER)
        f_lbl2.place(x=100,y=42,width=200,height=200)

        lbl_title1= Label(main_frame2,text="NAME :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        lbl_title1.place(x=40,y=270,width=100,height=20)

        lbl_name=Label(main_frame2,text="Nikita Kamble",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        lbl_name.place(x=180,y=270,width=110,height=20)

        roll_title1= Label(main_frame2,text="Roll NO :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        roll_title1.place(x=40,y=315,width=100,height=20)

        roll_name1=Label(main_frame2,text="20102A2008",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        roll_name1.place(x=180,y=315,width=110,height=20)

        dept_title1= Label(main_frame2,text="DEPT :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        dept_title1.place(x=40,y=360,width=100,height=20)

        dept_name1=Label(main_frame2,text="CMPN",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        dept_name1.place(x=180,y=360,width=110,height=20)

        div_title1= Label(main_frame2,text="DIV :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        div_title1.place(x=40,y=400,width=100,height=20)

        div_name1=Label(main_frame2,text="A",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        div_name1.place(x=180,y=400,width=110,height=20)

        #dev_label=Label(main_frame2,text="Department",font=("times new romen",12,"bold"),bg="white")
        #dev_label.place(x=0,y=5)

        #Developer info 1
        main_frame1=Frame(f_lbl,bd=2,bg="moccasin")
        main_frame1.place(x=60,y=95,width=400,height=450)

        img3=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\male.png")
        img3=img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl2=Label(main_frame1,image=self.photoimg3,justify=CENTER)
        f_lbl2.place(x=100,y=42,width=200,height=200)

        lbl_title2= Label(main_frame1,text="NAME:",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        lbl_title2.place(x=40,y=270,width=100,height=20)

        lbl_name2=Label(main_frame1,text="Walid Ansari",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        lbl_name2.place(x=180,y=270,width=110,height=20)

        roll_title2= Label(main_frame1,text="Roll NO :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        roll_title2.place(x=40,y=315,width=100,height=20)

        roll_name2=Label(main_frame1,text="20102B2004",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        roll_name2.place(x=180,y=315,width=110,height=20)

        dept_title2= Label(main_frame1,text="DEPT :",font=("times new romen",12,"bold"),justify=LEFT,bg="white",fg="black")
        dept_title2.place(x=40,y=360,width=100,height=20)

        dept_name2=Label(main_frame1,text="CMPN",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        dept_name2.place(x=180,y=360,width=110,height=20)

        div_title2= Label(main_frame1,text="DIV :",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        div_title2.place(x=40,y=405,width=100,height=20)

        div_name2=Label(main_frame1,text="B",font=("times new romen",12,"bold"),bg="white",justify=LEFT,fg="black")
        div_name2.place(x=180,y=400,width=110,height=20)



        #dev_label=Label(main_frame1,text="Department",font=("times new romen",12,"bold"),bg="white")
        #dev_label.place(x=0,y=5)







if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
  