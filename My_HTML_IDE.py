from tkinter import *
from tkinter import filedialog
import os 
import webbrowser
from PIL import ImageTk,Image
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background='#6699CC')

open_image = ImageTk.PhotoImage(Image.open('open.png'))
save_image = ImageTk.PhotoImage(Image.open('save.png'))
exit_image = ImageTk.PhotoImage(Image.open('exit.jpg'))

label1 = Label(root,text='File Name:')
label1.place(relx=0.28,rely=0.03,anchor=CENTER)

inputFileName = Entry(root)
inputFileName.place(relx=0.5,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80,bg='white',fg='black')
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

name = ''
file_path = ''

def openFile():
    global name
    global file_path
    my_text.delete(1.0,END)
    inputFileName.delete(0,END)
    html_file = filedialog.askopenfilename(title='Open html file',filetypes=(('html Files','*.html'),))
    print(html_file)
    file_path = html_file
    name = os.path.basename(html_file)
    formatted_name = name.split('.')[0]
    formatted_name.insert(END,formatted_name)
    root.title(formatted_name)
    html_file = open(name,'r')
    paragraph = html_file.read()
    my_text.insert(END,formatted_name)
    html_file.close()
    
def save():
    input_name = inputFileName.get()
    file = open(input_name + ".html",'w')
    data = my_text.get('1.0',END)
    print(data)
    file.write(data)
    inputFileName.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo('Update','Your data has been successfully updated')
    
def run_html_file():
    global file_path
    webbrowser.open_new('file://' + file_path)
    
    
btn = Button(root,img=open_image,command=openFile)
btn.place(relx=0.1,rely=0.03,anchor=CENTER)

btn2 = Button(root,img=save_image,command=save)
btn2.place(relx=0.15,rely=0.03,anchor=CENTER)

btn3 = Button(root,img=exit_image,command=save)
btn3.place(relx=0.2,rely=0.03,anchor=CENTER)

root.mainloop()