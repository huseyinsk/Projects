## Market uygulaması işlevi gören python dosyası

elma = 5
armut = 5
domates = 10
salatalik = 10
kiwi = 15
marul = 20
ananas = 20


print("Marketimize hoş geldiniz !")
toplam = 0
while True:
    meyve = input("Almak istediğiniz meyveyi giriniz :").lower()
    while meyve not in ["elma","armut","domates","salatalik","kiwi","marul","ananas"]:
        print("Yanlış meyve girdiniz, Lütfen(elma/armut/domates/salatalik/kiwi/marul/ananas) olacak şekilde giriniz: ")
        meyve = input("Almak istediğiniz meyveyi giriniz :").lower()

    if meyve == "elma":
        toplam += elma
        print("Elmanın adet değeri: ", elma, " TL")
    elif meyve == "armut":
        toplam += armut
        print("Armutun adet değeri: ", armut, " TL")
    elif meyve == "domates":
        toplam += domates
        print("Domatesin adet değeri: ", domates, " TL")
    elif meyve == "salatalik":
        toplam += salatalik
        print("Salatalığın adet değeri: ", salatalik, " TL")
    elif meyve == "kiwi":
        toplam += kiwi
        print("Kiwinin adet değeri: ", kiwi, " TL")
    elif meyve == "marul":
        toplam += marul
        print("Marulun adet değeri: ", marul, " TL")
    else:
        toplam += ananas
        print("Ananasın adet değeri: ", ananas ," TL")

    baskaMeyveSorgu = input("Başka meyve almak ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
    while baskaMeyveSorgu not in ["evet","hayır"]:
        print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
        baskaMeyveSorgu = input("Başka meyve almak ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
    if baskaMeyveSorgu == "evet":
        continue
    else:
        print(f"Ödemeniz gereken toplam tutar: {toplam}")
        print("İyi günler dileriz !") 
        break

