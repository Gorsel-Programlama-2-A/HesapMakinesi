from tkinter import *

# kullanıcının girdiği değeri tanımla
değer = ""

# Rakam veya işlem operatörü butonlarına basıldığında çağrılan fonksiyon
def tusa_bas(tus):
    global değer
    değer = değer + str(tus)
    denklem.set(değer)

# Hesaplama yapan tanım
def hesapla():
    try:
        global değer
        sonuç = str(eval(değer))
        denklem.set(sonuç)
        değer = ""
    except:
        denklem.set("Hata!")
        değer = ""

# Hesap makinesindeki değerleri sıfırlayan kısım
def temizle():
    global değer
    değer = ""
    denklem.set("")

# Pencereyi oluşturur
pencere = Tk()
pencere.configure(background="light green")
pencere.title("Basit Hesap Makinesi")
pencere.geometry("265x125")

# StringVar() sınıfını kullanarak bir değişken oluştur kullanıcı arayüzündeki metin alanlarını güncelleştirme amaçlıdır
denklem = StringVar()
değer_alanı = Entry(pencere, textvariable=denklem)
değer_alanı.grid(columnspan=4, ipadx=70)
denklem.set('Değer girin')

# Butonları oluşturup pozisyonlarını ayarlar
butonlar = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'Temizle', '=', '+'
]

satır_değeri = 2
sütun_değeri = 0

for buton in butonlar:
    if buton == 'Temizle':
        btn = Button(pencere, text=buton, fg='black', bg='red', command=temizle, height=1, width=7)
    elif buton == '=':
        btn = Button(pencere, text=buton, fg='black', bg='red', command=hesapla, height=1, width=7)
    else:
        btn = Button(pencere, text=buton, fg='black', bg='red', command=lambda b=buton: tusa_bas(b), height=1, width=7)

    btn.grid(row=satır_değeri, column=sütun_değeri)
    sütun_değeri += 1

    if sütun_değeri > 3:
        sütun_değeri = 0
        satır_değeri += 1

# Programı başlat
pencere.mainloop()
