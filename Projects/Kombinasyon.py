## Kombinasyon işlevi gören python uygulaması
import time

print("Kombinasyon işlemi 'C(n,r) = (n!)/(n-r)! * r!' şeklinde gösterilir."
      +"\nVe n tane şeyden r tanesini kaç farklı şekilde seçileceğini belirlemek için kullanılır."
      +"\nProgram başlıyor..")
time.sleep(1.5)

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

n = int(input("Lütfen n olarak atamak istediğiniz ana kaynak adetini giriniz: "))
r = int(input("Lütfen r olarak atamak istediğiniz farklı seçim adetini giriniz: "))

sonuc = kombinasyon(n,r)
print(f"Vermiş olduğunuz verilere göre {sonuc} farklı şekilde seçim yapılabilir.")
