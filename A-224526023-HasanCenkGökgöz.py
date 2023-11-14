from tkinter import *


window = Tk()
window.title("Hesap Makinesi")
window.maxsize(width=600, height=500)
window.configure(bg='purple')

window.config(padx=100, pady=80)

total =  size=0
holder = []

# Functions
def add():
    global total
    total += float(userInput.get())
    userInput.delete(0, END)
    lbl.config(text=total)

def multiply():
    global total
    total *= float(userInput.get())
    userInput.delete(0, END)
    lbl.config(text=total)

def divide():
    global total
    total /= float(userInput.get())
    userInput.delete(0, END)
    lbl.config(text=total)

def minus():
    global total
    total -= float(userInput.get())
    userInput.delete(0, END)
    lbl.config(text=total)

def power():
    global total
    total = pow(total, float(userInput.get()))
    userInput.delete(0, END)
    lbl.config(text=total)

def square():
    global total
    total = pow(total, 0.5)
    userInput.delete(0, END)
    lbl.config(text=total)

def c():
    global total
    total = 0
    userInput.delete(0, END)
    lbl.config(text=total)

def mp():
    global holder
    holder.append(float(userInput.get()))
    if len(holder) > 2:
        holder = [holder[0] + holder[1]]

def mm():
    global holder
    holder.append(-float(userInput.get()))
    if len(holder) > 2:
        holder = [holder[0] + holder[1]]

def mc():
    global holder
    holder = []

def mr():
    global holder
    lbl.config(text=sum(holder))

# Input
userInput = Entry(width=30)
userInput.pack(side=TOP)

# Total
lbl = Label(text=str(total), background="pink",)
lbl.pack(side=TOP)

# Buttons
my_button = Button(text="+", width=5, background="yellow", command=add)
my_button.pack(side=LEFT)

my_button = Button(text="-", width=5, background="yellow",command=minus)
my_button.pack(side=LEFT)

my_button = Button(text="*", width=5, background="yellow",command=multiply)
my_button.pack(side=LEFT)

my_button = Button(text="/", width=5, background="yellow",command=divide)
my_button.pack(side=LEFT)

my_button = Button(text="^", width=5, background="yellow",command=power)
my_button.pack(side=RIGHT)

my_button = Button(text="√", width=5, background="yellow",command=square)
my_button.pack(side=RIGHT)

my_button = Button(text="C", width=5, background="yellow",command=c)
my_button.pack(side=RIGHT)

my_button = Button(text="M+", width=5, background="yellow",command=mp)
my_button.pack(side=RIGHT)

my_button = Button(text="M-", width=5, background="yellow",command=mm)
my_button.pack(side=RIGHT)

my_button = Button(text="MC", width=5, background="yellow",command=mc)
my_button.pack(side=RIGHT)

my_button = Button(text="MR", width=5, background="yellow",command=mr)
my_button.pack(side=RIGHT)



window.mainloop()
