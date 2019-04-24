
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter as tk
import SplitAndCat


def get_filename():
    global filename
    filename = askopenfilename()
    print(filename)
    text_fragment_file.delete(1.0, END)
    text_fragment_file.insert(END, filename)


def split_file():
    size = int(entry_fragment_size.get()) * 1024 * 1024
    print(filename)
    SplitAndCat.split_file(filename, size)


r = Tk()
r.geometry('{}x{}'.format(460, 350))
label_fragment_size = Label(r, text='请输入要分割的文件大小单位M：')
label_fragment_size.grid(row=0)
entry_fragment_size = Entry(r)
entry_fragment_size.grid(row=0, column=1)
text_fragment_file = Text(r, height=5, width=30)
text_fragment_file.grid(row=1, column=0)
button_select_file = tk.Button(r, text='选择文件', width=10, command=get_filename, fg="red")
button_select_file.grid(row=1, column=1)
button_start = tk.Button(r, text='开始分割', width=10, command=split_file, fg="red")
button_start.grid(row=2, column=1)

r.mainloop()


