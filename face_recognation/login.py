from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from main import Face_Recognition_System



class Login:
    def __init__(self,root):
        #self.variable = ttk.StringVar()
        self.root=root
        self.root.geometry("1360x770+0+0")
        self.root.title("Login")
        
        self.var_user=StringVar()
        self.var_pass=StringVar()

        bg_img=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\un.jpg")
        bg_img=bg_img.resize((1360,700),Image.ANTIALIAS)
        self.photobg_img=ImageTk.PhotoImage(bg_img)

        bg_lbl=Label(self.root,image=self.photobg_img)
        bg_lbl.place(x=0,y=0,width=1360,height=700)


        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=130,width=340,height=420)

        img1=Image.open(r"C:\Users\Admin1\Desktop\face_recognation\college_images\LoginIconAppl.png")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_img=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img.place(x=637,y=150,width=80,height=80)

        #get_str=Label(frame,text="")
        username=Label(frame,text="Username",font=("times new romen",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=135)

        self.user_entry=ttk.Entry(frame,textvariable=self.var_user,font=("times new romen",15,"bold"))
        self.user_entry.place(x=40,y=175,width=270)

        password=Label(frame,text="Password",font=("times new romen",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=215)

        self.pass_entry=ttk.Entry(frame,show="*",font=("times new romen",15,"bold"))
        self.pass_entry.place(x=40,y=250,width=270)

        login_btn=Button(frame,text="Login",font=("times new romen",15,"bold"),command=self.login,bd=3,relief=RIDGE,fg="white",bg="red")
        login_btn.place(x=105,y=315,width=130,height=35)

        # forget_btn=Button(frame,text="Forgot Password",font=("times new romen",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black")
        # forget_btn.place(x=10,y=380,width=160)

    def login(self):
            if self.user_entry.get()=="" or self.pass_entry.get()=="":
                messagebox.showerror("Error","All Fields Required")
            elif self.user_entry.get()=="admin" and self.pass_entry.get()=="admin@123":
                new_window=Toplevel(self.root)
                app=Face_Recognition_System(new_window)

            else:
                messagebox.showerror("invalid","Invalid Username or Password")


if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
  