## Öğrenci giriş işlevi gören python uygulaması
from veriDosyalari.hesaplarDB import ogrenci_tcNO

def ogrenciGiris():
    sayac = 0
    while sayac < 4:
        tc = int(input("TC kimlik numaranızı giriniz: "))
        sifre = input("Öğrenci şifrenizi giriniz: ")

        if (tc in ogrenci_tcNO.keys()) and (sifre == ogrenci_tcNO[tc]["SIFRE"]):
            print("Giriş başarılı !"
                +"\nHoş geldiniz ", ogrenci_tcNO[tc]["AD"]," ", ogrenci_tcNO[tc]["SOYAD"])
            break
        elif sayac == 3:
            print("Kartınız bloke oldu. Lütfen yetkili ile görüşünüz !")
            break
        else:
            sayac += 1
            print("Hatalı bilgi girdiniz. kalan deneme hakkınız: ", 4-sayac
                  ,"\nLütfen tekrar deneyiniz! ")

