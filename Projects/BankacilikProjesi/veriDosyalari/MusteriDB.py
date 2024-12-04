from random import randint
# Müşteri verilerini barındıran uygulama
musteri_HesapNO = {"1235":{"AD":"HÜSEYİN","SOYAD":"SARIKAYA","SIFRE":"12sadf0","IBAN":"TR123450","BAKİYE": 10000},  # hesapno : müşteriVerileri
                   "2341":{"AD":"SERPİL","SOYAD":"ASLAN","SIFRE":"123asdf","IBAN":"TR213321","BAKİYE": 150000},
                   "3214":{"AD":"MAHMUT","SOYAD":"AYTAN","SIFRE":"324dsas","IBAN":"TR312442","BAKİYE": 1000},
                   "4234":{"AD":"YAHYA","SOYAD":"ÖZDAMAR","SIFRE":"131asf3","IBAN":"TR412312","BAKİYE": 2500}}
musteri_Iban =    {"TR123450":"1235",   #iban : hesapNO
                   "TR213321":"2341",
                   "TR312442":"3214",
                   "TR412312":"4234"}


def yeniMusteri():    ## Yeni müşteri ekleyen parametresiz fonksiyon
    ad = input("Lütfen adını giriniz: ").upper()
    soyad = input("Lütfen Soyadını giriniz: ").upper()
    sifre = input("Lütfen kullanmak istediğiniz şifreyi giriniz: ")
    m_bakiye = 0
    m_hesapNo = str(randint(1000,5000))
    m_iban = "TR" + str(randint(100000,500000))
    
    print(f"HS Bankacılığa hoş geldiniz sayın {ad} {soyad}.")
    print(f"Hesap numaranız: {m_hesapNo} ve Iban bilginiz: {m_iban}'dır.\nSizi aramızda görmekten minnettarız !")
    musteri_HesapNO[m_hesapNo] = {}

    bilgiler = musteri_HesapNO[m_hesapNo]
    def bilgiEkle(ad,soyad,sifre,m_iban,m_bakiye): ## HesapNO-Bilgi sözlüğüne ekleyen fonksiyon
        bilgiler["AD"] = ad
        bilgiler["SOYAD"] = soyad
        bilgiler["SIFRE"] = sifre
        bilgiler["IBAN"] = m_iban
        bilgiler["BAKİYE"] = m_bakiye
    def bilgi_Ekle(m_iban,m_hesapNo):   ## İban - HesapNO sözlüğüne ekleyen fonksiyon
        musteri_Iban[m_iban] = m_hesapNo

    bilgiEkle(ad,soyad,sifre,m_iban,m_bakiye)
    bilgi_Ekle(m_iban,m_hesapNo)
