import threading
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter as tk
import SplitAndCat
from tkinter import ttk
import os

def get_filename():
    global filename
    filename = askopenfilename()
    print(filename)
    text_split_file.delete(1.0, END)
    text_split_file.insert(END, filename)


def split_file():
    size = int(entry_split_size.get()) * 1024 * 1024
    maximum = os.path.getsize(filename)
    progress_bar['maximum'] = maximum
    progress_bar['value'] = 0
    thread = threading.Thread(target=SplitAndCat.split_file, args=(filename, size, progress_bar,))
    thread.start()


def cat_files():
    pass


r = Tk()
r.geometry('{}x{}'.format(460, 350))
label_split_size = Label(r, text='请输入要分割的文件大小单位M：')
label_split_size.grid(row=0)
entry_split_size = Entry(r)
entry_split_size.grid(row=0, column=1)
text_split_file = Text(r, height=5, width=30)
text_split_file.grid(row=1, column=0)
button_select_file = tk.Button(r, text='选择文件', width=10, command=get_filename, fg="red")
button_select_file.grid(row=1, column=1)
button_start = tk.Button(r, text='开始分割', width=10, command=split_file, fg="red")
button_start.grid(row=2, column=1)
progress_bar = ttk.Progressbar(r, orient='horizontal', length=250, mode='determinate')
progress_bar.grid(row=2, column=0)
progress_bar['value'] = 0
button_cat = tk.Button(r, text='开始合并', width=10, command=cat_files, fg="red")
button_cat.grid(row=3, column=1)

r.mainloop()


