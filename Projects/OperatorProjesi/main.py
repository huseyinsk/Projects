import Database as db, LogFunctions as log, ExtraPackages as ep, Gifts2Loyalties as gl, Analysis as an,time
import packageDetails as pD 

print("HS Operatörlüğüne Hoşgeldiniz! \nLütfen yapmak istediğiniz işlemi seçiniz.")
time.sleep(1)
uyeMi = input("1. Giris Yap / 2. Kayit Ol(numara ile seçiniz): ") 
while uyeMi != "1" and uyeMi != "2":
    print("Lütfen geçerli bir işlem seçiniz.")
    uyeMi = input("1. Giris Yap / 2. Kayit Ol(numara ile seçiniz): ") 

if uyeMi == "1":
    log.Login()
    time.sleep(1)
    ad = log.ad
    soyad = log.soyad
    tc = log.tc
    numara = log.numara

else:
    ad = input("Adınızı giriniz: ").lower()
    soyad = input("Soyadınızı giriniz: ").lower()
    tc = input("TC kimlik numaranızı giriniz: ")
    while len(tc) != 11 or tc[0] == "0":
        print("Lütfen 11 haneli bir TC kimlik numarası(başında 0 olmadan) giriniz.")
        tc = input("TC kimlik numaranızı giriniz: ")
    numara = input("Lütfen sahip olmak istediğiniz 11 haneli bir telefon numarası giriniz.(0536XXXXXXX şeklinde olmalıdır): ")
    while len(numara) != 11 or numara[0] != "0" or numara[1] != "5" or numara[2] != "3" or numara[3] != "6":
        print("Hatalı bir telefon numarası girdiniz! ")
        numara = input("Lütfen sahip olmak istediğiniz 11 haneli bir telefon numarası giriniz.(0536XXXXXXX şeklinde olmalıdır): ")
    log.check_phone_exists(numara)
    log.register(ad, soyad, tc, numara)
    time.sleep(1)
    log.Login()
    time.sleep(1)
    ad = log.ad
    soyad = log.soyad
    tc = log.tc
    numara = log.numara

print("1. Analiz Yap\n2. Paket Önerisinde Bulun\n3. Ek Paket Al \n4. Sadakat Puanımı Kontrol Et\n5. Paket Detaylarımı Öğren\n"
      +"6. Bakiye Yükle\n7. Paket Al(Yeni üyeler için)\n8. Kaydımı Sildir\n9. Çıkış Yap")
islem = input("Yukarıdaki menüden yapmak istediğiniz işlemi, numarası ile seçiniz: ")
while islem not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    print("Lütfen geçerli bir işlem seçiniz.")
    islem = input("Yukarıdaki menüden yapmak istediğiniz işlemi, numarası ile seçiniz: ")

if islem == "1":
    an.analysis(tc)

elif islem == "2":
    an.analysis(tc)
    an.suggestion(tc)

elif islem == "3":
    exType = input("Ek paket türünü, numara olarak seçiniz (1. Tam Paketler/2. Parçalı Paketler): ").lower()
    while exType != "1" and exType != "2":
        print("Lütfen geçerli bir işlem seçiniz.")
        exType = input("Ek paket türünü, numara olarak seçiniz (1. Tam Paketler/2. Parçalı Paketler): ").lower()
    if exType == "1":
        ep.extraFullPackages(tc)
    else:
        ep.extraPackages(tc)

elif islem == "4":
    gl.lpCounter()

elif islem == "5":
    pD.packageDetails(tc)

elif islem == "6":
    miktar = int(input("Eklemek istediğiniz miktarı giriniz: "))
    db.addBalance(tc,miktar)

elif islem == "7":
    print("Paket al menüsü başlatılıyor...")
    print("Paketler şöyledir: "
          +"\n1. Iron"
          +"\n2. Bronze"
          +"\n3. Silver"
          +"\n4. Gold"
          +"\n5. Platinum"
          +"\n6. Diamond"
          +"\n7. VIP")
    new_id = int(input("Lütfen paketi idsini yazacağınız şekilde giriniz:"))
    db.buyPackage(tc,new_id)

elif islem == "8":
    db.deleteUser(tc)

else:
    log.logout()

