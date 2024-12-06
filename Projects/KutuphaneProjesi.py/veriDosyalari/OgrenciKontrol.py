## Öğrencinin kayıtlı olup olmadığını kontrol eden python uygulaması
from veriDosyalari.hesaplarDB import ogrenci_tcNO as sozluk

def ogrenciKontrol():
    tc = int(input("Sorgulamak istediğiniz tc'yi giriniz: ")) 
    ad = input("Sorgulamak istediğiniz adı giriniz: ").upper()
    soyad = input("Sorgulamak istediğiniz soyadı giriniz: ").upper()
    sifre = input("Sorgulamak istediğiniz şifreyi giriniz: ")
    adi = sozluk[tc]["AD"]
    soyadi = sozluk[tc]["SOYAD"]
    sifresi = sozluk[tc]["SIFRE"]

    if (tc in sozluk.keys()) and (ad == adi) and (soyad == soyadi) and (sifre == sifresi):
        print("Vermiş olduğunuz bilgilere ait öğrenci bulunmaktadır")
        print(f"Adı: {adi}" f"\nSoyadı: {soyadi}"+f"\n TC No'su: {tc}" +f"\nŞifresi: {sifresi}")
    else:
        print("Sistemde bu bilgilere ait öğrenci bulunmamaktadır")