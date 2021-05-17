from tkinter import *
import tkinter.messagebox as tmk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title('Untitled-1')
    file = None
    Textarea.delete(1.0, END)
def openy():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,'r')
        Textarea.insert(1.0,f.resd())
        f.close()
def new():
    global file
    root.title('Untitled-1')
    file = None
    Textarea.delete(1.0, END)

def save():
    global file
    file = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt',
                             filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file == "":
        file = None
    else:
        f = open(file, 'w')
        f.write(Textarea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + "-Notepad")
        print('filesaved')

def saveas():
    global file
    file = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt',
                             filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file == "":
        file = None
    else:
        f = open(file, 'w')
        f.write(Textarea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + "-Notepad")
        print('filesaved')

def undo():
    Textarea.event_generate(("<<undo>>"))
def cut():
    Textarea.event_generate(("<<Cut>>"))

def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def delete():
    Textarea.delete(1.0,END)

def about():
    tmk.showinfo('About Us', 'Notepad created by Pavas')

def help():
    tmk.showinfo('Help','how ,can i  help you')
def feedback():
    a=tmk.askquestion('experience','was your experience good??')
    if a=='yes':
        msg=tmk.showinfo('rate us','rate us on playstore please ')
    else:
        msg=tmk.showinfo('rate us','what went wrong??')
    print(msg)
def exit():
    a=tmk.askyesno('exit','Do you want to exit the Notepad')
    if a==True:
        b=tmk.askyesno('save','Do you want to save?')
        if b==True:
            save()
        if b==False:
            quit()

if __name__=='__main__':
    root=Tk()
    root.title('Notepad')
    root.wm_iconbitmap("notepads.ico")
    root.geometry('544x455')

    Textarea=Text(root,font='lucida 14')
    Textarea.pack(fill=BOTH,expand=True)
    file=None

    mymenu=Menu(root)
    m1 = Menu(mymenu, tearoff=0)
    m1.add_command(label='New', command=newfile)
    m1.add_command(label='New window', command=new)
    m1.add_command(label='Open..', command=openy)
    m1.add_command(label='Save', command=save)
    m1.add_command(label='Save as..', command=saveas)
    m1.add_separator()
    m1.add_command(label='exit', command=exit)
    root.config(menu=mymenu)
    mymenu.add_cascade(label='File', menu=m1)

    m2 = Menu(mymenu, tearoff=0)
    m2.add_command(label='Undo', command=undo)
    m2.add_separator()
    m2.add_command(label='Cut', command=cut)
    m2.add_command(label='Copy', command=copy)
    m2.add_command(label='Paste', command=paste)
    m2.add_command(label='Delete', command=delete)
    m2.add_separator()
    root.config(menu=mymenu)
    mymenu.add_cascade(label='Edit', menu=m2)

    m5 = Menu(mymenu, tearoff=0)
    m5.add_command(label='View Help', command=help)
    m5.add_command(label='Send Feedback', command=feedback)
    m5.add_separator()
    m5.add_command(label='About Notepad', command=about)
    root.config(menu=mymenu)
    mymenu.add_cascade(label='Help', menu=m5)

    scroll=Scrollbar(Textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scroll.set)
    root.mainloop()