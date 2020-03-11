from tkinter import *

from PIL import Image,ImageTk
def see_images(k):
    t = Tk()
    iiii = Image.open(str(k))
    iiii = iiii.resize((300, 300), Image.ANTIALIAS)
    p = ImageTk.PhotoImage(iiii)
    label = Label(t, image=p)
    label.pack()
    mainloop()
if __name__ == '__main__':
    showwarning('Info', 'Please Login first using \'Log_in.py\' file')
    exit(0)