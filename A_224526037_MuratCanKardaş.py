import tkinter as tk
import math

def sayi_gir(num):
    global girilen_sayi
    girilen_sayi = num
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(girilen_sayi))

def islem_butonu_olustur(metin, komut):
    return tk.Button(pencere, text=metin, command=lambda: kullanilan_islem.set(komut))

def topla():
    global toplam, girilen_sayi, gecerli_islem
    if gecerli_islem == "":
        toplam = girilen_sayi
    else:
        toplam += girilen_sayi
    gecerli_islem = "+"
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))

def cikar():
    global toplam, girilen_sayi, gecerli_islem
    if gecerli_islem == "":
        toplam = girilen_sayi
    else:
        toplam -= girilen_sayi
    gecerli_islem = "-"
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))

def carp():
    global toplam, girilen_sayi, gecerli_islem
    if gecerli_islem == "":
        toplam = girilen_sayi
    else:
        toplam *= girilen_sayi
    gecerli_islem = "*"
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))

def bol():
    global toplam, girilen_sayi, gecerli_islem
    if gecerli_islem == "":
        toplam = girilen_sayi
    else:
        if girilen_sayi != 0:
            toplam /= girilen_sayi
        else:
            toplam = "Hata: Sıfıra bölünemez."
    gecerli_islem = "/"
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))

def karekok_al():
    global toplam, girilen_sayi, gecerli_islem
    toplam = math.sqrt(girilen_sayi)
    gecerli_islem = "√"
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))

def us_al():
    global toplam, girilen_sayi, gecerli_islem
    if gecerli_islem == "":
        toplam = girilen_sayi
    else:
        toplam = toplam ** girilen_sayi
    gecerli_islem = "^"
    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))

def sonuc_hesapla():
    global toplam, girilen_sayi, gecerli_islem
    if gecerli_islem == "+":
        toplam += girilen_sayi
    elif gecerli_islem == "-":
        toplam -= girilen_sayi
    elif gecerli_islem == "*":
        toplam *= girilen_sayi
    elif gecerli_islem == "/":
        if girilen_sayi != 0:
            toplam /= girilen_sayi
        else:
            toplam = "Hata: Sıfıra bölünemez."
    elif gecerli_islem == "√":
        toplam = math.sqrt(toplam)
    elif gecerli_islem == "^":
        toplam = toplam ** girilen_sayi

    sonuc_gosterimi.delete(0, tk.END)
    sonuc_gosterimi.insert(tk.END, str(toplam))
    girilen_sayi = 0
    gecerli_islem = ""

def sonuc_temizle():
    global toplam, girilen_sayi, gecerli_islem
    toplam = 0
    girilen_sayi = 0
    gecerli_islem = ""
    sonuc_gosterimi.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x400")

toplam = 0
girilen_sayi = 0
gecerli_islem = ""
kullanilan_islem = tk.StringVar()
sonuc_gosterimi = tk.Entry(pencere)
sonuc_gosterimi.grid(row=0, column=0, columnspan=4)

b0 = tk.Button(pencere, text=0, command=lambda num=0: sayi_gir(num))
b1 = tk.Button(pencere, text=1, command=lambda num=1: sayi_gir(num))
b2 = tk.Button(pencere, text=2, command=lambda num=2: sayi_gir(num))
b3 = tk.Button(pencere, text=3, command=lambda num=3: sayi_gir(num))
b4 = tk.Button(pencere, text=4, command=lambda num=4: sayi_gir(num))
b5 = tk.Button(pencere, text=5, command=lambda num=5: sayi_gir(num))
b6 = tk.Button(pencere, text=6, command=lambda num=6: sayi_gir(num))
b7 = tk.Button(pencere, text=7, command=lambda num=7: sayi_gir(num))
b8 = tk.Button(pencere, text=8, command=lambda num=8: sayi_gir(num))
b9 = tk.Button(pencere, text=9, command=lambda num=9: sayi_gir(num))

toplama_butonu = islem_butonu_olustur("+", topla)
cikarma_butonu = islem_butonu_olustur("-", cikar)
carpma_butonu = islem_butonu_olustur("*", carp)
bolme_butonu = islem_butonu_olustur("/", bol)
karekok_butonu = islem_butonu_olustur("√", karekok_al)
us_alma_butonu = islem_butonu_olustur("^", us_al)

esittir_butonu = tk.Button(pencere, text="=", command=sonuc_hesapla)
temizleme_butonu = tk.Button(pencere, text="C", command=sonuc_temizle)

butonlar = [
    [b7, b8, b9, toplama_butonu],
    [b4, b5, b6, cikarma_butonu],
    [b1, b2, b3, carpma_butonu],
    [temizleme_butonu, b0, esittir_butonu, bolme_butonu],
    [karekok_butonu, us_alma_butonu]
]

for i in range(5):
    for j in range(4):
        if i == 4 and j > 1:
            break
        butonlar[i][j].grid(row=i+1, column=j)

pencere.mainloop()

