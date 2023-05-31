from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


#Set up Window
class Help:
    def __init__(self,root):
        #self.variable = ttk.StringVar()
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Help Desk",font=("times new romen",35,"bold"),fg="red")
        title_lbl.place(x=0,y=0,width=1360,height=40)

        img=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img=img.resize((1360,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=42,width=1360,height=700)

        div_name2=Label(f_lbl,text="Email:ansari.wasim@vit.edu.in",font=("times new romen",12,"bold"),bg="white",fg="black")
        div_name2.place(x=600,y=400)













if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
  