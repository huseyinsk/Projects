## Girilen sayılardan en küçüğü ve en büyüğü bulan python uygulaması

elemanSayisi = int(input("Kaç tane sayı verileceğini giriniz: "))
sayiListesi = []
sayac = 1

while sayac <= elemanSayisi:
    sayi = int(input(f"{sayac}. sayıyı giriniz: "))
    sayiListesi.append(sayi)
    sayac += 1

sayiListesi.sort()
print("Verilen sayılardan en küçük olanı: ", sayiListesi[0])
print("Verilen sayılardan en büyük olanı: ", sayiListesi[elemanSayisi-1])

