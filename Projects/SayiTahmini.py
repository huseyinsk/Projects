### Sayı tahminini kaç hamlede bulduran makine
from random import randint

ad = str(input("Oyunumuzda sizleri görmekten minnettarız,Lütfen adınızı giriniz: ")).upper()    
soyad = str(input("Soyadınızı giriniz: ")).upper()

print(f"Sayı tahmini oyunumuza hoş geldiniz {ad} {soyad}")
sayi_1 = int(input("Sayı aralığını belirlemek istediğiniz ilk sayı: "))
sayi_2 = int(input("Sayı aralığını belirlemek istediğiniz ikinci sayı: "))
sayac = 0 
kontrol = True   # while loopundaki anahtar boolean koşulumuz

if sayi_1 < sayi_2:                        # randint fonksiyonunu küçük-büyük ayırarak sorunsuz çalıştıran if bloku
    rastgeleSayi = randint(sayi_1,sayi_2)  
else:
    rastgeleSayi = randint(sayi_2,sayi_1)

while kontrol:  # oyunu oynatan döngümüz 
    tahmin = int(input("Tahmin etmek istediğiniz sayıyı giriniz: "))
    if tahmin < rastgeleSayi:   
        print("Tahmin ettiğiniz sayı rastgele sayıdan küçüktür, daha büyük sayı deneyiniz. ")
        sayac += 1
    elif tahmin == rastgeleSayi:  #Sayacı 1 arttırıp tahmin sayısı rastgele sayıya eşitse kontrolü false'a çevirip while döngüsünden çıkar
        sayac += 1
        kontrol = False
    else:
        print("Tahmin ettiğiniz sayı rastgele sayıdan büyüktür, daha küçük sayı deneyiniz. ")
        sayac += 1
     
print("Tebrik ederiz. Doğru sayıyı bildiniz")
print(f"{sayac} kere tahmin ettiniz ")
print("Oyunumuzu oynadığınız için teşekkür ederiz.")
