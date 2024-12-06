# Hayvanları gezme başına düşen fiyatları depolayan python dosyası
from veriDosyalari.hesapDB import musteri_tcno as sozluk

maymun = 5
timsah = 10
fokBaligi = 15
yunus = 15
aslan = 20
def gezi():
    print("Bir hayvan birden fazla gezilebilir ve Gezi başına fiyatlarımız şu şekildedir: "
        +f"\nAslan: {aslan}"
        +f"\nMaymun: {maymun}"
        +f"\nTimsah: {timsah}"
        +f"\nFok Balığı: {fokBaligi}"
        +f"\nYunus: {yunus}")
    boolean = True
    ucret = 0
    while boolean:
        geziTurleri = input("Lütfen gezmek istediğiniz hayvan ismini giriniz: ").lower()
        while geziTurleri not in ["aslan","maymun","timsah","fokbaligi","yunus"]:
            print("Yanlış hayvan ismi girdiniz, Lütfen tekrar deneyiniz! ")
            geziTurleri = input("Lütfen gezmek istediğiniz hayvan ismini giriniz: ").lower()
        
        if geziTurleri == "aslan":
            ucret += 20
        elif geziTurleri == "maymun":
            ucret += 5
        elif geziTurleri == "timsah":
            ucret += 10
        else:
            ucret +=15
        
        geziBitimiSorgu = input("Başka bir hayvanı daha gezmek ister misiniz? (evet/hayır) olarak giriniz: ").lower()
        while geziBitimiSorgu not in ["evet","hayır"]:
            print("Yanlış cevap türü verdiniz, Lütfen tekrar deneyiniz!")
            geziBitimiSorgu = input("Başka bir hayvanı daha gezmek ister misiniz? (evet/hayır) olarak giriniz: ").lower()

        if geziBitimiSorgu == "hayır":
            print(f"Toplam ödemeniz gereken miktar: {ucret} TL'dir.")
            tc = int(input("Bakiye işlemi için lütfen tekrardan tc'nizi giriniz: "))
            while tc not in sozluk.keys():
                print("Sistemde kayıtlı olmayan tc girdiniz !")
                tc = int(input("Bakiye işlemi için lütfen tekrardan tc'nizi giriniz: "))

            guncelBakiye = sozluk[tc]["BAKIYE"] - ucret
            if guncelBakiye < 0:
                print("Yetersiz bakiye! Lütfen tekrar deneyiniz")
                continue
            else:
                print("Güncel bakiyeniz: ", (guncelBakiye)," TL'dir")
                break
        else:
            continue
        
