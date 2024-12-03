### Hesap makinesi

def topla(x, y):    #Toplama işlemi yapan fonksiyon
    return x + y

def cikar(x, y):    #Çıkarma işlemi yapan fonksiyon
    return x - y

def carp(x, y):     #Çarpma işlemi yapan fonksiyon
    return x * y

def bol(x, y):      #Bölme işlemi yapan fonksiyon
    return x / y


print("İşlem Türleri: Toplama, Çıkarma, Bölme, Çarpma")
islemTuru = str(input("Yapmak istediğiniz işlemi giriniz: ")).lower()

while(islemTuru != "toplama") and (islemTuru !="çıkarma") and (islemTuru != "çarpma") and (islemTuru != "bölme"): # işlemi doğru yazana kadar tekrar eden döngü
    print("Lütfen yapılmak istenen işlemi doğru karakterize şekilde giriniz")
    islemTuru = str(input("Yapmak istediğiniz işlemi giriniz: ")).lower()

if islemTuru == "toplama":
    sayi_1 = float(input("İlk sayıyı giriniz: "))
    sayi_2 = float(input("İkinci sayıyı giriniz: "))
    print(topla(sayi_1, sayi_2))

elif islemTuru == "çıkarma":
    sayi = int(input("Ana sayıyı giriniz: "))
    sayidanCikartilan = int(input("Çıkartılacak sayıyı giriniz: "))
    print(cikar(sayi, sayidanCikartilan))

elif islemTuru == "bölme":
    bolunen = int(input("Hangi sayıyı bölmek istediğinizi giriniz: "))
    bolen = int(input("Hangi sayı ile bölmek istediğinizi giriniz: "))
    print(bol(bolunen, bolen))

else:
    sayi_1 = float(input("Çaprmak istediğiniz ilk sayıyı giriniz: "))
    sayi_2 = float(input("Çarpmak istediğiniz İkinci sayıyı giriniz: "))
    print(carp(sayi_1, sayi_2))
