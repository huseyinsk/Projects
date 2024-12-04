# Kayıt olma işlevini gören uygulama
from MusteriDB import *
def kayitSorgu():
    sorgu = input("Kayıt olmak ister misiniz ?").lower()
    while (sorgu != "evet") and (sorgu != "hayır"):
        print("Lütfen evet veya hayır olarak cevaplayınız.")
        sorgu = input("Girdiğiniz bilgiler sistemimizde yok, kayıt olmak ister misiniz ?").lower()        
    
    if sorgu == "evet":
        yeniMusteri()
    
    else:
        print("İyi günler dileriz !")