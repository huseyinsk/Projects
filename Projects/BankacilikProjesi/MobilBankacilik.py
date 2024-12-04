# Mobil bankacılık uygulaması işlevini gören uygulama 
from Giris import giris
from KayitSorgu import kayitSorgu
from Yapilmakİstenen import yapilmakIstenen
import time


print("HS bankacılığa hoş geldiniz.")
soru = str(input("Bankamızın bir üyesi misiniz ? : ")).lower()
while soru != "evet" and soru != "hayır":
    print("Lütfen üyeyseniz evet veya değilseniz hayır yazınız.")
    soru = str(input("Bankamızın bir üyesi misiniz ? : ")).lower()
    
if soru == "evet" :
    giris()

else:
    kayitSorgu()

yapilmakIstenen()

