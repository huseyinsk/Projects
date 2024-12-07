from veriDosyalari.hesapDB import musteri_tcno as sozluk

def musteriEkle(): 
    tc = int(input("Lütfen kullanmak istediğiniz tc'yi giriniz: ")) 
    ad = input("Lütfen adını giriniz: ").upper()
    soyad = input("Lütfen Soyadını giriniz: ").upper()
    sifre = input("Lütfen kullanmak istediğiniz şifreyi giriniz: ")
    bakiye = 0
    print(f"HS Hayvanat Bahçesine hoş geldiniz sayın {ad} {soyad}."
         +"Güncel bakiyeniz: 0 TL'dir")
    print(f"Şifreniz {sifre}'dir.\nSizi aramızda görmekten minnettarız !")
    sozluk[tc] = {}
    bilgiler = sozluk[tc]
    def bilgiEkle(ad,soyad,sifre,bakiye): 
        bilgiler["AD"] = ad
        bilgiler["SOYAD"] = soyad
        bilgiler["SIFRE"] = sifre
        bilgiler["BAKIYE"] = 0

    bilgiEkle(ad,soyad,sifre)
