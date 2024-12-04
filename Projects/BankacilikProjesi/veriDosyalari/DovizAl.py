# Döviz alma işlevini gören uygulama
from time import sleep

def dovizAl():
    altin = 10
    dolar = 10
    euro = 13
    print("Satın alınacak her bir döviz için kesilecek olan faiz 25/100'dür")
    print("Birim fiyatlarına göre Türk Lirası değerine sahip döviz fiyatları şu şekildedir: ")
    sleep(1.5) 
    print("Dolar: ", dolar, "\nAltın: ", altin, "\nEuro: ", euro)
    print("Almak istediğiniz döviz türünü TL fiyatına göre alıp, Miktar olarak hesabınıza yansıtılacaktır.")
    faiz = 1/4
    alinacakKur = input("Lütfen almak istediğiniz dövizi giriniz: ").lower()
    alinacakMiktar = float(input("Lütfen satın almak istediğiniz kuru TL miktarına göre giriniz: ")) 
    odenecekFaiz = alinacakMiktar * faiz    
    odenecekToplam = alinacakMiktar + odenecekFaiz

    while alinacakKur != "altın" and alinacakKur != "dolar" and alinacakKur != "euro":
        print("Yanlış döviz türü girdiniz lütfen altın,dolar,euro şeklinde giriniz.")
        alinacakKur = input("Lütfen almak istediğiniz dövizi giriniz: ").lower()
    
    if alinacakKur == "altın" :
        print("Güncel euro miktarı: ", altin)
        print("Almış olduğunuz euro adeti miktarı: ", alinacakMiktar / altin )
        print(f"Ödeyeceğiniz faiz miktarı: {odenecekFaiz} ve toplam miktar: {odenecekToplam}'dır.")
        print("İşleminiz başarıyla gerçekleşmiştir.")
    elif alinacakKur == "dolar":
        print("Güncel euro miktarı: ", dolar)
        print("Almış olduğunuz euro adeti miktarı: ", alinacakMiktar / dolar )
        print(f"Ödeyeceğiniz faiz miktarı: {odenecekFaiz} ve toplam miktar: {odenecekToplam}'dır.")
        print("İşleminiz başarıyla gerçekleşmiştir.")
    else:
        print("Güncel euro miktarı: ", euro)
        print("Almış olduğunuz euro adeti miktarı: ", alinacakMiktar / euro )
        print(f"Ödeyeceğiniz faiz miktarı: {odenecekFaiz} ve toplam miktar: {odenecekToplam}'dır.")
        print("İşleminiz başarıyla gerçekleşmiştir.")