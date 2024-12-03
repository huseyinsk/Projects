## Modüler aritmetik işlevini gören python uygulaması

print("Mod(Modül) kendini tekrar eden sayıdır, Mod min 2 ve pozitif olmalıdır")
print("Örnek bir soru '143 = x (mod 5) ise x en az 3'tür ve sonsuzdur !")

mod = int(input("Girmek istediğiniz modul değerini yazınız: "))
sayi = int(input("Girmek istediğiniz sayıyı yazınız: "))
sayac = 0

if sayi < 0 :
    while sayi < 0:
        sayi += mod
    print(f"Vermiş olduğunuz {sayi} sayısı ve {mod} moduna göre x'in en az pozitif tam sayı değeri: ", sayi)

else:
    kalan = sayi % mod
    print(f"Vermiş olduğunuz {sayi} sayısı ve {mod} moduna göre x'in en az pozitif tam sayı değeri: ", kalan)
        


