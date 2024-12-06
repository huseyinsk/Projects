## Zar oyunu işlevi gören python uygulaması
from random import randint

"""""
    2 adet zar atılsın ve her iki zarın değeri de 6 olduğunda program dursun.
    İki zar da 6 gelene kadar kaç kez zar atıldığını bildiren programı yazınız.
"""""

def oyun(oyuncuSayac):
    sayac = 0
    boolean = True
    while boolean:
        ilkZar = randint(1,6)
        ikinciZar = randint(1,6)
        if (ilkZar == 6) and (ikinciZar == 6):
            boolean = False
        else:
            sayac += 1

    print(f"{oyuncuSayac}. oyuncu için toplam tur sayısı: ", sayac)
    return sayac

oyuncuSayisi = int(input("Kaç oyuncu olduğunu giriniz: "))
oyuncuSayac = 1

while oyuncuSayac <= oyuncuSayisi:
    oyun(oyuncuSayac) 
    oyuncuSayac += 1

