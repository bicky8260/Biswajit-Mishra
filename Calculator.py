'''CALCULATOR BY BICKY(ME)'''
from tkinter import *
import tkinter.messagebox as tmsg

def click(event):
    global scvalue
    text = event.widget.cget("text")  #It gives the button on which we have just clicked 
    if scvalue.get() == "Error":
        scvalue.set("")
        scvalue.set(text)
        screen.update()
        return
    if scvalue.get() == "0":
        scvalue.set("")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = e
                scvalue.set(f"{value} not allowed.")
                return
        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()
        scvalue.set("0")
        screen.update()
    
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

def help():
    tmsg.showinfo("HELP","Sorry Sir/Ma'am we cant help you right now because it is a simple calculator.")

root = Tk()
root.geometry("500x850")
root.title("CALCULATOR by Bicky")
root.configure(bg="beige")
root.wm_iconbitmap("Calculator.ico")

scvalue = StringVar()
scvalue.set("0")
screen = Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=20)

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="Help",command=help)
root.configure(menu=mainmenu)
mainmenu.add_cascade(label="≡",menu=m1)

frame1 = Frame(root,bg="pink")
b = Button(frame1,text="AC",padx=7,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="00",padx=6,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="%",padx=10,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="/",padx=18,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root,bg="pink")
b = Button(frame1,text="9",padx=22,pady=15,font="lucida 30 bold",bg="lavender blush")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="8",padx=18,pady=15,font="lucida 30 bold",bg="light pink")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="7",padx=18,pady=15,font="lucida 30 bold",bg="lavender blush")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="*",padx=15,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root,bg="pink")
b = Button(frame1,text="6",padx=19,pady=15,font="lucida 30 bold",bg="light pink")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="5",padx=18,pady=15,font="lucida 30 bold",bg="lavender blush")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="4",padx=18,pady=15,font="lucida 30 bold",bg="light pink")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="-",padx=19,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root,bg="pink")
b = Button(frame1,text="3",padx=17,pady=15,font="lucida 30 bold",bg="lavender blush")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="2",padx=18,pady=15,font="lucida 30 bold",bg="light pink")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="1",padx=17,pady=15,font="lucida 30 bold",bg="lavender blush")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="+",padx=17,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root,bg="pink")
b = Button(frame1,text="0",padx=84,pady=18,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text=".",padx=17,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame1,text="=",padx=17,pady=15,font="lucida 30 bold",bg="pale violet red")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
frame1.pack()

root.mainloop()
     