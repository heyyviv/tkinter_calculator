from tkinter import *
root=Tk()
root.title("Calculater")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=5)
global name
global num
def clicked(num):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(num))

def add():
    global name
    global num
    g=e.get()

    num=int(g)

    name="add"
    e.delete(0,END)
def mul():
    global name
    global num
    d=e.get()
    num=int(d)
    name="multiply"
    e.delete(0,END)

def div():
    global name
    global num
    d = e.get()
    num = int(d)
    name = "division"
    e.delete(0, END)
def sub():
    global name
    global num
    d = e.get()
    num = int(d)
    name = "subtraction"
    e.delete(0, END)
def cle():
    e.delete(0,END)
def equal():
    k=int(e.get())
    e.delete(0,END)
    p=int(num)

    if name=="add":
        e.insert(0,k+p)
    if name == "subtraction":
        e.insert(0, p-k)
    if name=="multiply":
        e.insert(0,k*p)
    if name == "division":
        e.insert(0, k / p)








b_1=Button(root,text="1",padx=40,pady=10,command=lambda:clicked(1))
b_2=Button(root,text="2",padx=40,pady=10,command=lambda:clicked(2))
b_3=Button(root,text="3",padx=40,pady=10,command=lambda:clicked(3))
b_4=Button(root,text="4",padx=40,pady=10,command=lambda:clicked(4))
b_5=Button(root,text="5",padx=40,pady=10,command=lambda:clicked(5))
b_6=Button(root,text="6",padx=40,pady=10,command=lambda:clicked(6))
b_7=Button(root,text="7",padx=40,pady=10,command=lambda:clicked(7))
b_8=Button(root,text="8",padx=40,pady=10,command=lambda:clicked(8))
b_9=Button(root,text="9",padx=40,pady=10,command=lambda:clicked(9))
b_0=Button(root,text="0",padx=40,pady=10,command=lambda:clicked(0))
b_eq=Button(root,text="=",padx=90,pady=10,command=equal)
b_add=Button(root,text="+",padx=40,pady=10,command=add)
b_sub=Button(root,text="-",padx=40,pady=10,command=sub)
b_mul=Button(root,text="x",padx=40,pady=10,command=mul)
b_div=Button(root,text="/",padx=40,pady=10,command=div)
b_clear=Button(root,text="CLE",padx=90,pady=10,command=cle)

b_1.grid(row=3,column=0)
b_2.grid(row=3,column=1)
b_3.grid(row=3,column=2)
b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)
b_7.grid(row=1,column=0)
b_8.grid(row=1,column=1)
b_9.grid(row=1,column=2)
b_0.grid(row=4,column=0)
b_eq.grid(row=4,column=1,columnspan=2)
b_add.grid(row=5,column=0)
b_sub.grid(row=5,column=1)
b_mul.grid(row=5,column=2)
b_div.grid(row=6,column=0)
b_clear.grid(row=6,column=1,columnspan=2)


root.mainloop()