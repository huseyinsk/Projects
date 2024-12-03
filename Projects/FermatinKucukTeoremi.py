## Fermatın küçük teoremini ele alan python uygulaması

print("Üslü sayıların belli sayılar ile bölümünden kalanı buldurtur."
      +"\np: asal sayı, a: üslü sayıların toplamı için a ile p aralarında asal ise: a^(p-1) = 1 (mod p)'dir.")
        
kume_a = []
kume_bolen = []
a = int(input("Bir a sayısı giriniz: "))
bolen = int(input("Hangi sayıya bölmek istediğinizi giriniz(Asal sayı olmalıdır): "))
sayac = 2

if bolen == 2:
    pass
else:
    while bolen > sayac:
        if bolen % sayac == 0: 
            sayac = 2
            bolen = int(input("Asal olmayan bir sayı girdiniz.Lütfen bir asal sayı giriniz: "))
            continue
        else:
            sayac += 1

for i in range(2,a):  # a'nın bölenlerini kümeleyen for döngüsü
    if a % i == 0:
        kume_a.append(i)
    else:
        pass

for j in range(2,bolen):  # bölenin bölenlerini kümeleyen for döngüsü
    if bolen % i == 0:
        kume_bolen.append(i)
    else:
        pass

boolean = True
for k in range(len(kume_a)):
    k = kume_a[k]
    for l in range(len(kume_bolen)):
        l = kume_bolen[l]
        if k == l:
            boolean = False
            break

if boolean == False:
    print(f"Girmiş olduğunuz {a} tabanı ile {bolen} böleni aralarında asal olmadığı için Teorem kullanılamaz.")
else:
    print(f"Girmiş olduğunuz değerlerle Fermatın Küçük Teoremini kullanabilirsiniz.")

üslüSayi = int(input(f"Girmiş olduğunuz {a} sayısına bir üs giriniz: "))

cevap = (a ** üslüSayi) % bolen

print("Fermatın Küçük Teoremine göre girmiş olduğunuz değerlerin cevabı: ",cevap)