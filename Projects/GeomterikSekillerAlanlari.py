## Geometrik şekillerin alanlarını bulan python uygulaması
from math import pi

def kare():
    kenar = int(input("Kenarı giriniz: "))
    print("Karenin alanı: ", kenar**2)

def dikdortgen():
    kisaKenar = int(input("Kısa kenarı giriniz: "))
    uzunKenar = int(input("Uzun kenarı giriniz: "))
    alan = kisaKenar * uzunKenar
    print("Dikdörtgenin alanı: ", alan)

def yamuk():
    altTaban = int(input("Alt tabanı giriniz: "))
    üstTaban = int(input("Üst tabanı giriniz: "))
    yukseklik = int(input("yükseklik giriniz: "))
    alan = (altTaban+üstTaban)*yukseklik / 2
    print("Yamuğun alanı: ", alan)

def paralelKenar():
    tabanKenari = int(input("Tabanı giriniz: "))
    yukseklik = int(input("yükseklik giriniz: "))
    alan = tabanKenari*yukseklik
    print("Paralelkenarın alanı: ", alan)

def kup():
    kenar = int(input("Bir kenar giriniz: "))
    alan = 6*(kenar**2)
    print("Küpün alanı: ", alan)

def eskenarUcgenPrizma():
    kenar = int(input("Kenarı giriniz: "))
    yukseklik = int(input("yükseklik giriniz: "))
    alan = (((kenar**2)*(3**1/2))/2) + (3*kenar*yukseklik)
    print("Eşkenar üçgen prizmanın alanı: ", alan)

def dikUcgenPrizma():
    dikKenar_1 = int(input("1. Dik kenarı giriniz: "))
    dikKenar_2 = int(input("2. Dik kenarı giriniz: "))
    hipotenus = int(input("Hipotenüsü giriniz: "))
    yukseklik = int(input("yükseklik giriniz: "))
    alan = (dikKenar_1*dikKenar_2) + (dikKenar_1 + dikKenar_2 + hipotenus) * yukseklik
    print("Dik üçgen prizmanın alanı: ", alan)

def silindir():
    yaricap = int(input("Yarıçapı giriniz: "))
    yukseklik = int(input("Yükseklik giriniz: "))
    pi = pi()
    alan = (2*pi*yaricap*yukseklik) + (2*pi*(yaricap**2))
    print("Eşkenar üçgen prizmanın alanı: ", alan)

sorgu = input("Alanını bulmak istediğiniz geometrik şekli giriniz: ").lower()
while sorgu not in ["kare","dikdortgen","yamuk","paralelkenar","kup","eskenarucgenprizma","dikucgenprizma","silindi"]:
    print("Yanlış geometrik şekil girdiniz !")
    sorgu = input("Alanını bulmak istediğiniz geometrik şekli giriniz: ").lower()

if sorgu == "kare":
    kare()
elif sorgu == "dikdortgen":
    dikdortgen()
elif sorgu == "yamuk":
    yamuk()
elif sorgu == "paralelkenar":
    paralelKenar()
elif sorgu == "kup":
    kup()
elif sorgu == "eskenarucgenprizma":
    eskenarUcgenPrizma()
elif sorgu == "dikucgenprizma":
    dikUcgenPrizma()
else:
    silindir()
