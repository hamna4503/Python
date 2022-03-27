#import pyodbc
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
m=Tk()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
def display():

    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=F:\games setups\std.accdb;')
    cur = con.cursor()
    cur.execute('select * from emp')
    data = cur.fetchall()
    print("Name", "\t", "Address")
    if len(data) != 0:
        for i in data:
            print(i)
    con.close()

def insert():
    con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=f:\games setups\std.mdb;')
    cur1=con.cursor()
    cur1.execute(f"INSERT INTO emp(empno,ename,address,deptid) values('{var1.get()}','{var2.get()}','{var3.get()}','{var4.get()}')")
    con.commit()
    messagebox.showinfo("Insert", "One record has been added")
    display()
    con.close()

def delete():
    con=pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                         r'DBQ=f:\games setups\std.mdb;')
    cur1=con.cursor()
    cur1.execute(f"DELETE FROM emp WHERE empno={var1.get()}")
    con.commit()
    messagebox.showinfo("Delete","One record has been deleted")
    display()
    con.close()



l1=Label(m,bg="gold",fg="red",text="PIZZA HUT",font=("Times New Roman",45),bd=10)
l1.pack(side=TOP,fill=X)
f1=Frame(m,bg="light blue")
f1.place(x=10,y=100,width=450,height=650)
f2=Frame(m,bg="pink")
img1=PhotoImage(file=r'f:\games setups\ned2.png')
img2=img1.subsample(2,2)
lim=Label(f1,image=img2).grid(row=0,column=0,padx=50,pady=10,columnspan=2)
l2=Label(f1,bg="gold",fg="red",text="MENU",font=("bold"),width=15,bd=15).grid(row=1,column=0,padx=50,pady=10)
b1=Button(f1,text="Pizza",bg="blue",fg="white",font=("bold"),width=15,bd=10,command=display).grid(row=5,column=0)
b2=Button(f1,text="Pasta",bg="blue",fg="white",font=("bold"),width=15,bd=10,command=insert).grid(row=6,column=0)
b3=Button(f1,text="Drinks",bg="blue",fg="white",font=("bold"),width=15,bd=10,command=delete).grid(row=7,column=0)
b4=Button(f1,text="Deserts",bg="blue",fg="white",font=("bold"),width=15,bd=10).grid(row=8,column=0)

f2.place(x=450,y=100,width=900,height=700)
stable=ttk.Treeview(f2,height=900,columns=("empno","ename","address","deptid"))
stable.pack()
m.mainloop()
