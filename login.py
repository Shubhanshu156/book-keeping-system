from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk,Image

import mysql.connector as ms
conn=ms.connect(host='bvflxiwhnysprucu2mpt-mysql.services.clever-cloud.com',password='SsPtUncx8qW0XAsQnJTy', user='ubbmbzmkw9ezho4e',database='bvflxiwhnysprucu2mpt',port=3306)
print("Error! Not connected to Database")
if conn.is_connected()==True:
    print("successfully created")
 
cur=conn.cursor(buffered=True)
root=Tk()
root.geometry('500x500')
root.iconbitmap("icon.ico") 
count=0

def submit():
        sql12="select bissue from login where bissue!='not' and username='%s'"%(var1.get())
        
        cur.execute(sql12)
        data1=cur.fetchall()
        
        if data1!=[]:
            mq=messagebox.showwarning("submit first","pls submit book first"+str(data1[-1]))
        else:
           
            inp=(var1.get(),boo.get())
            
            sql="select issuer from book where bname='%s'"%inp[1]
            cur.execute(sql)
            data=cur.fetchone()
            
            cur.execute(sql)
            data=cur.fetchall()
      
            if data!=[(None,)]:
                sql="update book set issuer=%s where bname=%s"
                sql1="update login set bissue='%s' where username='%s'"%(boo.get(),var1.get())
                cur.execute(sql1)
                
                cur.execute(sql,inp)
                conn.commit()
               

                meas=messagebox.showinfo("issued","you have issued "+inp[1])
            else:
                 mess=messagebox.showwarning("issued","book already issued") 
def issue():
    sql="update book set issuer='not' where bname='%s'"%(boo.get())
    sql1="update login set bissue='not' where username='%s'"%(var1.get())
    print(sql,sql1)
    cur.execute(sql)
    cur.execute(sql1)
    conn.commit()
    mess=messagebox.showinfo("submit","you have submitted")

def createaccount():
    global var1,var2
    num1=var1.get()
    num2=var2.get()

    sqln="select * from  login where username='%s' and password='%s'"%(num1,num2)
    cur.execute(sqln)
    data=cur.fetchone()
    
    if data==('', ''):
        l=messagebox.showwarning("invalid username","enter valid username or password")
    if data!=None:
        l=messagebox.showwarning("account already exist","account already exist")
    else:
        sql="insert into login (username,password,bissue)VALUES('{}','{}',not')".format(num1,num2)

        cur.execute(sql)
        conn.commit()
        m=messagebox.showinfo("succesfully!!! account created","congratulation your account has been created")
def selected(event):
    boo=StringVar()
    mainframe=Frame(root)
    
    mainframe.pack(fill=X,expand=1)
    mycanvas=Canvas(mainframe)


    mycanvas.pack(side=LEFT,fill=BOTH,expand=1)
    myscrollbar=ttk.Scrollbar(mainframe,orient=VERTICAL,command=mycanvas.yview)
    myscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=myscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))

    secondframe=Frame(mycanvas)
    mycanvas.create_window((3,3),window=secondframe,anchor="nw")
  
    
   
    
    num=clicked.get()
    sql="select bname,bauthor,category from book where category='%s'and issuer='not'"%(num)
    cur.execute(sql)
    thing=10
    mn=7
    lab=Label(secondframe,text="book name",font=("Back to Demo",15)).grid(row=0,column=0)
    lab2=Label(secondframe,text="author name",font=("Back to Demo",15)).grid(row=0,column=5)
    lab3=Label(secondframe,text="book category",font=("Back to Demo",15)).grid(row=0,column=10)
    for row in cur:
        mn=0
        for ele in row:
            labe=Label(secondframe,text=ele)
            labe.grid(row=thing,column=mn,pady=20,padx=70)
                    
            mn+=5
        
        thing+=5
  
    mycanvas.create_line(3,3,thing,mn)
    mycanvas.pack()
         
clicked=StringVar()
def clickede():
    global var1,var2
    num1=var1.get()
    num2=var2.get()
    sql="select * from  login where username='%s' and password='%s'"%(num1,num2)
    
    cur.execute(sql)
    data=cur.fetchone()   
    
    if data==('', '') or data==None:
       l=messagebox.showwarning("invalid username","enter valid username or password")
    else:        
        sql="select * from login where bissue!='not' and username='%s'"%var1.get()
        
        cur.execute(sql)
        data=cur.fetchall()
        if data!=[]:
            mq=messagebox.showwarning("submit first","pls submit book first")
      
        createaccountbtn.destroy()
        loginbtn.destroy()
        
        root.config(background='dodger blue')
        
        global countbtn
        username.destroy()
        password.destroy()
        a.destroy()
        b.destroy()
        mylabel.destroy()
        global your
        your=ImageTk.PhotoImage(Image.open("SUBMIT.png"))
        myimage=ImageTk.PhotoImage(Image.open("books.png"))
    
        m=Label(root,image=myimage)
        m.pack()
        data=["choose category","action and adventure","biography","classic","Sci-Fi"]
             

        global boo
        selct=OptionMenu(root,clicked,*data,command=selected).place(x=400,y=100)
        
        enter=Entry(root,textvariable=boo)
        style=Style()
        style.configure("TButton",font=("ds-digital,20"),background="purple",bd="3",activebackground="red",activeforeground="green")
        btn=Button(root,text="Issue a book",command=submit).place(x=550,y=50)
        btnu=Button(root,text="submit a book",command=issue).place(x=100,y=50)

        enter.place(x=300,y=50)   
    
        
boo=StringVar()
var1=StringVar()
var2=StringVar()
root.title("Login")
root.geometry('750x500')
mypic=Image.open("jarvis.png")
mypici=Image.open("login.png")
mypicj=Image.open("create account.png")
SUBMIT=Image.open("SUBMIT.png")
resizedS=SUBMIT.resize((100,50),Image.ANTIALIAS)
resized=mypic.resize((750,500),Image.ANTIALIAS)
resizedi=mypici.resize((100,50),Image.ANTIALIAS)
resizedj=mypicj.resize((100,50),Image.ANTIALIAS)

mypicS=ImageTk.PhotoImage(file="SUBMIT.png")
mypic=ImageTk.PhotoImage(file="jarvis.png")
mypici=ImageTk.PhotoImage(file="login.png")
mypicj=ImageTk.PhotoImage(file="create account.png")
newpic=ImageTk.PhotoImage(resized)
newpici=ImageTk.PhotoImage(resizedi)
newpicj=ImageTk.PhotoImage(resizedj)

NEWSUBMIT=ImageTk.PhotoImage(resizedS)
mylabel=Label(root,image=newpic)
mylabel.pack()
a=Entry(root,textvariable=var1,width=15,font=("ds-digital",45))
b=Entry(root,textvariable=var2,width=15,show="*",font=("ds-digital",45))
a.place(x=280,y=75)
b.place(x=275,y=170)
username=Label(root,text="username",font=("ds-digital",40),background="black",foreground="cyan")
password=Label(root,text="password",font=("ds-digital",40),background="black",foreground="cyan")
username.place(x=50,y=70)
password.place(x=50,y=180)


loginbtn=Button(root,text="login",image=newpici,command=clickede)
global createaccountbtn
createaccountbtn=Button(root,text="password",image=newpicj,command=createaccount)
createaccountbtn.place(x=350,y=350)


loginbtn.place(x=80,y=350)

mainloop()