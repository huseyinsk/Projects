# Sözleşme işlevi gören uygulama
from veriDosyalari.MusteriDB import *

def sozlesme():
    print("Taksitlerin ödeme günü her ayın ilk günüdür.")
    while True:
        hesapNo = input("Lütfen hesap no'nuzu giriniz: ")
        ad = input("Lütfen adınızı giriniz: ")
        soyad = input("Lütfen soyadınızı giriniz: ")
        sifre = input("Lütfen şifrenizi giriniz: ")
        if (hesapNo in musteri_HesapNO.keys()) and (ad in musteri_HesapNO[hesapNo]["AD"]) and (soyad in musteri_HesapNO[hesapNo]["SOYAD"]) and (sifre in musteri_HesapNO[hesapNo]["SIFRE"]): ## müşteri verileriyle uyuştuğu koşulu kontrol eder
            print("Sözleşme imzalandı.Teşekkür ederiz.")
            break
        else:
            print("Bilgileri yanlış girdiniz. Lütfen tekrar deneyiniz.")