## Çark işlevi gören python uygulaması
from time import time,sleep
from random import choice

elemanSayisi = int(input("Çarkınıza eklemek istediğiniz nesne sayısını giriniz: "))
cark = []
for i in range(elemanSayisi):
    eklenenEleman = input("Lütfen eklemek istediğiniz nesneyi giriniz: ").lower()
    cark.append(eklenenEleman)

print(f"Çarkınız şöyledir: {cark}")
sorgu = input("Döndürmek ister misiniz ?(evet/hayır olarak cevap veriniz): ").lower()

while sorgu not in ["evet","hayır"]:
    print("Yanlış başlama komutu verdiniz. Lütfen tekrar deneyiniz !")
    sorgu = input("Döndürmek ister misiniz ?(evet/hayır olarak cevap veriniz): ").lower()

if sorgu == "evet":
    print("Çark çeviriliyor...")
    for j in cark:
        print(j, end =" ")
    rastgeleSecim = choice(cark)
    print(f"\nKazanan nesne: {rastgeleSecim}, tebrik ederiz !")
else:
    print("Çark çevirme işlemi iptal edilmiştir.")

