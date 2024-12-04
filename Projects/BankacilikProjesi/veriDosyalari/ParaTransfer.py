from veriDosyalari.MusteriDB import * 
import time

# Para Transferi işlevini gören uygulama 
def paraTransfer():
    gonderimTuru = input("Hangi gönderim türüyle işlem yapmak istersiniz, Iban mı yoksa HesapNo mu ? : ").lower()
    while (gonderimTuru != "iban") and (gonderimTuru != "hesapno"):
        print("Yanlış seçim yaptınız, Lütfen iban veya hesapno'yu seçiniz.")
        gonderimTuru = input("Hangi gönderim türüyle işlem yapmak istersiniz, Iban mı yoksa HesapNo mu ? : ").lower()
        
    if(gonderimTuru == "iban"):
        iban_gonderme = input("Lütfen göndereceğiniz kişinin Iban numarasını giriniz: ")
        ad_gonderme = input("Lütfen göndereceğiniz kişinin adını giriniz: ")
        soyad_gonderme = input("Lütfen göndereceğiniz kişinin soyadını giriniz: ")
        gonderilen_miktar = int(input("Göndermek istediğiniz miktar: "))
        gonderen_hesapNo = input("Lütfen HesapNo'nuzu giriniz: ")

        if (gonderilen_miktar) > (musteri_HesapNO[gonderen_hesapNo]["BAKİYE"]):
            print("Maalesef işlemi gerçekleştiremedik.\nYetersiz Bakiye\nLütfen tekrar deneyiniz.")
            paraTransfer()

        elif (iban_gonderme in musteri_Iban.keys()) and (ad_gonderme in musteri_HesapNO[musteri_Iban[iban_gonderme]]["AD"]) and (soyad_gonderme in musteri_HesapNO[musteri_Iban[iban_gonderme]]["SOYAD"]) and (gonderen_hesapNo in musteri_HesapNO.keys()): ## müşteri verileriyle uyuştuğu koşulu kontrol eder
            musteri_HesapNO[musteri_Iban[iban_gonderme]]["BAKİYE"] = musteri_HesapNO[musteri_Iban[iban_gonderme]]["BAKİYE"] + gonderilen_miktar   ## Gönderilen kişinin yeni bakiyesi
            musteri_HesapNO[gonderen_hesapNo]["BAKİYE"] = musteri_HesapNO[gonderen_hesapNo]["BAKİYE"] - gonderilen_miktar  ## Gönderen kişinin yeni bakiyesi 
            print("Tebrikler işlem başarılı.. \nGüncel bakiyeniz: ", musteri_HesapNO[gonderen_hesapNo]["BAKİYE"] )
            print("İyi günler dileriz")
        
        else:
            print("Hatalı bilgi girdiniz lütfen tekrar deneyiniz.")
            paraTransfer()
            
    elif(gonderimTuru == "hesapno"):
        hesapno_gonderme = input("Lütfen göndereceğiniz kişinin HesapNO'sunu giriniz: ")
        ad_gonderme = input("Lütfen göndereceğiniz kişinin adını giriniz: ")
        soyad_gonderme = input("Lütfen göndereceğiniz kişinin soyadını giriniz: ")
        gonderilen_miktar = int(input("Göndermek istediğiniz miktar: "))
        gonderen_hesapNo = input("Lütfen HesapNo'nuzu giriniz: ")
        
        if (gonderilen_miktar) > (musteri_HesapNO[gonderen_hesapNo]["BAKİYE"]):
            print("Maalesef işlemi gerçekleştiremedik.\nYetersiz Bakiye\nLütfen tekrar deneyiniz.")
            paraTransfer()

        elif (hesapno_gonderme in musteri_HesapNO.keys()) and (ad_gonderme in musteri_HesapNO[hesapno_gonderme]["AD"]) and (soyad_gonderme in musteri_HesapNO[hesapno_gonderme]["SOYAD"]) and (gonderen_hesapNo in musteri_HesapNO.keys()): ## müşteri verileriyle uyuştuğu koşulu kontrol eder
            musteri_HesapNO[hesapno_gonderme]["BAKİYE"] = musteri_HesapNO[hesapno_gonderme]["BAKİYE"] + gonderilen_miktar ## Gönderilen kişinin yeni bakiyesi
            musteri_HesapNO[gonderen_hesapNo]["BAKİYE"] = musteri_HesapNO[gonderen_hesapNo]["BAKİYE"] - gonderilen_miktar ## Gönderen kişinin yeni bakiyesi 

            print("Tebrikler işlem başarılı.. \nGüncel bakiyeniz: ", musteri_HesapNO[gonderen_hesapNo]["BAKİYE"] )
            print("İyi günler dileriz")
        else:
            print("Hatalı bilgi girdiniz lütfen tekrar deneyiniz.")
            paraTransfer()

    else:
        print("Hatalı bilgi girdiniz lütfen tekrar deneyiniz.")
        paraTransfer()