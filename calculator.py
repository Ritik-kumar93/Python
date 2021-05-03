import tkinter as tk
def num1(x):
    global k1
    global k3
    if(k3==1):
        a1=v1.get()+str(x)
        v1.set(a1)
        k1=0
    else:
        a1=str(x)
        v1.set(a1)
        k3=1
        k1=0
def opr1(y):
    global k1
    global k2
    global k3
    if(k1==0):
        if(k3==0 and (y=="+" or y=="-")):
            a1=v1.get()+str(y)
            v1.set(a1)
            k1=1
        else:
            a1=v1.get()+str(y)
            v1.set(a1)
            k1=1
        k2=0
        k3=1
def dot1(z):
    global k1
    global k2
    if(k2==0):
        a1=v1.get()+str(z)
        v1.set(a1)
        k2=1
        k1=1
def equal1():
    global k1
    global k2
    global k3
    a1=v1.get()
    a2=eval(a1)
    v1.set(a2)
    k2=1
    k1=0
    k3=0
def back1():
    global k1
    global k2
    global k3
    a1=v1.get()
    a2=a1[0:len(a1)-1]
    v1.set(a2)
    k2=1
    k1=0
    k3=0       







frame1=tk.Tk()
frame1.title("calculator")
v1=tk.StringVar()
k1=0
k2=0
k3=0
v1.set("0")
tk.Entry(frame1,font=("arial",20,"bold"),bd=10,bg="powder blue",justify="right",textvariable=v1).grid(columnspan=4)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",command=lambda:num1('1')).grid(row=1,column=0)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",command=lambda:num1('2')).grid(row=1,column=1)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda:num1('3')).grid(row=1,column=2)


tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda:num1('4')).grid(row=2,column=0)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda:num1('5')).grid(row=2,column=1)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda:num1('6')).grid(row=2,column=2)


tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda:num1('7')).grid(row=3,column=0)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda:num1('8')).grid(row=3,column=1)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda:num1('9')).grid(row=3,column=2)


tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text=".",command=lambda:num1('.')).grid(row=4,column=0)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",command=lambda:num1('0')).grid(row=4,column=1)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="#",command=lambda:num1('#')).grid(row=4,column=2)


tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda:opr1('+')).grid(row=5,column=0)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda:opr1('-')).grid(row=5,column=1)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",command=lambda:opr1('/')).grid(row=5,column=2)



tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",command=lambda:opr1('*')).grid(row=6,column=0)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="BACK",command=back1).grid(row=6,column=1)
tk.Button(frame1,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=equal1).grid(row=6,column=2)
frame1.mainloop()


