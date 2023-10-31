import tkinter as tk

def hesap_makinesi():
    pencere = tk.Tk()
    pencere.title("Hesap Makinesi")

    ekran = tk.Entry(pencere, width=20, borderwidth=7)
    ekran.grid(row=0, column=0, columnspan=4)
    

    def button_click(sayi):
        mevcut = ekran.get()
        ekran.delete(0, tk.END)
        ekran.insert(0, mevcut + sayi)

    def hesapla():
        try:
            sonuc = eval(ekran.get())
            ekran.delete(0, tk.END)
            ekran.insert(0, sonuc)
        except:
            ekran.delete(0, tk.END)
            ekran.insert(0, "Hata")
            
            
    buttons = [
        '7','8','9','/',
        '4','5','6','*',
        '1','2','3','-',
        '0','.','=','+',
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        tk.Button(pencere, text=button, padx=20, pady=20, command=lambda b=button: button_click(b) if b != "=" else hesapla()).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    pencere.mainloop()

hesap_makinesi()
