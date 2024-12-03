## Saymanın Temel Prensibi konusunu ele alan python uygulaması 

print("Temeli bir olayın kaç farklı şekilde gerçekleşeceğini bulmaktır.")
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
    
def ornek1():
    print("Örnek:a çeşit sıcak çorbadan x veya b çeşit yemekten y tane yemeği kaç farklı şekilde seçeriz ?")
    a = int(input("a sayısını giriniz :"))
    b = int(input("b sayısını giriniz :"))
    x = int(input("x sayısını giriniz :"))
    y = int(input("y sayısını giriniz :"))

    cevap1 = kombinasyon(a,x)
    cevap2 = kombinasyon(b,y)
    print(f"{a} çeşit çorbadan {x} farklı {cevap1} adet seçim yapılabilir")
    print(f"{b} çeşit çorbadan {y} farklı {cevap2} adet seçim yapılabilir")

def ornek2():
    print("x öğrencinin bulunduğu sınıfta a başkan ve b yardımcı kaç farklı şekilde seçilir ? :")
    x = int(input("Bir x sayısı giriniz: "))
    a = int(input("Bir a sayısı giriniz: "))
    b = int(input("Bir b sayısı giriniz: "))

    cevap1 = kombinasyon(x,a)
    cevap2 = kombinasyon((x-1),b)
    print(f"{x} öğrencinin bulunduğu sınıftan {cevap1} adet başkan seçilebilir")
    print(f"{x} öğrencinin bulunduğu sınıftan {cevap2} adet yardımcı seçilebilir")

def ornek3():
    print("A - B - C konumlarında bulunan lokasyonlara göre A dan B ye x ; A dan C ye y tane ; B den C ye z tane yol vardır.")
    print("A'dan C'ye, B'ye uğramak şartı ile kaç farklı şekilde gidilir ?"
          "\nA'dan C'ye, B'ye uğramak şartı ile kaç farklı şekilde gidilip geri dönülür ?")
    x = int(input("x sayısını giriniz :"))
    y = int(input("y sayısını giriniz :"))
    z = int(input("z sayısını giriniz :"))    
    
    cevap1 = kombinasyon(x,1) * kombinasyon(z,1)
    cevap2 = (kombinasyon(x,1) * kombinasyon(z,1) * kombinasyon(z,1) * kombinasyon(x,1))
    print(f"Soru1: A'dan B'ye {x} yol ve B'den C'ye {z} yol vardır ve cevabı: {cevap1}")
    print(f"Soru1: A'dan B'ye {x} yol ve B'den C'ye {z} yol vardır, Dönüşte de yine aynı yollar kullanılacaktır.: {cevap2}")

ornekSorgu = input("Çözmek istediğiniz örneği 'ornek1','ornek2','ornek3' olacak şekilde giriniz: ").lower()
while ornekSorgu not in ["ornek1","ornek2","ornek3"]:
    print("Yanlış örnek türü girdiniz !")
    ornekSorgu = input("Çözmek istediğiniz örneği 'ornek1','ornek2','ornek3' olacak şekilde giriniz: ").lower()

if ornekSorgu == "ornek1":
    ornek1()
elif ornekSorgu == "ornek2":
    ornek2()
else:
    ornek3()
