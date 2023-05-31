from tkinter import *                                                                                                                                                   
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2

#Set up Window
class Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Face Recognition System")

        lbl_title= Label(self.root,text="Face Detection",font=("times new romen",20,"bold"),bg="yellow",fg="red")
        lbl_title.place(x=0,y=5,width=1360,height=38)

        #1st Image
        img11=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\face_detector1.jpg")
        img11=img11.resize((580,650),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        f_lbl=Label(self.root,image=self.photoimg11)
        f_lbl.place(x=0,y=45,width=580,height=650)

        #2nd Image
        img1=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img1=img1.resize((820,650),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=550,y=45,width=820,height=650)

        #button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="yellow")
        b1_1.place(x=300,y=570,width=200,height=40)

    #Attendance Function
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
             mydata=f.readlines()
             name_list=[]
             for line in mydata:
                 entry=line.split((","))
                 name_list.append(entry[0])
             if ( (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                 now=datetime.now()
                 d1=now.strftime("%d/%m/%Y")
                 dtString=now.strftime("%H:%M:%S")
                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        
    #Face Recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id1,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Walid@541",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where id="+str(id1))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select rollno from student where id="+str(id1))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where id="+str(id1))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select id from student where id="+str(id1))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept:{d}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face Detected",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                
                coord=[x,y,w,h]
                
            return coord

        def recognize(img,clf,faceCascade):
            coord= draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Recognition(root)
    root.mainloop()
