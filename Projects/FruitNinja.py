## Fruit Ninja oyunu işlevini gören sanal python uygulaması
from random import choice
from time import time,sleep

baslangicZamani = time()
objeler = ["karpuz","elma","muz","kivi","ananas","bomba"]
puan = 0
boolean = False
while (time() - baslangicZamani) <= 30:  #20 saniye boyunca
    rastgeleObje = choice(objeler)
    print(f"Ekrana gelen obje :{rastgeleObje}")
    bicak = input("Kesmek ister misiniz(evet/hayır olarak giriniz) ?: ").lower()
    while bicak not in ["evet","hayır"]:
        print("Yanlış cevap verdiniz !")
        bicak = input("Kesmek ister misini? (evet/hayır) olarak cevap veriniz: ").lower()

    if bicak == "evet":
        if rastgeleObje == "bomba":
            print("Bombayı patlattınız !"
            +f"\nOyunu kaybettiniz.Toplamış olduğunuz puan: {puan}")
            break
        else:
            if rastgeleObje == "karpuz":
                puan += 10
            elif rastgeleObje == "elma":
                puan += 5
            elif rastgeleObje == "muz":
                puan += 7
            elif rastgeleObje == "kivi":
                puan += 12
            else:
                puan += 15
    elif (time()- baslangicZamani) == 30:
        boolean = True
    else:
        if rastgeleObje =="bomba":# bomba gelince patlatmama durumu
            puan += 15
        else:
            print(f"Verilen {rastgeleObje} meyvesini kesmediğiniz için oyunu kaybettiniz"
            +f"\nToplam puanınız: {puan}")


if boolean == True:
    print("Oyunu kazandınız. Tebrik ederiz"
    +f"\nToplam puanınız: {puan}.")







