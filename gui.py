import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

def submit():
   messagebox.showinfo(title="custom dialogue box", message="Registration form successfully submitted")
    
window=Tk()
window.geometry("500x500")
window.title("GUI")
myfont=Font(family="times",size=20,weight="bold",slant="italic",underline=1)
lab=Label(window,text="Registeration Form",font=myfont,bg="#0a3d62",fg="white",padx=2,pady=1,relief="raised")
myfont1=Font(family="times",size=15,weight="bold")
lab1=Label(window,text="Name :",font=myfont1,).place(x=50,y=95)
en=tk.Entry(window,width=30,selectbackground="red",selectforeground="black")
lab2=Label(window,text="Email :",font=myfont1,).place(x=50,y=150)
en1=tk.Entry(window,width=30,selectbackground="red",selectforeground="black")
lab3=Label(window,text="Phone NO :",font=myfont1,).place(x=50,y=200)
en2=tk.Entry(window,width=30,selectbackground="red",selectforeground="black")
lab4=Label(window,text="Gender :",font=myfont1,).place(x=50,y=250)
r=Radiobutton(window,text="Male",value=1,font=("times",15,"bold"))
r1=Radiobutton(window,text="Female",value=0,font=("times",15,"bold"))
labl=Label(window,text="Choose a Course :",font=myfont1).place(x=30,y=300)
ch1=Checkbutton(window,text="BCOM",onvalue=1,offvalue=0,font=("times",15,"bold"))
ch2=Checkbutton(window,text="BCA",onvalue=1,offvalue=0,font=("times",15,"bold"))
ch3=Checkbutton(window,text="BBA",onvalue=1,offvalue=0,font=("times",15,"bold"))
l=Button(window,text="Submit",font=myfont,bg="green", fg="white",padx=3,pady=2,command=submit)


lab.pack()
en.place(x=200,y=100)
en1.place(x=200,y=155)
en2.place(x=200,y=205)
r.place(x=200,y=250)
r1.place(x=300,y=250)
ch1.place(x=200,y=300)
ch2.place(x=200,y=330)
ch3.place(x=200,y=360)
l.place(x=200,y=420)
window.mainloop()
    
    



