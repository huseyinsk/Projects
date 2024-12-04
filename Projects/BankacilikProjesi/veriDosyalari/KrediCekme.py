# Kredi çekme işlevini gören uygulama
import time
from veriDosyalari.Sozlesme import sozlesme

def krediCekme():
    print("Bankamızda stabil 12 ay taksit bulunmaktadır.\nFaiz ise çektiğiniz kredinizin %30'u dur.")
    print("Yani 100.000TL kredi çekecek iseniz 12 ay taksitle 130.000TL ödeyeceksiniz.")
    time.sleep(1)
    cekimTalebi = float(input("Lütfen çekmek istediğiniz kredi miktarını giriniz: "))
    faiz = 30/100
    odenenMiktar = cekimTalebi * faiz
    geriOdenenMiktar = cekimTalebi + faiz
    print(f"İstediğiniz miktara bağlı ödeyeceğiniz faiz miktarı: {odenenMiktar} ve ödeyeceğiniz toplam miktar: {geriOdenenMiktar}'dır.")
    krediSorgu = input("Verilen tutarı ve anlaşmayı kabul ediyor musunuz ?: ").lower()
    while (krediSorgu != "evet") and (krediSorgu != "hayır"):
        print("Yanlış cevap verdiniz, lütfen evet veya hayır olarak giriniz.")
        krediSorgu = input("Verilen tutarı ve anlaşmayı kabul ediyor musunuz ?: ").lower()
    else:
        if krediSorgu == "evet":
            print("Lütfen sözleşmeyi imzalayınız.")
            sozlesme()
        else:
            print("Kredi çekim talebi reddedilmiştir. İyi günler dileriz !")