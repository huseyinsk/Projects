## Müşteri giriş işlevi gören python uygulaması
from veriDosyalari.hesapDB import musteri_tcno as sozluk

def musteriGiris():
    sayac = 0
    while sayac < 4:
        tc = int(input("TC kimlik numaranızı giriniz: "))
        sifre = input("Müşteri şifrenizi giriniz: ")

        if (tc in sozluk.keys()) and (sifre == sozluk[tc]["SIFRE"]):
            print("Giriş başarılı !"
                +"\nHS Hayvanat bahçesine Hoş geldiniz ", sozluk[tc]["AD"]," ", sozluk[tc]["SOYAD"])
            break
        elif sayac == 3:
            print("Kartınız bloke oldu. Lütfen yetkili ile görüşünüz !")
            break
        else:
            sayac += 1
            print("Hatalı bilgi girdiniz. kalan deneme hakkınız: ", 4-sayac
                  ,"\nLütfen tekrar deneyiniz! ")

