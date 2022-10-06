from tkinter import *

win = Tk()

win.geometry("700x350")

def on_click():
   label["text"] = "Code"
   b["text"] = "Congrats! You are now a true programmer"

label = Label(win, text="Coffee",
font=('Calibri 15 bold'))
label.pack(pady=20)

b = Button(win, text="Click to change Coffee to Code", command=on_click)
b.pack(pady=20)

win.mainloop()