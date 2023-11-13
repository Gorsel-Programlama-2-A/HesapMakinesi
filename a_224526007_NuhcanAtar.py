from tkinter import *
from tkinter import ttk
import math

memory = 0

def buttonHesapla(secilisembol):
    input_text = input_widget.get()
    
    if(secilisembol) == "=":
        try:
            sonuc = eval(input_text)
            input_widget.delete(0, 'end')
            input_widget.insert('end', str(sonuc))
        except Exception as e:
            input_widget.delete(0, 'end')
            input_widget.insert('end', 'Hata')
    elif secilisembol == "C":
        input_widget.delete(0, 'end')
    elif secilisembol == "√":
        input_widget.delete(0,'end')
        input_widget.insert('end', str(math.sqrt(float(input_text))))
    elif secilisembol == "^":
        input_widget.delete(0,'end')
        input_widget.insert('end', input_text + "**")
    elif secilisembol == "M+":
        
        bellekEkle(input_text)
        
    elif secilisembol == "M-":
        
        bellekAzalt(input_text)
        
    elif secilisembol == "MC":
        
        bellegitamamensil()
        
    elif secilisembol == "MR":
        
        bellegicagir()
    else:
        input_widget.delete(0,'end')
        input_widget.insert('end', input_text + str(secilisembol))
    
def bellekEkle(value):
    global memory
    try:
        memory+= eval(value)
    except Exception as e:
        input_widget.delete(0, 'end')
        input_widget.insert('end', "Hata")

def bellekAzalt(value):
    global memory
    try:
        memory-=eval(value)
    except Exception as e:
        input_widget.delete(0,'end')
        input_widget.insert('end', "Hata")
        
def bellegitamamensil():
    global memory
    memory = 0
    

def bellegicagir():
    global memory
    input_widget.delete(0, 'end')
    input_widget.insert('end', str(memory))    
        

anaform = Tk()

anaform.title("Hesap Makinası")
anaform.geometry("400x400")


# inputlar
input_widget = Entry(anaform, width=30, font=('Arial', '16'))
input_widget.grid(row=0, column=0, columnspan=4,padx=5,pady=5)


# butonlar listesi
buttons = [
    ('C', 1, 0), ('M+', 1, 1), ('M-', 1, 2), ('MC', 1, 3),
    ('MR', 2, 0), ('√', 2, 1), ('^', 2, 2), ('/', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('0', 6, 0), ('=', 6, 1)
    ]


for (text, row, column) in buttons:
    button_widget = ttk.Button(anaform, text=text, width=6, command=lambda t=text: buttonHesapla(t))
    button_widget.grid(row=row,column=column, padx=5,pady=5)

anaform.mainloop()
