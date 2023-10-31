# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:38:47 2023

@author: Excalibur
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:34:01 2023

@author: Excalibur
"""


def c():
    inputValue.delete(0,tk.END)
    valueSonuc.delete(0,tk.END)

def topla():
    try:
        sayi = float(inputValue.get())
        sonuc_text = float(valueSonuc.get())
        yeni_sonuc = sayi + sonuc_text
        valueSonuc.delete(0, tk.END)
        valueSonuc.insert(0, yeni_sonuc)        
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")
        
def carpma():
    try:
        sayi = float(inputValue.get())
        sonuc_text = float(valueSonuc.get())
        yeni_sonuc = sayi * sonuc_text
        valueSonuc.delete(0, tk.END)
        valueSonuc.insert(0, yeni_sonuc)        
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")
        
def bolme():
    try:
        sayi = float(inputValue.get())
        sonuc_text = float(valueSonuc.get())
        yeni_sonuc = sayi / sonuc_text
        valueSonuc.delete(0, tk.END)
        valueSonuc.insert(0, yeni_sonuc)        
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")
        
def cikarma():
    try:
        sayi = float(inputValue.get())
        sonuc_text = float(valueSonuc.get())
        yeni_sonuc = sayi - sonuc_text
        valueSonuc.delete(0, tk.END)
        valueSonuc.insert(0, yeni_sonuc)        
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")
        
def karekok():
    try:
        sayi = float(inputValue.get())
        sonuc_text = float(valueSonuc.get())
        yeni_sonuc = math.sqrt(sayi)
        valueSonuc.delete(0, tk.END)
        valueSonuc.insert(0, yeni_sonuc)        
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")

def usAl():
    try:
        sayi = float(inputValue.get())
        sonuc_text = float(valueSonuc.get())
        
        yeni_sonuc = math.pow(sayi, sonuc_text)
        valueSonuc.delete(0,tk.END)
        valueSonuc.insert(0, yeni_sonuc)
    except ValueError:
        messagebox.showerror("Hata", "Değeri Giriniz")

import math
import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()
pencere.title("Hesap Makinası Python")
pencere.geometry("400x500")


inputValue = tk.Entry(width=30)
inputValue.grid(row=0, column=1, padx=(0, 10), pady=10, ipady=10, ipadx=0)  

valueSonucText = tk.Label(text="Sonuç:")
valueSonucText.grid(row=1, column=0, padx=10, pady=10)

valueSonuc = tk.Entry(width=30,textvariable="0")
valueSonuc.grid(row=1, column=1, padx=(0, 10), pady=10, ipady=10, ipadx=0) 



toplama_button = tk.Button(text="Topla", width=10, height=2,command=topla)
toplama_button.grid(row=2, column=0, padx=5, pady=5)

cikarma_button = tk.Button(text="Çıkarma", width=10, height=2,command=cikarma)
cikarma_button.grid(row=2, column=1, padx=5, pady=5)

carpma_button = tk.Button(text="Çarpma", width=10, height=2,command=carpma)
carpma_button.grid(row=2, column=2, padx=5, pady=5)


bolme_button = tk.Button(text="Bölme", width=10, height=2,command=bolme)
bolme_button.grid(row=3, column=0, padx=5, pady=5)

karekok_button = tk.Button(text="Karekök", width=10, height=2,command=karekok)
karekok_button.grid(row=3, column=1, padx=5, pady=5)

usAl_button = tk.Button(text="Üs Al", width=10, height=2,command=usAl)
usAl_button.grid(row=3, column=2, padx=5, pady=5)

#

bolme_button = tk.Button(text="MC", width=10, height=2)
bolme_button.grid(row=4, column=0, padx=5, pady=5)

karekok_button = tk.Button(text="C", width=10, height=2,command=c)
karekok_button.grid(row=4, column=1, padx=5, pady=5)

karekok_button = tk.Button(text="Üs Alma", width=10, height=2)
karekok_button.grid(row=4, column=2, padx=5, pady=5)






pencere.mainloop()