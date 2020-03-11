from tkinter import *
from tkinter.filedialog import askopenfile



def open_file():
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	if file is not None:
		content = file.name
		return content

if __name__ == '__main__':
    showwarning('Info', 'Please Login first using \'Log_in.py\' file')
    exit(0)

