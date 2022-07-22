import tkinter as tk
import random
from PIL import Image,ImageTk
from tkinterdnd2 import *
x=100
y=300
imgesA=[]


def btn_clickSh():
    global imgesA
    global x,y

    canvas.delete('all')
    x=100
    y=300
    random.shuffle(imgesA)
    for i in range(len(imgesA)):
        canvas.create_rectangle(x-200/2,y-200/2,x+200/2,y+200/2,outline='#e8ecef',fill='#fff')
        canvas.create_image(x,y,image=imgesA[i])
        x+=200
        if x>800:
            x-=800
            y+=205
    canvas.pack()

def drop(event):
    global display_image,canvas
    global x,y
    global imgesA
    canvas.create_line(100,100,800,100,fill='#fefefe',width=5)
    img=Image.open(event.data)
    img.thumbnail((200,200))
    display_image=ImageTk.PhotoImage(img)
    imgesA.append(display_image)
    for i in range(len(imgesA)):
        canvas.create_rectangle(x-200/2,y-200/2,x+200/2,y+200/2,outline='#e8ecef',fill='#fff')
        canvas.create_image(x,y,image=imgesA[-1])
    if x>600:
        x-=800
        y+=205
    x+=200
    canvas.pack()


def btn_clickDe():
    global imgesA
    global x,y
    canvas.delete('all')
    imgesA = []
    x=100
    y=300
display_image=None
root=TkinterDnD.Tk()
#root=tk.Tk()
root.geometry("800x1000")
canvas=tk.Canvas(width=800,height=1000,relief="ridge",borderwidth="2",bg='#fefefe')
root.title('imagespack2')
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>',drop)

btnDe=tk.Button(text="delete",command=btn_clickDe)
btnDe.place(x=100,y=50)
btnSh=tk.Button(text="shuffle",command=btn_clickSh)
btnSh.place(x=150,y=50)
root.mainloop()
