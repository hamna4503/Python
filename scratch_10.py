import math
from tkinter import*

m =Tk()
m.state("zoom")
m.title("SCIENTIIC CALCULATOR")
frame = Frame(m, bg="pink", borderwidth=10, highlightthickness=2, relief=GROOVE)
frame.place(height=500, width=500)
def sum():
    n1=int(e1.get())
    n2=int(e2.get())
    add=n1+n2
    #l = Label(m, width=20, text=add, bg="lightblue",fg="red")
    #l.grid(row=5, column=1)
    #l3.config(m, text="", bg="red", fg="black", width=20)
    #l3.grid(row=3, column=1)
    l3.config(text=add)
def subtract():
    n1 = int(e1.get())
    n2 = int(e2.get())
    sub = n1-n2
    #l=Label(m, width=20, text=sub, bg="lightblue",fg="red")
    #l.grid(row=6,column=1)
    #l3.config(m, text="", bg="red", fg="black", width=20)
    #l3.grid(row=3, column=1)
    l3.config(text=sub)
def multiply():
    n1 = int(e1.get())
    n2 = int(e2.get())
    multi = n1 * n2
    #l=Label(m, width=20, text=multi, bg="lightblue",fg="red")
    #l.grid(row=7,column=1)
    l3.config(text=multi)


def division():
    n1 = int(e1.get())
    n2 = int(e2.get())
    div = n1 / n2
    #l = Label(m, width=20, text= div, bg="lightblue", fg="red")
    #l.grid(row=8, column=1)
    l3.config(text=div)
def factorial():
    fact=1
    x=int(e1.get())
    for i in range(1,x+1):
        fact=fact*i
    #l=Label(m, width=20,text="The factorial is"+str(fact),bg="lightblue", fg="red")
    #l.grid(row=9, column=1)
    l3.config(text=fact)
def table():
    tno=int(e1.get())
    trange=int(e2.get())
    for i in range(1,trange+1):
        result=(tno,"*",i,"=",tno*i)
        #l=Label(m,width=20,text=result,bg="lightblue", fg="red")
        #l.grid(row=10,column=1)
        l3.config(text=result)
def sqrt():
    n1=int(e1.get())
    sqroot=math.sqrt(n1)
    #l=Label(m,width=20,text= "The square root is"+str(sqroot),bg="lightblue", fg="red")
    #l.grid(row=11,column=1)
    l3.config(text=sqroot)
def tan():
    n1 = int(e1.get())
    ans=math.tan(n1)
    #l = Label(m, width=20, text="The tan " + str(ans), bg="lightblue", fg="red")
    #l.grid(row=12, column=1)
    l3.config(text=ans)
def sin():
    n1 = int(e1.get())
    ans = math.sin(n1)
    #l = Label(m, width=20, text="The sin " + str(ans), bg="lightblue", fg="red")
    #l.grid(row=13, column=1)
    l3.config(text=ans)
def cos():
    n1 = int(e1.get())
    ans = math.cos(n1)
    #l = Label(m, width=20, text="The cos " + str(ans), bg="lightblue", fg="red")
    #l.grid(row=14, column=1)
    l3.config(text=ans)





l1=Label(m,height=2,width=20,text="Enter first no",bg="pink",fg="blue")
l1.grid(row=1,column=0)

e1=Entry(m,width=20,bg="pink",fg="blue")
e1.grid(row=1,column=1)

l2=Label(m,width=20,text="Enter second no",bg="pink",fg="blue")
l2.grid(row=2,column=0)

e2=Entry(m,width=20,bg="pink",fg="blue")
e2.grid(row=2,column=1)

l3=Label(m,bg="red",fg="white")
l3.grid(row=3,column=1)

#lb1=Label(m,width=20,text="",bg="yellow")
#lb1.grid(row=3,column=0)


#lb2=Label(m,width=20,text="",bg="yellow")
#lb2.grid(row=3,column=1)

btn1=Button(m,text="Add",width=12,height=1,bg="lightblue",fg="red",command=sum)
btn1.grid(row=5,column=1)

btn2=Button(m,text="Subtract",width=12,height=1,bg="lightblue",fg="red",command=subtract)
btn2.grid(row=6,column=1)

btn3=Button(m,text="Multiply",width=12,height=1,bg="lightblue",fg="red",command=multiply)
btn3.grid(row=7,column=1)

btn4=Button(m,text="Divide",width=12,height=1,bg="lightblue",fg="red",command=division)
btn4.grid(row=8,column=1)

btn5=Button(m,text="factorial",width=12,height=1,bg="lightblue",fg="red",command=factorial)
btn5.grid(row=9,column=1)

btn6=Button(m,text="table",width=12,height=1,bg="lightblue",fg="red",command=table)
btn6.grid(row=10,column=1)

btn7=Button(m,text="Square Root",width=12,height=1,bg="lightblue",fg="red",command=sqrt)
btn7.grid(row=11,column=1)

btn8=Button(m,text="Tan",width=12,height=1,bg="lightblue",fg="red",command=tan)
btn8.grid(row=12,column=1)

btn9=Button(m,text="Sin",width=12,height=1,bg="lightblue",fg="red",command=sin)
btn9.grid(row=13,column=1)

btn10=Button(m,text="cos",width=12,height=1,bg="lightblue",fg="red",command=cos)
btn10.grid(row=14,column=1)





m.mainloop()