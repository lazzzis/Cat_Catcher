__author__ = 'lazzzis'

import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os.path
import dl


def start_dl(width, height, folder):
    folder = os.path.join(folder, 'pic.jpg')
    if dl.dl_pic(width, height, folder):
        messagebox.showinfo('Cat_Catcher', 'Successfully downloaded at ' + folder, parent=master)
    else:
        messagebox.showwarning('Cat_Catcher', 'No such picture with the given size ' + e1.get() + ' * ' + e2.get())


def center_window(root, width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def get_save_dir():
    file_name = filedialog.askdirectory()
    if file_name:  # fileName is not none or ''
        file_save_pos.delete(0, tk.END)
        file_save_pos.insert(0, file_name)
    else:
        file_save_pos.delete(0, tk.END)
        file_save_pos.insert(0, os.path.expanduser('~'))

if __name__ == '__main__':
    master = tk.Tk()
    master.title('cat_catcher')

    tk.Label(master, text="width").grid(row=0, column=0)
    tk.Label(master, text="height").grid(row=1, column=0)

    e1 = tk.Entry(master)  # width input
    e2 = tk.Entry(master)  # height input
    e1.grid(row=0, column=1, columnspan=2)
    e2.grid(row=1, column=1, columnspan=2)

    save_pos_label = tk.Label(master, text="save dir")
    save_pos_label.grid(row=2, column=0)

    file_save_pos = tk.Entry(master)  # show the folder where the pic will be saved
    file_save_pos.insert(0, os.path.expanduser('~'))  # as default, pic will be saved on home folder
    file_save_pos.grid(row=2, column=1)

    # press to change the save dir
    file_save_button = tk.Button(master, text='...', command=get_save_dir)
    file_save_button.grid(row=2, column=2)

    # press to start downloading
    tk.Button(master, text="start", width=10, command=lambda :start_dl(e1.get(), e2.get(), file_save_pos.get()))\
        .grid(row=3, column=0, sticky=tk.W)
    # press to quit
    tk.Button(master, text="exit", width=10, command=master.quit)\
        .grid(row=3, column=2, sticky=tk.E)

    # window will be show on the center of screen
    center_window(master, 385, 100)

    tk.mainloop()
