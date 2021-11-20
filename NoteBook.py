''' NoteBook v 0.1.2 '''

import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

FILE_NAME = tkinter.NONE


def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)

def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

root = tkinter.Tk()
root.title("NoteBook")
root.minsize(width=320, height=480)
root.maxsize(width=320, height=480)

text = tkinter.Text(root, width=400, height=400)
text.pack()

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_comand(label="New file", command=new_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_separator()
menuBar.add_cascade(label="File", menu=fileMenu)

root.config(menu=menuBar)
root.mainloop()
