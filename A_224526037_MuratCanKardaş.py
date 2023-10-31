import tkinter as tk
import math

class HesapMakinesi:
    def __init__(self, pencere):
        self.pencere = pencere
        pencere.title("Hesap Makinesi")
        pencere.geometry("300x400") 

        self.toplam = 0
        self.girilen_sayi = 0
        self.gecerli_islem = ""
        self.sonuc_gosterimi = tk.Entry(pencere)
        self.sonuc_gosterimi.grid(row=0, column=0, columnspan=4)

        b0 = self.buton_olustur(0)
        b1 = self.buton_olustur(1)
        b2 = self.buton_olustur(2)
        b3 = self.buton_olustur(3)
        b4 = self.buton_olustur(4)
        b5 = self.buton_olustur(5)
        b6 = self.buton_olustur(6)
        b7 = self.buton_olustur(7)
        b8 = self.buton_olustur(8)
        b9 = self.buton_olustur(9)

        toplama_butonu = self.islem_butonu_olustur("+", self.topla)
        cikarma_butonu = self.islem_butonu_olustur("-", self.cikar)
        carpma_butonu = self.islem_butonu_olustur("*", self.carp)
        bolme_butonu = self.islem_butonu_olustur("/", self.bol)
        karekok_butonu = self.islem_butonu_olustur("√", self.karekok_al)
        us_alma_butonu = self.islem_butonu_olustur("^", self.us_al)

        esittir_butonu = tk.Button(pencere, text="=", command=self.sonuc_hesapla)

        temizleme_butonu = tk.Button(pencere, text="C", command=self.sonuc_temizle)

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

    def buton_olustur(self, deger):
        return tk.Button(self.pencere, text=deger, command=lambda num=deger: self.sayi_gir(num))

    def islem_butonu_olustur(self, metin, komut):
        return tk.Button(self.pencere, text=metin, command=komut)

    def sayi_gir(self, num):
        self.girilen_sayi = (self.girilen_sayi * 10) + num
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.girilen_sayi))

    def topla(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam += self.girilen_sayi
        self.gecerli_islem = "+"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def cikar(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam -= self.girilen_sayi
        self.gecerli_islem = "-"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def carp(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam *= self.girilen_sayi
        self.gecerli_islem = "*"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def bol(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            if self.girilen_sayi != 0:
                self.toplam /= self.girilen_sayi
            else:
                self.toplam = "Hata: Sıfıra bölünemez."
        self.gecerli_islem = "/"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def karekok_al(self):
        self.toplam = math.sqrt(self.girilen_sayi)
        self.gecerli_islem = "√"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def us_al(self):
        if self.gecerli_islem == "":
            self.toplam = self.girilen_sayi
        else:
            self.toplam = self.toplam ** self.girilen_sayi
        self.gecerli_islem = "^"
        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))

    def sonuc_hesapla(self):
        if self.gecerli_islem == "+":
            self.toplam += self.girilen_sayi
        elif self.gecerli_islem == "-":
            self.toplam -= self.girilen_sayi
        elif self.gecerli_islem == "*":
            self.toplam *= self.girilen_sayi
        elif self.gecerli_islem == "/":
            if self.girilen_sayi != 0:
                self.toplam /= self.girilen_sayi
            else:
                self.toplam = "Hata: Sıfıra bölünemez."
        elif self.gecerli_islem == "√":
            self.toplam = math.sqrt(self.toplam)
        elif self.gecerli_islem == "^":
            self.toplam = self.toplam ** self.girilen_sayi

        self.sonuc_gosterimi.delete(0, tk.END)
        self.sonuc_gosterimi.insert(tk.END, str(self.toplam))
        self.girilen_sayi = 0
        self.gecerli_islem = ""

    def sonuc_temizle(self):
        self.toplam = 0
        self.girilen_sayi = 0
        self.gecerli_islem = ""
        self.sonuc_gosterimi.delete(0, tk.END)

pencere = tk.Tk()
hesapMakinesi = HesapMakinesi(pencere)
pencere.mainloop()