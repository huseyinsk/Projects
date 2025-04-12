import Database as db, LogFunctions as log, ExtraPackages as ep, Gifts2Loyalties as gl, Analysis as an , Packages as pk,time

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
      +"6. Sistemdeki bilgilerimi öğren\n7. Paket Al(Yeni üyeler için)\n8. Paketimi Güncelle\n9. Kaydımı Sildir\n10. Çıkış Yap")
islem = input("Yukarıdaki menüden yapmak istediğiniz işlemi, numarası ile seçiniz: ")
while islem not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    print("Lütfen geçerli bir işlem seçiniz.")
    islem = input("Yukarıdaki menüden yapmak istediğiniz işlemi, numarası ile seçiniz: ")

if islem == "1":
    an.analysis()

elif islem == "2":
    an.analysis()
    an.suggestion()

elif islem == "3":
    exType = input("Ek paket türünü, numara olarak seçiniz (1. Tam Paketler/2. Parçalı Paketler): ").lower()
    while exType != "1" and exType != "2":
        print("Lütfen geçerli bir işlem seçiniz.")
        exType = input("Ek paket türünü, numara olarak seçiniz (1. Tam Paketler/2. Parçalı Paketler): ").lower()
    if exType == "1":
        ep.extraFullPackages()
    else:
        ep.extraPackages()

elif islem == "4":
    gl.lpCounter()

elif islem == "5":
    print("1. Iron\n2. Bronze\n3. Silver\n4. Gold\n5. Platinum\n6. Diamond\n7. Vip")
    packageType = input("Paket türünüzü, numarası ile giriniz: ")
    while packageType not in ["1","2","3","4","5","6","7"]:
        print("Lütfen geçerli bir işlem seçiniz.")
        packageType = input("Paket türünüzü, numarası ile giriniz: ")
    if packageType == "1":
        pk.iron()
    elif packageType == "2":
        pk.bronze()
    elif packageType == "3":
        pk.silver()
    elif packageType == "4":
        pk.gold()
    elif packageType == "5":
        pk.platinum()
    elif packageType == "6":
        pk.diamond()
    else:
        pk.vip()
    pk.packageDetails(pk.dakika, pk.internet, pk.sms, pk.sosyalMedya, pk.fiyat) 

elif islem == "6":
    db.display_user(ad, soyad, tc)

elif islem == "7":
    print("Paket al menüsü başlatılıyor...")
    paket_map = {
        "1": "Iron",
        "2": "Bronze",
        "3": "Silver",
        "4": "Gold",
        "5": "Platinum",
        "6": "Diamond",
        "7": "Vip"
    }
    
    print("1. Iron\n2. Bronze\n3. Silver\n4. Gold\n5. Platinum\n6. Diamond\n7. Vip")
    packageType = input("Paket türünüzü, numarası ile giriniz: ")
    while packageType not in paket_map:
        print("Lütfen geçerli bir işlem seçiniz.")
        packageType = input("Paket türünüzü, numarası ile giriniz: ")
    
    paketAdi = paket_map[packageType]
    current_package = db.get_user_package(ad, soyad, tc)
    
    if current_package:
        print(f"Zaten '{current_package}' paketine sahipsiniz. Paket değişikliği için 'Paketimi Güncelle' seçeneğini kullanabilirsiniz.")
    else:
        print(f"{paketAdi} paketi seçildi, işleminiz gerçekleştiriliyor...")
        if db.add_package_to_newUser(ad, soyad, tc, numara, paketAdi):
            print(f"{paketAdi} paketini başarıyla satın aldınız.")

elif islem == "8":
    print("Paket güncelleme menüsü başlatılıyor...")
    paket_map = {
        "1": "Iron",
        "2": "Bronze",
        "3": "Silver",
        "4": "Gold",
        "5": "Platinum",
        "6": "Diamond",
        "7": "Vip"
    }
    
    print("1. Iron\n2. Bronze\n3. Silver\n4. Gold\n5. Platinum\n6. Diamond\n7. Vip")
    packageType = input("Yeni paket türünüzü, numarası ile giriniz: ")
    while packageType not in paket_map:
        print("Lütfen geçerli bir işlem seçiniz.")
        packageType = input("Yeni paket türünüzü, numarası ile giriniz: ")
    
    yeniPaket = paket_map[packageType]
    current_package = db.get_user_package(ad, soyad, tc)
    
    if not current_package:
        print("Henüz bir paketiniz bulunmamaktadır. Yeni paket almak için 'Paket Al' seçeneğini kullanabilirsiniz.")
    else:
        print(f"Paketiniz '{current_package}' paketinden '{yeniPaket}' paketine güncelleniyor...")
        if db.update_package(ad, soyad, tc, numara, current_package, yeniPaket):
            print(f"Paketiniz başarıyla güncellendi.")

elif islem == "9":
    db.delete_user(ad, soyad, tc)

else:
    log.logout()

