# making scientific calculator(COMPLETED);TKINTERLAB
import math
from tkinter import *

m = Tk()

def sn():
    x = float(e1.get())
    h = math.sin(x)
    Label(m, bg="white", fg="black", width=30, font=("aerial", 20), text="sin" + str(x) + " = " + str(h)).grid(row=3,
                                                                                                               column=1)
def cs():
    x = float(e1.get())
    h = math.cos(x)
    Label(m, bg="white", fg="black", width=30, font=("aerial", 20), text="cos" + str(x) + " = " + str(h)).grid(row=3,
                                                                                                               column=1)
def tn():
    x = float(e1.get())
    h = math.tan(x)
    Label(m, bg="white", fg="black", font=("aerial", 20), width=30, text="tan" + str(x) + " = " + str(h)).grid(row=3,
                                                                                                               column=1)
def sqrt():
    x = float(e1.get())
    h = math.sqrt(x)
    Label(m, bg="white", fg="black", font=("aerial", 20), width=30, text="√" + str(x) + " = " + str(h)).grid(row=3,
                                                                                                             column=1)
def sqr():
    x = float(e1.get())
    h = x * x
    Label(m, bg="white", fg="black", font=("aerial", 20), width=30, text=str(x) + "²" + " = " + str(h)).grid(row=3,
                                                                                                             column=1)
def cube():
    x = float(e1.get())
    h = x * x * x
    Label(m, bg="white", fg="black", font=("aerial", 20), width=30, text=str(x) + "³" + " = " + str(h)).grid(row=3,
                                                                                                             column=1)
def fact():
    x = int(e1.get())
    h = float(math.factorial(x))
    Label(m, bg="white", fg="black", font=("aerial", 20), text=str(x) + "! = " + str(h)).grid(row=3, column=1)

def log():
    x = float(e1.get())
    h = math.log10(x)
    Label(m, bg="white", fg="black", font=("aerial", 20), width=30, text="log" + str(x) + " = " + str(h)).grid(row=3,
                                                                                                               column=1)
def Enter():
    x = (e1.get())
    h = eval(x)
    Label(m, bg="white", fg="black", font=("aerial", 20), width=30, text=str(x) + " = " + str(h)).grid(row=3, column=1)


l = Label(m, bg="lightblue", fg="black", width=20, font=("aerial", 15), text="Enter").grid(row=0, column=0, padx=6,
                                                                                           pady=6)

e1 = Entry(m, bg="white", fg="black")
e1.grid(row=0, column=3)

b1 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="sin", command=sn)
b1.grid(row=5, column=4, pady=5, padx=5)
b2 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="cos", command=cs)
b2.grid(row=5, column=5, pady=5, padx=5)
b3 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="tan", command=tn)
b3.grid(row=5, column=6, pady=5, padx=5)
b4 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="√x", command=sqrt)
b4.grid(row=6, column=4, padx=5, pady=5)
b5 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="x²", command=sqr)
b5.grid(row=6, column=5, padx=5, pady=5)
b6 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="x³", command=cube)
b6.grid(row=6, column=6, padx=5, pady=5)
b7 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="log", command=log)
b7.grid(row=7, column=4, padx=5, pady=5)
b8 = Button(m, bg="blue", fg="white", width=15, font=("aerial", 10), text="x !", command=fact)
b8.grid(row=7, column=5, padx=5, pady=5)
b9 = Button(m, bg="green", fg="white", width=15, font=("aerial", 10), text="Enter", command=Enter)
b9.grid(row=7, column=6, padx=5, pady=5)

m.mainloop()
