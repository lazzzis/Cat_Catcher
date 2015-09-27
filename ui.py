__author__ = 'lazzzis'

import tkinter as tk
import dl

def start_dl(width, height):
    dl.dl_pic(width, height)


def center_window(root, width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))



master = tk.Tk()

tk.Label(master, text="width").grid(row=0, column=0)
tk.Label(master, text="length").grid(row=1, column=0)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(master, text="start", width=10, command=lambda :start_dl(e1.get(), e2.get()))\
    .grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
tk.Button(master, text="exit", width=10, command=master.quit)\
    .grid(row=3, column=1, sticky=tk.E, padx=10, pady=10)

center_window(master, 325, 100)

tk.mainloop()


