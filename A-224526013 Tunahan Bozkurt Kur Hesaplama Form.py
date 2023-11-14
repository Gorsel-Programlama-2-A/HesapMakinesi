# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:13:54 2023

@author: Tunahan
"""

import tkinter as tk
from tkinter import ttk #combobox modülü bunun içinde bulunuyor.

# Dönüştürülecek ihtimaller.
def try_den_dolara(miktar):
    return miktar / 28.50

def try_den_euroya(miktar):
    return miktar / 30.45

def dolar_dan_tryye(miktar):
    return miktar * 28.50

def dolar_dan_euroya(miktar):
    return miktar * 0.93

def euro_dan_tryye(miktar):
    return miktar * 30.45

def euro_dan_dolara(miktar):
    return miktar / 0.93

# Dönüştürme işlemini gerçekleştiren fonksiyon
def hesapla():
    miktar = float(miktar_giris.get())
    dönüştürülen_para_birimi = secim_kaynak.get()
    dönüştürülecek_para_birimi = secim_hedef.get()

    # Dönüşüm fonksiyonunu çağır
    if dönüştürülen_para_birimi == "TRY":
        if dönüştürülecek_para_birimi == "USD":
            sonuc = try_den_dolara(miktar)
        elif dönüştürülecek_para_birimi == "EUR":
            sonuc = try_den_euroya(miktar)
        else:
            sonuc = miktar
    elif dönüştürülen_para_birimi == "USD":
        if dönüştürülecek_para_birimi == "TRY":
            sonuc = dolar_dan_tryye(miktar)
        elif dönüştürülecek_para_birimi == "EUR":
            sonuc = dolar_dan_euroya(miktar)
        else:
            sonuc = miktar
    elif dönüştürülen_para_birimi == "EUR":
        if dönüştürülecek_para_birimi == "TRY":
            sonuc = euro_dan_tryye(miktar)
        elif dönüştürülecek_para_birimi == "USD":
            sonuc = euro_dan_dolara(miktar)
        else:
            sonuc = miktar
    else:
        sonuc = miktar

    # Hesaplanan sonucu yaz
    sonuc_etiketi.config(text=f"Girdiğiniz {miktar} {dönüştürülen_para_birimi} değerin karşılığı: {sonuc:.2f} {dönüştürülecek_para_birimi}")

# bir GUI penceresi oluşturma.
pencere = tk.Tk()
pencere.title("Kur Hesaplama Form - Tunahan Bozkurt")

etiket_miktar = tk.Label(pencere, text="Dönüştürülen miktarı giriniz:")
etiket_miktar.grid(row=0, column=0, padx=10, pady=10)
miktar_giris = tk.Entry(pencere)
miktar_giris.grid(row=0, column=1, padx=10, pady=10)

etiket_kaynak = tk.Label(pencere, text="Bu Birimden:")
etiket_kaynak.grid(row=1, column=0, padx=10, pady=10)
secim_kaynak = ttk.Combobox(pencere, values=["TRY", "USD", "EUR"])
secim_kaynak.set("TRY")
secim_kaynak.grid(row=1, column=1, padx=10, pady=10)

etiket_hedef = tk.Label(pencere, text="Bu Birime Dönüştürülecek:")
etiket_hedef.grid(row=2, column=0, padx=10, pady=10)
secim_hedef = ttk.Combobox(pencere, values=["TRY", "USD", "EUR"])
secim_hedef.set("TRY")
secim_hedef.grid(row=2, column=1, padx=10, pady=10)

btn_donustur = tk.Button(pencere, text="Hesapla!", command=hesapla)
btn_donustur.grid(row=3, column=0, columnspan=2, pady=10)

sonuc_etiketi = tk.Label(pencere, text="Lütfen Miktarı Giriniz")
sonuc_etiketi.grid(row=4, column=0, columnspan=2, pady=10)

pencere.mainloop()