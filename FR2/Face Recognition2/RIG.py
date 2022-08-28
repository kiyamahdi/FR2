#Receiving Information GUI

import tkinter as tk
from tkinter import ttk
def GUI():
    infolist = []
    root = tk.Tk()
    root.title('Receiving Information')
    root.geometry("300x350")
    fname = tk.StringVar()
    lname = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    lblfn = ttk.Label(root, text='First name : ', font=("Helvetica", 14))
    lblfn.place(x=20, y=30)
    efname = ttk.Entry(root, textvariable=fname)
    efname.place(x=150, y=35)
    lblln = ttk.Label(root, text='Last name : ', font=("Helvetica", 14))
    lblln.place(x=20, y=100)
    elname = ttk.Entry(root, textvariable=lname)
    elname.place(x=150, y=105)
    lblage = ttk.Label(root, text='Age : ', font=("Helvetica", 14))
    lblage.place(x=20, y=170)
    eage = ttk.Entry(root, textvariable=age)
    eage.place(x=150, y=175)
    lblgen = ttk.Label(root, text='Gender : ', font=("Helvetica", 14))
    lblgen.place(x=20, y=240)
    rgender = ttk.Radiobutton(root, text='Male', value='M', variable=gender)
    rgender.place(x=150, y=245)
    rfgender = ttk.Radiobutton(root, text='Female', value='F', variable=gender)
    rfgender.place(x=220, y=245)
    button_ok = ttk.Button(root, text='OK', command=lambda: (
        infolist.append((fname.get(), lname.get(), age.get(), gender.get())), root.quit()))
    button_ok.place(x=200, y=310)
    button_exit = ttk.Button(root, text='Exit', command=lambda: root.quit())
    button_exit.place(x=20, y=310)
    root.mainloop()
    fname = infolist[0][0]
    lname = infolist[0][1]
    age = infolist[0][2]
    gender = infolist[0][3]
    return fname, lname, age, gender
