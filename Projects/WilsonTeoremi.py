## Wilson teoremini işleme alan python uygulaması

print("n>1 ve n asal olmak üzere (n-1)! = -1 (mod n) veya (n-1)! = n-1 (mod n) şeklinde gösterilir.")

mod = int(input("Bir n(mod) asal sayısı giriniz: "))
sayac = 2
if mod == 2:
    pass
else:
    while mod > sayac:
        if mod % sayac == 0: 
            sayac = 2
            mod = int(input("Asal olmayan bir sayı girdiniz.Lütfen bir asal sayı giriniz: "))
            continue
        else:
            sayac += 1

bolunen = int(input("Bir faktöriyel türünden bölünen sayısı giriniz: "))
faktoriyelBolunen = 1
for i in range(1, bolunen+1): # Bölünenin faktöriyelini hesaplayan for döngüsü
    faktoriyelBolunen *= i

print(f"Vermiş olduğunuz verilere göre problem şu şekildedir: {bolunen}! = a (mod {mod})")
cevap = faktoriyelBolunen % mod
if bolunen < mod: # mod-1 den küçük bir değer verilmesi durumunda mod-1 den başlayıp bolunen sayıya kadar işlem yaptıran koşul bloku 
    if bolunen == (mod-1):
        print(f"Vermiş olduğunuz {bolunen}! = a (mod {mod}) denkleminin cevabı(a'sı): {cevap} veya -1'dir")
    else:
        print(f"Vermiş olduğunuz {bolunen}! = a (mod {mod}) denkleminin cevabı(a'sı): {cevap} veya {(cevap-mod)}")
else:
    print("Bölüneni(n-1!)'i mod(n)'den küçük girdiğiniz için Wilson Teoremini kullanamazsınız.")