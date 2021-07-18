from tkinter import*
from tkinter .ttk import *
from time import strftime
# download font ds-digital from         https://www.dafont.com/ds-digital.font

root=Tk()
root.title("Clock")
root.geometry("500x200")
root.configure(bg='black')
def time():
    string =strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font=("ds-digital",80), background="black",foreground="cyan")
label.pack(anchor='center')
time()
mainloop()