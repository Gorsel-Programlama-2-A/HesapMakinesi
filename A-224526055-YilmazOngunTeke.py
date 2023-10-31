from tkinter import *

window = Tk()
window.title("Hesap Makinesi")
window.minsize(width=500, height=400)

window.config(padx=100, pady=80)

total = 0
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
userInput = Entry(width=50)
userInput.pack(side=TOP)

# Total
lbl = Label(text=str(total), background="red")
lbl.pack(side=TOP)

# Buttons
my_button = Button(text="Topla", width=50, command=add)
my_button.pack(side=TOP)

my_button = Button(text="Çıkar", width=50, command=minus)
my_button.pack(side=TOP)

my_button = Button(text="Çarp", width=50, command=multiply)
my_button.pack(side=TOP)

my_button = Button(text="Böl", width=50, command=divide)
my_button.pack(side=TOP)

my_button = Button(text="Üs", width=50, command=power)
my_button.pack(side=TOP)

my_button = Button(text="Karekök", width=50, command=square)
my_button.pack(side=TOP)

my_button = Button(text="C", width=50, command=c)
my_button.pack(side=TOP)

my_button = Button(text="M+", width=50, command=mp)
my_button.pack(side=TOP)

my_button = Button(text="M-", width=50, command=mm)
my_button.pack(side=TOP)

my_button = Button(text="MC", width=50, command=mc)
my_button.pack(side=TOP)

my_button = Button(text="MR", width=50, command=mr)
my_button.pack(side=TOP)

window.mainloop()