## Yetkili giriş işlevi gören python uygulaması
from veriDosyalari.hesaplarDB import yetkili_tcNO

def yetkiliGiris():
    sayac = 0
    while sayac < 4:
        tc = int(input("TC kimlik numaranızı giriniz: "))
        sifre = input("Yetkili giriş şifrenizi giriniz: ")

        if (tc in yetkili_tcNO.keys()) and (sifre == yetkili_tcNO[tc]["SIFRE"]):
            print("Giriş başarılı !"
                +"\nHoş geldiniz ", yetkili_tcNO[tc]["AD"]," ", yetkili_tcNO[tc]["SOYAD"])
            break
        elif sayac == 3:
            print("Kartınız bloke oldu. Lütfen yetkili ile görüşünüz !")
            break
        else:
            sayac += 1
            print("Hatalı bilgi girdiniz. kalan deneme hakkınız: ", 4-sayac
                  ,"\nLütfen tekrar deneyiniz! ")

