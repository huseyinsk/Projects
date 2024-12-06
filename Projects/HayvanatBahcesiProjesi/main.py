from veriDosyalari.HayvanUcretleri import *
from veriDosyalari.MusteriEkle import musteriEkle
from veriDosyalari.MusteriGiris import musteriGiris
from veriDosyalari.YetkiliGiris import yetkiliGiris
from veriDosyalari.MusteriSil import musteriSil

giris = input("Giriş türünüzü (musteri/yonetici) olarak seçiniz: ").lower()
while giris not in ["musteri","yonetici"]:
    print("Yanlış giriş türü girdiniz!")
    giris = input("Giriş türünüzü (musteri/yonetici) olarak seçiniz: ").lower()

if giris == "musteri":
    kayitSorgu = input("Hayvanat Bahçemizin bir üyesi misiniz? (evet/hayır) olarak cevaplayınız :").lower()
    while kayitSorgu not in ["evet","hayır"]:
        print("Yanlış cevap türü girdiniz, Tekrar deneyiniz!")
        kayitSorgu = input("Hayvanat Bahçemizin bir üyesi misiniz? Lütfen (evet/hayır) olarak cevaplayınız :").lower()
    
    if kayitSorgu == "hayır":
        kayitIstekSorgu = input("Kayıt olmak ister misiniz ? :").lower()
        while kayitIstekSorgu not in ["evet","hayır"]:
            print("Yanlış cevap türü verdiniz, Lütfen tekrar deneyiniz!")
            kayitIstekSorgu = input("Kayıt olmak ister misiniz ? :").lower()
        if kayitIstekSorgu == "evet":
            musteriEkle()
        else:
            print("Sistemden çıkış yapıldı.. İyi günler dileriz!")
    else:
        musteriGiris()
        gezi()


else:
    yetkiliGiris()
    yapilmakIstenen = input("Yapmak istediğiniz seçeneği(musterisil/musteriekle) olarak giriniz: ").lower()
    while (yapilmakIstenen not in ["musterisil","musteriekle"]):
        print("Yanlış cevap türü verdiniz, Lütfen tekrar deneyiniz !")
        yapilmakIstenen = input("Yapmak istediğiniz seçeneği(musterisil/musteriekle) olarak giriniz: ").lower()
    
    if yapilmakIstenen == "musteriekle":
        musteriEkle()
    else:
        musteriSil()
