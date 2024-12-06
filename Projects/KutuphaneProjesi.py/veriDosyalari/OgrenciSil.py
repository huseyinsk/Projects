## Veri dosyasından öğrenci silen python dosyası
from veriDosyalari.hesaplarDB import ogrenci_tcNO as sozluk

def ogrenciSil():
    tc = int(input("Silmek istediğiniz öğrenci kaydına ait tc kimlik no'yu giriniz: "))
    del sozluk[tc]