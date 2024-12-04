# Mobil bankacılık giriş ekranını uygulayan uygulama
from MusteriDB import *
from Yapilmakİstenen import yapilmakIstenen
import time

def giris():
    while True:
        print("Lütfen bekleyiniz..")
        time.sleep(2)  ## 2 saniye bekletir
        hesapNo = input("Lütfen hesap numaranızı giriniz: ")
        sifre = input("Lütfen müşteri şifrenizi giriniz: ")
        if(hesapNo in musteri_HesapNO.keys()) and (sifre in musteri_HesapNO[hesapNo]["SIFRE"]): ## müşteri verileriyle uyuştuğu koşulu kontrol eder
            print("Giriş başarılı.. Hoş geldiniz !")
            yapilmakIstenen()
            break

        else:
            print("Yanlış bilgi girdiniz lütfen tekrar deneyiniz !")
            time.sleep(1)
            continue    