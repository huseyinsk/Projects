from veriDosyalari.hesaplarDB import ogrenci_tcNO as sozluk

def ogrenciEkle(): 
    tc = int(input("Lütfen kullanmak istediğiniz tc'yi giriniz: ")) 
    ad = input("Lütfen adını giriniz: ").upper()
    soyad = input("Lütfen Soyadını giriniz: ").upper()
    sifre = input("Lütfen kullanmak istediğiniz şifreyi giriniz: ")
    
    print(f"HS Kütüphanesine hoş geldiniz sayın {ad} {soyad}.")
    print(f"Şifreniz {sifre}'dir.\nSizi aramızda görmekten minnettarız !")
    sozluk[tc] = {}

    bilgiler = sozluk[tc]
    def bilgiEkle(ad,soyad,sifre): 
        bilgiler["AD"] = ad
        bilgiler["SOYAD"] = soyad
        bilgiler["SIFRE"] = sifre

    bilgiEkle(ad,soyad,sifre)
