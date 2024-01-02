from PyQt5 import uic

with open('Ogrenci_Bilgi.py', 'w', encoding="utf-8") as ceviri:
    uic.compileUi("Ogrenci_Bilgi.ui", ceviri)
    