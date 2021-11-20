''' NoteBook v 0.1 '''

import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

FILE_NAME = tkinter.NONE


def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)

root = tkinter.Tk()
root.title("NoteBook")
root.minsize(width=320, height=480)
root.maxsize(width=320, height=480)

text = tkinter.Text(root, width=400, height=400)
text.pack()

root.mainloop()
