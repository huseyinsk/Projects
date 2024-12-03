## Verilen bir sayının asal olup olmadıgını kontrol eden program

sayi = int(input("Kontrol etmek istediğiniz sayıyı giriniz: "))
if sayi < 0:
    print("Lütfen pozitif doğal sayı giriniz.")

elif sayi == 2:
    print("2 sayısı çift bir asal sayıdır.(Tek çift asaldır)")

elif sayi == 1: 
    print("1 sayısı asal sayı değildir.")

else:
    boolean = True
    sayac = 2
    
    while sayac < sayi:
        if sayi % sayac == 0:
            print(f"Girmiş olduğunuz {sayi} sayısı bir asal sayı değildir.")
            boolean = False
            break
        else:
            sayac += 1
    
    if boolean:
        print(f"Girmiş olduğunuz {sayi} sayısı bir asal sayıdır.")
    else:
        pass