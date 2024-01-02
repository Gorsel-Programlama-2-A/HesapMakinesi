import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import * 
from Ogrenci_Bilgi import * 

uygulama = QApplication(sys.argv) 
pencere = QMainWindow() 
ui = Ui_MainWindow()
ui.setupUi(pencere) 
pencere.show() 

import sqlite3

baglanti = sqlite3.connect("ogrenci.db")
islem = baglanti.cursor() 
baglanti.commit() 

table = islem.execute("create table if not exists ogrenci(ID INTEGER PRIMARY KEY AUTOINCREMENT, numarasi TEXT, adi TEXT, soyadi TEXT, bolumu TEXT, dersAdi TEXT) ")
baglanti.commit()


def Ogrenci_Ekle():
    Numarasi = ui.lblNumarasi.text()
    Adi = ui.lblAdi.text()
    Soyadi = ui.lblSoyadi.text()
    Bolumu = ui.cbBolumu.currentText()
    DersAdi = ui.cbDersAdi.currentText()
    
    try:
        ekle = "insert into ogrenci(numarasi, adi, soyadi, bolumu, dersAdi) values(?,?,?,?,?)"
        islem.execute(ekle,(Numarasi, Adi, Soyadi, Bolumu, DersAdi))
        baglanti.commit()
        Ogrenci_Listele()
        ui.statusbar.showMessage("Öðrenci Kaydedildi.", 10000)
    except Exception as error:
        ui.statusbar.showMessage("HATA! Öðrenci Kaydedilemedi. :"+str(error))
        
def Ogrenci_Listele():
    ui.tblListele.clear()
    ui.tblListele.setHorizontalHeaderLabels(("ID", "Numarası", "Adı", "Soyadı", "Bölümü", "Dersin Adı"))
    
    sorgu = "select * from ogrenci"
    islem.execute(sorgu)
    
    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tblListele.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

def Ogrenci_DersListele():

    ui.tblListele.clear()
    ui.tblListele.setHorizontalHeaderLabels(("Numarasý", "Adý", "Soyadý", "Bölümü", "Dersin Adı"))
    ui.tblListele.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    dersAdi = ui.cbDersSec.currentText()

    sorgu = "select * from ogrenci where dersAdi = ?"

    islem.execute(sorgu, (dersAdi,))

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tblListele.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
            
def Ogrenci_Sil():
    sil_mesaj = QMessageBox.question(pencere, "Silme Onayla", "Öðrenci kaydý silmek mi istiyorsunuz?", QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tblListele.selectedItems()

        if secilen_kayit:
            silinecek_kayitID = ui.tblListele.item(secilen_kayit[0].row(), 0).text()  

            sorgu = "delete from ogrenci where ID =?"
            try:
                islem.execute(sorgu, (silinecek_kayitID,))
                baglanti.commit()
                ui.statusbar.showMessage("Kayýt baþarýyla silindi!")
                Ogrenci_Listele()
            except Exception as error:
                ui.statusbar.showMessage("HATA! Kayýt silinemedi." + str(error))
        else:
            ui.statusbar.showMessage("HATA! Lütfen Kayýt seçin.")
    else:
        ui.statusbar.showMessage("Silme iþlemi iptal edildi.")

        
    
        
def Ogrenci_Guncelle():
    guncelle_mesaj = QMessageBox.question(pencere, "Güncellemeyi onaylýyor musunuz", "Güncellensin mi?", QMessageBox.Yes | QMessageBox.No)
    if guncelle_mesaj == QMessageBox.Yes:
        try:
            ID = ui.lblSeciliOgrenci.text()
            Numarasi = ui.lblNumarasi.text()
            Adi = ui.lblAdi.text()
            Soyadi = ui.lblSoyadi.text()
            Bolumu = ui.cbBolumu.currentText()
            DersAdi = ui.cbDersAdi.currentText()
            
            if Numarasi == "" and Adi == "" and Soyadi == "" and Bolumu == "" and DersAdi == "":
                islem.execute("update ogrenci set dersAdi =? where ID =?", (DersAdi, ID))
            else:
                islem.execute("update ogrenci set Adi =?, soyadi =?, bolumu =?, dersAdi =?, numarasi =? where ID =?", (Adi, Soyadi, Bolumu, DersAdi, Numarasi, ID))
            baglanti.commit()
            Ogrenci_Listele()
            ui.statusbar.showMessage("Baþarýlý! Öðrenci Güncellendi°.")
        except Exception as error:
             ui.statusbar.showMessage("HATA! Güncelleme baþarýsýz. :" + str(error))
    else:
        ui.statusbar.showMessage("Güncelleme iptal edildi.")


def Formu_Temizle():
    for widget in ui.centralwidget.findChildren((QLineEdit, QComboBox)):
        if isinstance(widget, QLineEdit):
            widget.clear()
        elif isinstance(widget, QComboBox):
            widget.setCurrentIndex(0)
            
def Ogrenci_Duzenle():
    try:
       
        ID = ui.tblListele.item(ui.tblListele.currentRow(), 0).text()
        Numarasi = ui.tblListele.item(ui.tblListele.currentRow(), 1).text() 
        Adi = ui.tblListele.item(ui.tblListele.currentRow(), 2).text() 
        Soyadi = ui.tblListele.item(ui.tblListele.currentRow(), 3).text()  
        Bolumu = ui.tblListele.item(ui.tblListele.currentRow(), 4).text() 
        DersAdi = ui.tblListele.item(ui.tblListele.currentRow(), 5).text()  

        ui.lblSeciliOgrenci.setText(ID)
        ui.lblNumarasi.setText(Numarasi)
        ui.lblAdi.setText(Adi)
        ui.lblSoyadi.setText(Soyadi)
        ui.cbBolumu.setCurrentText(Bolumu)
        ui.cbDersAdi.setCurrentText(DersAdi)

        ui.statusbar.showMessage("Başarıyls kaydedildi")
    except Exception as error:
        ui.statusbar.showMessage("HATA! Güncellenmedi. :" + str(error))


ui.btnEkle.clicked.connect(Ogrenci_Ekle)
ui.btnListele.clicked.connect(Ogrenci_Listele)
ui.btnSil.clicked.connect(Ogrenci_Sil)
ui.btnGuncelle.clicked.connect(Ogrenci_Guncelle)
ui.btnTemizle.clicked.connect(Formu_Temizle)
ui.btnDuzenle.clicked.connect(Ogrenci_Duzenle)
ui.btnDersListele.clicked.connect(Ogrenci_DersListele)

Ogrenci_Listele()


sys.exit(uygulama.exec_()) 

