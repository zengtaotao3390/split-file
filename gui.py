import threading
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter as tk
import SplitAndCat
from tkinter import ttk
import os
import ntpath


def get_split_filename():
    global filename
    filename = askopenfilename()
    print(filename)
    text_split_file.delete(1.0, END)
    text_split_file.insert(END, filename)


def get_cat_file_path():
    global cat_filepath
    cat_filepath = askopenfilename()
    text_cat_file.delete(1.0, END)
    text_cat_file.insert(END, cat_filepath)


def split_file():
    size = int(entry_split_size.get()) * 1024 * 1024
    maximum = os.path.getsize(filename)
    split_progress_bar['maximum'] = maximum
    split_progress_bar['value'] = 0
    thread = threading.Thread(target=SplitAndCat.split_file, args=(filename, size, split_progress_bar,))
    thread.start()


def cat_files():
    path, cat_filename = ntpath.split(cat_filepath)
    print(path)
    size = sum(os.path.getsize(path + '/' + f) for f in os.listdir(path) if os.path.isfile(path + '/' + f))
    print(size)
    cat_progress_bar['maximum'] = size
    cat_progress_bar['value'] = 0
    thread = threading.Thread(target=SplitAndCat.cat_files, args=(path, cat_progress_bar,))
    thread.start()


if __name__ == '__main__':
    r = Tk()
    r.geometry('{}x{}'.format(560, 350))
    label_split_size = Label(r, text='请输入要分割的文件大小单位M：')
    label_split_size.grid(row=0)

    entry_split_size = Entry(r)
    entry_split_size.grid(row=0, column=1)

    text_split_file = Text(r, height=5, width=30)
    text_split_file.grid(row=1, column=0)

    button_select_file = tk.Button(r, text='选择分割文件', width=10, command=get_split_filename, fg="red")
    button_select_file.grid(row=1, column=1)

    button_start = tk.Button(r, text='开始分割', width=10, command=split_file, fg="red")
    button_start.grid(row=2, column=1)

    split_progress_bar = ttk.Progressbar(r, orient='horizontal', length=250, mode='determinate')
    split_progress_bar.grid(row=2, column=0)
    split_progress_bar['value'] = 0

    text_cat_file = Text(r, height=5, width=30)
    text_cat_file.grid(row=3, column=0)

    button_select_cat_file = tk.Button(r, text='选择合并文件', width=10, command=get_cat_file_path, fg="red")
    button_select_cat_file.grid(row=3, column=1)

    cat_progress_bar = ttk.Progressbar(r, orient='horizontal', length=250, mode='determinate')
    cat_progress_bar.grid(row=4, column=0)
    cat_progress_bar['value'] = 0

    button_select_cat_file = tk.Button(r, text='合并文件', width=10, command=cat_files, fg="red")
    button_select_cat_file.grid(row=4, column=1)

    r.mainloop()


