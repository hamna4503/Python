from tkinter import*
m=Tk()
def bn():
    dec=int(e1.get())
    bn = ""
    while dec != 1:
        a = dec % 2
        if a == 0:
            bn += "0"
        else:
            bn += "1"
        dec = int(dec / 2)
    bn="1"+bn[::-1]
    l2=Label(m,bg="yellow",fg="black",text="After conversion to binary:"+"    "+bn)
    l2.grid(row=4,column=0,pady=6)
l1=Label(m,bg="pink",fg="black",width=30,text="Decimal number to convert to binary:").grid(row=0,column=0,padx=2,pady=2)
e1=Entry(m,bg="lightblue",fg="black")
e1.grid(row=0,column=2)
b1=Button(m,bg="red",fg="yellow",text="Find Now",command=bn)
b1.grid(row=2,column=5,padx=5)
m.mainloop()