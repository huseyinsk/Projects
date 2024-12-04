## BANKACILIK PROJESİNİN ATM işlevini uygulayan makine
import time 
from MusteriDB import *
from ParaTransfer import *
def atm():
    print("HS bankacılığı ATM'ye hoş geldiniz.")
    yanlisSayac = 0 
    while True:
        print("Lütfen bekleyiniz..")
        time.sleep(2)  ## 2 saniye bekletir
        hesapNo = input("Lütfen hesap numaranızı giriniz: ")
        sifre = input("Lütfen müşteri şifrenizi giriniz: ")
        if(hesapNo in musteri_HesapNO.keys()) and (sifre in musteri_HesapNO[hesapNo]["SIFRE"]): ## müşteri verileriyle uyuştuğu koşulu kontrol eder
            print("Giriş başarılı.. Hoş geldiniz !")
            sorgu = input("Lütfen yapmak istediğiniz işlemi 'paracek', 'parayatir','paragonder' şeklinde giriniz: ").lower()
            while (sorgu != "paracek") and (sorgu != "parayatir") and (sorgu != "paragonder"):
                print("Yanlış işlemi tuşladınız. Lütfen tekrar deneyiniz.")
                sorgu = input("Lütfen yapmak istediğiniz işlemi 'paracek', 'parayatir','paragonder' şeklinde giriniz: ").lower()
                
            if (sorgu == "paracek"):
                float(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
                print("Para çekme işlemi gerçekleşti. İyi günler dileriz.")   
                break             
            elif (sorgu == "paragonder"):
                paraTransfer()  ## para transferi fonksiyonunu getirir
                break
            else:
                float(input("Lütfen yatırmak istediğiniz miktarı giriniz: "))
                print("Para yatırma işlemi gerçekleşti. İyi günler dileriz.")
                break

        elif yanlisSayac == 3:
            print("Deneme hakkınız bitmiştir ve kartınız bloke olmuştur. Lütfen müşteri temsilcisiyle iletişime geçiniz.")
            break 

        else:
            print("Yanlış bilgi girdiniz lütfen tekrar deneyiniz !")
            yanlisSayac +=1 
            print("Kalan deneme hakkınız: ", (4 - yanlisSayac),)
            continue
