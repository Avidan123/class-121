from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
root.title("notepad")
root.maxsize(1200,1200)
root.minsize(650,650)

open_img=ImageTk.PhotoImage(Image.open("open.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))

filename=Label(root,text="File Name")
filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename=Entry(root)
input_filename.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""
def openbtn():
    global name
    my_text.delete(1.0, END)
    input_filename.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_filename.insert(END,formated_name)
    root.title(formated_name)
    text_file=open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
    
open_btn=Button(root,image=open_img,text="Open_file",command=openbtn)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

def savebtn():
    input_name=input_filename.get()
    file=open(input_name+".txt","w")
    data=my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_filename.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("info","your file has been saved")
    
save_btn=Button(root,image=save_img,text="Save image",command=savebtn)
save_btn.place(relx=0.15,rely=0.03,anchor=CENTER)

def exitfunc():
    root.destroy()
    
    
    
exit_btn=Button(root,image=exit_img,text="EXIT",command=exitfunc)
exit_btn.place(relx=0.9,rely=0.03,anchor=CENTER)


root.mainloop()
