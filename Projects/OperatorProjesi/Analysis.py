# Analiz sistemi random kütüphanesi kullanılıp random sayılar üretilerek yapılmıştır.
# Kullanıcıdan alınan verilerle karşılaştırılarak kullanıcıya en uygun paketi önerir.
from random import randint
import time, Packages as pack

randomInternet = 0
randomCall = 0
randomSms = 0
randomSocialMedia = 0

def analysis():
    global randomCall
    global randomInternet
    global randomSms
    global randomSocialMedia
    print("Analiz sistemine hoş geldiniz..")
    print("iron,bronze,silver,gold,platinum,diamond,vip paketleri bulunmaktadır")
    
    package = input("Lütfen paketinizin ismini giriniz: ").lower()
    while package not in ["iron", "bronze", "silver", "gold", "platinum", "diamond", "vip"]:
        print("Lütfen geçerli bir paket ismi giriniz.")
        package = input("Lütfen paketinizin ismini giriniz: ").lower()

    print(f"{package} paketiniz için analiz yapılıyor.")
    time.sleep(1)

    if package == "iron":
        randomCall = randint(1, 250)
        randomInternet = randint(1, 3)
        randomSms = randint(1, 75)

    elif package == "bronze":
        randomCall = randint(1, 350)
        randomInternet = randint(1, 5)
        randomSms = randint(1, 100)

    elif package == "silver":
        randomCall = randint(1, 500)
        randomInternet = randint(1, 8)
        randomSms = randint(1, 120)
    
    elif package == "gold":
        randomCall = randint(1, 650)
        randomInternet = randint(1, 10)
        randomSms = randint(1, 150)
        randomSocialMedia = randint(1, 3)
    
    elif package == "platinum":
        randomCall = randint(1, 850)
        randomInternet = randint(1, 15)
        randomSms = randint(1, 175)
        randomSocialMedia = randint(1, 5)
    
    else:
        randomCall = randint(1, 1000)
        randomInternet = randint(1, 20)
        randomSms = randint(1, 200)
        randomSocialMedia = randint(1, 10)
    
    print("Kullanım analizi tamamlandı. Sonuçlar:")
    print("Dakika: ", randomCall)
    print("İnternet: ", randomInternet, " GB")
    print("SMS: ", randomSms)
    if randomSocialMedia > 0:
        print("Sosyal Medya: ", randomSocialMedia, " GB")


def suggestion():
    global randomCall
    global randomInternet
    global randomSms
    global randomSocialMedia
    if randomCall <= 250 and randomInternet <= 3 and randomSms <= 75:
        print("Kullanmanız gereken paketiniz: Iron Paketi")
        pack.iron()
        pack.packageDetails(250, 3, 75, 0, 20)
    
    elif (randomCall <= 350 and randomCall > 250) and (randomInternet <= 5 and randomInternet > 3) and (randomSms <= 100 and randomSms > 75):
        print("Kullanmanız gereken paketiniz: Bronze Paketi")
        pack.bronze()
        pack.packageDetails(350, 5, 100, 0, 30)

    elif (randomCall <= 500 and randomCall > 350) and (randomInternet <= 8 and randomInternet > 5) and (randomSms <= 120 and randomSms > 100):
        print("Kullanmanız gereken paketiniz: Silver Paketi")
        pack.silver()
        pack.packageDetails(500, 8, 120, 0, 40)
    
    elif (randomCall <= 650 and randomCall > 500) and (randomInternet <= 10 and randomInternet > 8) and (randomSms <= 150 and randomSms > 120) and (randomSocialMedia <= 3):
        print("Kullanmanız gereken paketiniz: Gold Paketi")
        pack.gold()
        pack.packageDetails(650, 10, 150, 3, 50)
    
    elif (randomCall <= 850 and randomCall > 650) and (randomInternet <= 15 and randomInternet > 10) and (randomSms <= 175 and randomSms > 150) and (randomSocialMedia <= 5 and randomSocialMedia > 3):
        print("Kullanmanız gereken paketiniz: Platinum Paketi")
        pack.platinum()
        pack.packageDetails(850, 15, 175, 5, 60)
    
    elif (randomCall <= 1000 and randomCall > 850) and (randomInternet <= 20 and randomInternet > 15) and (randomSms <= 200 and randomSms > 175) and (randomSocialMedia <= 10 and randomSocialMedia > 5):
        print("Kullanmanız gereken paketiniz: Diamond Paketi")
        pack.diamond()
        pack.packageDetails(1000, 20, 200, 10, 70)
    
    else:
        print("Kullanmanız gereken paketiniz: VIP Paketi")
        pack.vip()
        pack.packageDetails(1500, 30, 500, 20, 80)
    


    