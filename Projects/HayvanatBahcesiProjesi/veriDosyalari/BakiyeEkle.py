## Bir müşteri kartına bakiye yükleyen python uygulaması
from veriDosyalari.hesapDB import musteri_tcno as sozluk

def bakiyeEkle():
    while True:
        eklenenBakiye = int(input("Eklemek istediğiniz bakiyeyi giriniz: "))
        tc = int(input("Eklenecek olan karta kayıtlı TC NO giriniz: "))
        sifre = input("Eklenecek olan karta ait şifrenizi giriniz: ").lower()

        if (tc in sozluk.keys()) and (sifre in sozluk[tc]["SIFRE"]):
            print("Tebrikler, bakiye yüklenimi gerçekleti!"
                +f"Yüklenen bakiye: {eklenenBakiye}"
                +"Güncel bakiyeniz: ", (sozluk[tc]["BAKIYE"] + eklenenBakiye))
            break
        else:
            print("Hatalı bilgi girdiniz, Lütfen tekrar deneyiniz!")
