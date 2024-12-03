## Dışarıdan girilen veri ile bazı küme sorularını çözümleyen kombinasyon programı

def kombinasyon(n,r):
    sayac_n = 1
    sayac_r = 1
    sayac_nr = 1
    for i in range(n,0,-1): # n faktöriyel bulduran for döngüsü
        sayac_n *= i
    
    for k in range(r,0,-1): # r faktöriyel bulduran for döngüsü
        sayac_r *= k
    
    for j in range((n-r),0,-1): # (n-r) faktöriyel bulduran for döngüsü
        sayac_nr *= j
     
    C = (sayac_n) / ((sayac_nr) * (sayac_r))
    return C

elemanSayisi = int(input("Kümenizde bulunmasını istediğiniz eleman sayısını giriniz: "))
eklemeSayac = 0 
kume = []
while eklemeSayac < elemanSayisi:
    eklemeSayac += 1
    kumeEkleme = input(f"Lütfen kümenize eklemek istediğiniz {eklemeSayac}. değeri giriniz: ") # harf ve sayı alabileceği için str değerinde
    kume.append(kumeEkleme)

x = int(input("En çok x elemanlı alt küme sayısı için bir 'x' değeri giriniz: ")) # Soru 1
cevap = 0

for i in range(x+1):
    islem = kombinasyon(elemanSayisi,i)
    cevap += islem
print(f"Kümenizde en çok {x} elemanlı alt küme sayısı C({elemanSayisi},{x}) ile  bulunur ve cevabı: ", cevap)

cevap = 0
y = int(input("En az y elemanlı alt küme sayısı için bir 'y' değeri giriniz: "))  # Soru 2
for j in range(x,elemanSayisi+1):
    islem = kombinasyon(elemanSayisi,j)
    cevap += islem
print(f"Sorunun cevabı: ", cevap)

kumenin_ilk_harfi = kume[0]
z = int(input("z elemanlı alt kümenin kaçında " + kume[0] +  " bulunmadığı alt küme sayısı için bir z değeri giriniz: "))
cevap = kombinasyon((elemanSayisi-1),z)
print(f"Sorunun cevabı: ", cevap)

a = int(input("a elemanlı alt kümenin kaçında " + kume[0] +  " bulunur " + kume[1] + " bulunmaz için için bir a değeri giriniz: "))
cevap = kombinasyon((elemanSayisi-1),a) - kombinasyon((elemanSayisi-2),a)
print(f"Sorunun cevabı C({elemanSayisi-1},{a}) - C({elemanSayisi-2},{a}) ile  bulunur ve cevabı: ", cevap)

b = int(input("a elemanlı alt kümenin kaçında " + kume[0] +  " ve " + kume[1] + " bulunur için için bir b değeri giriniz: "))
cevap = kombinasyon((elemanSayisi-2),b)
print(f"Sorunun cevabı C({elemanSayisi-2},{b}) ile  bulunur ve cevabı: ", cevap)

