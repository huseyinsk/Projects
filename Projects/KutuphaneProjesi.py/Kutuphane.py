## Kütüphane projesi 
from veriDosyalari.OgrenciGiris import ogrenciGiris
from veriDosyalari.YetkiliGiris import yetkiliGiris
from veriDosyalari.OgrenciEkle import ogrenciEkle
from veriDosyalari.OgrenciSil import ogrenciSil
from veriDosyalari.OgrenciKontrol import ogrenciKontrol
from veriDosyalari.YetkiliEkle import yetkiliEkle
from veriDosyalari.YetkiliSil import yetkiliSil

print("HS Kütüphanesine hoş geldiniz.")
giris = input("Giriş türünüzü (ogrenci/yonetici) olarak seçiniz: ").lower()
while giris not in ["ogrenci","yonetici"]:
    print("Yanlış giriş türü girdiniz!")
    giris = input("Giriş türünüzü (ogrenci/yonetici) olarak seçiniz: ").lower()

if giris == "ogrenci":
    kayitSorgu = input("Kütüphanemizin bir üyesi misiniz? (evet/hayır) olarak cevaplayınız :").lower()
    while kayitSorgu not in ["evet","hayır"]:
        print("Yanlış cevap türü girdiniz, Tekrar deneyiniz!")
        kayitSorgu = input("Kütüphanemizin bir üyesi misiniz? Lütfen (evet/hayır) olarak cevaplayınız :").lower()
    
    if kayitSorgu == "hayır":
        kayitIstekSorgu = input("Kayıt olmak ister misiniz ? :").lower()
        while kayitIstekSorgu not in ["evet","hayır"]:
            print("Yanlış cevap türü verdiniz, Lütfen tekrar deneyiniz!")
            kayitIstekSorgu = input("Kayıt olmak ister misiniz ? :").lower()
        if kayitIstekSorgu == "evet":
            ogrenciEkle()
        else:
            print("Sistemden çıkış yapıldı.. İyi günler dileriz!")
    else:
        ogrenciGiris()

else:
    yetkiliGiris()
    yapilmakIstenen = input("Yapmak istediğiniz seçeneği(ogrenciekle/ogrencisil/ogrencikontrol/yetkiliekle/yetkilisil) olarak giriniz: ").lower()
    while (yapilmakIstenen not in ["ogrenciekle","ogrencisil","ogrencikontrol","yetkiliekle","yetkilisil"]):
        print("Yanlış cevap türü verdiniz, Lütfen tekrar deneyiniz !")
        yapilmakIstenen = input("Yapmak istediğiniz seçeneği(ogrenciekle/ogrencisil/ogrencikontrol/yetkiliekle/yetkilisil) olarak giriniz: ").lower()
    
    if yapilmakIstenen == "ogrenciekle":
        ogrenciEkle()
    elif yapilmakIstenen == "ogrencisil":
        ogrenciSil()
    elif yapilmakIstenen == "ogrencikontrol":
        ogrenciKontrol()
    elif yapilmakIstenen == "yetkiliekle":
        yetkiliEkle()
    else:
        yetkiliSil()

