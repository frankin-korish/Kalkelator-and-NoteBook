''' NoteBook v 1.0.0 '''

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


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Упс!", message="Не удалось сохранить файл....")


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name

    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)


root = tkinter.Tk()
root.title("NoteBook")
root.minsize(width=320, height=480)
root.maxsize(width=320, height=480)

text = tkinter.Text(root, width=400, height=400)
text.pack()

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="Новый файл", command=new_file)
fileMenu.add_command(label="Сохранить", command=save_file)
fileMenu.add_command(label="Сохранить как", command=save_as)
fileMenu.add_command(label="Открыть", command=open_file)
fileMenu.add_separator()
menuBar.add_cascade(label="Файл", menu=fileMenu)
fileMenu.add_command(label="Выход", command=root.quit)

root.config(menu=menuBar)
root.mainloop()
