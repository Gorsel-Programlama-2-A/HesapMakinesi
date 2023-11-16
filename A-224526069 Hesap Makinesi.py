import tkinter as tk

def on_button_click(deger):
    mevcut = entry_var.get()
    entry_var.set(mevcut + str(deger))

def clear_entry():
    entry_var.set("")

def hesapla():
    try:
        sonuc = eval(entry_var.get())
        entry_var.set(sonuc)
    except Exception as hata:
        entry_var.set("Hata")

pencere = tk.Tk()
pencere.title("Hesap Makinesi")

entry_var = tk.StringVar()
giris_ekrani = tk.Entry(pencere, textvariable=entry_var, justify="right", font=(15))
giris_ekrani.grid(row=0, column=0, columnspan=80)

butonlar = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for buton in butonlar:
    tk.Button(pencere, text=buton, padx=20, pady=20, font=("Arial", 12), command=lambda b=buton: on_button_click(b) if b != '=' else hesapla()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(pencere, text="Temizle", padx=20, pady=20, font=("Arial", 12), command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

pencere.mainloop()
