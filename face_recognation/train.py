from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

#Set up Window
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")

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

        #Title
        lbl_title= Label(self.root,text="TRAIN DATA SET",font=("times new romen",30,"bold"),bg="yellow",fg="red")
        lbl_title.place(x=0,y=100,width=1360,height=35)

        #Top Img
        img_top=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\facialrecognition.png")
        img_top=img_top.resize((1350,250),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=135,width=1360,height=250)

        #button
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="yellow")
        b1_1.place(x=0,y=385,width=1360,height=55)
        

        #bottom Img
        img_bottom=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\images.jpg")
        img_bottom=img_bottom.resize((1350,250),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1360,height=250)

    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #convert to greyscale
            imageNp=np.array(img,'uint8')
            id1=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id1)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!")




    






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
  
