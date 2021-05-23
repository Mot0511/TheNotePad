from tkinter import *
from tkinter import filedialog

win = Tk()
win.geometry('1000x500')
win.title('TheNotePad')

# add text input
input = Text(win)
input.pack(expand=YES, fill=BOTH)

def new():
    print('new')

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file', filetypes=(('Text Documents', '*.txt'), ('All files', '*.*')))

    if file_name:
        text_save = open(file_name, 'r').read()
        input.delete(1.0, END)
        input.insert(END, text_save)

def save():
    file_name = filedialog.asksaveasfilename(initialdir='/', title='Save file', filetypes=(('Text Documents', '*.txt'), ('All files', '*.*')))

    if file_name:
        f = open(file_name, 'w')
        save_text = str(input.get(1.0, END))
        f.write(save_text)
        f.close()

# add menu
menu = Menu(win)
win.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=new)
file_menu.add_command(label='Open...', command=open_file)
file_menu.add_command(label='Save as...', command=save)
file_menu.add_command(label='Exit', command=exit)
help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Help')
help_menu.add_command(label='About')
menu.add_cascade(label='File', menu=file_menu)




win.mainloop()