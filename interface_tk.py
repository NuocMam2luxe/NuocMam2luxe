import tkinter as tk
import sqlite3

# Functions

def reset():
    conn = sqlite3.connect("Saves\\Save1.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE nan")
    conn.commit()
    conn.close()    

def create_sql():
    conn = sqlite3.connect("Saves\\Save1.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE nan(Money TEXT)")
    conn.commit()
    conn.close()
    
def delete_sql():
    conn = sqlite3.connect("Saves\\Save1.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE nan(Money TEXT)")
    conn.commit()
    conn.close()

def printer():
    if var1.get() and var2.get():    
        print("both")
    elif var1.get() and var2.get()== False:    
        print("Only First")
    elif var1.get()== False and var2.get():
        print("Only second")
    else:
        print("None")

# Tkinter / Window

window = tk.Tk()

# Window size

w = 600
h = 400
pixelwidth = window.winfo_screenwidth()
pixelheight = window.winfo_screenheight()

x= int((pixelwidth/2)- (w/2))
y= int((pixelheight/2) - (h/2))

window.configure(bg="Dark Grey")
window.geometry(f"{w}x{h}+{x}+{y}")

# -------------------------------------

window.columnconfigure((0,1,2,3,4,5,6),weight=1,uniform='a')

window.rowconfigure((0,1,2),weight=1,uniform='a')


# Tk Variables

var1= tk.BooleanVar()
var2= tk.BooleanVar()
var3= tk.StringVar()

# -------------------------------------

# Widgets

label1 = tk.Label(window, text="j'nique ta mere",bg="Dark Grey")
label1.grid(row=0,column=3, sticky="s")


check1 = tk.Checkbutton(variable=var1,onvalue=1,offvalue=0,bg="Dark Grey")
check1.grid(row=0,column=2,sticky="se")

check2 = tk.Checkbutton(variable=var2,onvalue=1,offvalue=0,bg="Dark Grey")
check2.grid(row=0,column=4,sticky="sw")

entry1= tk.Entry(window)
entry1.grid(row=1,column=3)

button1= tk.Button(command=create_sql, text="Start",bg="Dark Grey",relief=tk.RIDGE)
button1.grid(row=2,column=2, sticky="ne")

button2= tk.Button(command=reset, text="Delte",bg="Dark Grey",relief=tk.RIDGE,)
button2.grid(row=2,column=4, sticky="nw")

# -------------------------------------

window.mainloop()

