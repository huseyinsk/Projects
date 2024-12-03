## Bağıntılar konusunu ele alan python programı 
from random import choice

elemanSayisi = int(input("Kümenin kaç elemanlı olacağını giriniz: "))
sayac = 0 
kume = []
ab_Kume = []
while elemanSayisi > sayac:
    sayac += 1
    eklenenEleman = int(input(f"Eklemek istediğiniz {sayac}. elemanı giriniz: "))
    kume.append(eklenenEleman)

kumeSayisi = int(input("Kontrol etmek istediğiniz küme kaç elemanlı olacak ?: "))
for i in range(kumeSayisi):
    a = choice(kume)
    b = choice(kume)
    ab_Kume.append((a,b))

def yansima(): #(a,a) olmalı
    boolean = True
    for j in range(len(kume)):
        kume_elemani = kume[j]
        if (kume_elemani,kume_elemani) not in ab_Kume:
            print(f"({kume_elemani},{kume_elemani}) elemanı, {ab_Kume} kümesinde olmadığından yansima özelliği yoktur")
            boolean = False
            return False
    if boolean:
        print(ab_Kume)
        print("Yansıma özelliği vardır")
        return True

def simetri(): # (x,y) varsa (y,x) olmalı
    boolean = True
    for j in range(len(ab_Kume)):
        ilkEleman = ab_Kume[j][0]
        ikinciEleman = ab_Kume[j][1]
        if (ikinciEleman,ilkEleman) not in ab_Kume:
            print(f"(({ilkEleman},{ikinciEleman}) için {ikinciEleman},{ilkEleman}) elemanı, {ab_Kume} kümesinde olmadığından simetri özelliği yoktur")
            boolean = False
            return False
    if boolean:
        print(ab_Kume)
        print("Simetri özelliği vardır")
        return True
    
def tersSimetri(): # (x,y) varsa (y,x) olmamalı
    boolean = True
    for k in range(len(ab_Kume)):
        ilkEleman = ab_Kume[k][0]
        ikinciEleman = ab_Kume[k][1]
        if (ikinciEleman,ilkEleman) in ab_Kume:
            print(f"(({ilkEleman},{ikinciEleman}) için {ikinciEleman},{ilkEleman}) elemanı, {ab_Kume} kümesinde olduğundan ters simetri özelliği yoktur")
            boolean = False
            return False

    if boolean:
        print(ab_Kume)
        print("Ters simetri özelliği vardır")
        return True

def gecisme(): # (a,b) ve (b,c) varsa (a,c) olmalı
    boolean = True
    for j in range(len(ab_Kume)):
        for k in range(len(ab_Kume)):
            ilkEleman = ab_Kume[j][0]
            ikinciEleman = ab_Kume[j][1]
            ikinci_ilkEleman = ab_Kume[k][0]
            ikinci_ikinciEleman = ab_Kume[k][1]
            if (ikinciEleman == ikinci_ilkEleman) and (ilkEleman,ikinci_ikinciEleman) not in ab_Kume:
               print(f"({ilkEleman},{ikinciEleman}) ve ({ikinci_ilkEleman},{ikinci_ikinciEleman}) bulunmakta ancak ({ilkEleman},{ikinci_ikinciEleman}) yoktur."
                     +"\nBu sebeple geçişme özelliği yoktur")
               boolean = False
               return False
    if boolean:
        print(ab_Kume)
        print("Geçişme özelliği vardır")
        return True

def denklikBagintisi(): # yansıma, simetri, geçişme varsa
    checking = [yansima(),simetri(),gecisme()]
    for i in checking:
        i
    if all(checking):
        print("Bir Denklik bağıntısıdır.")
    else:
        print("Bir Denklik bağıntısı değildir.")

def siralamaBagintisi(): # yansıma, ters simetri , geçişme varsa
    checking = [yansima(),tersSimetri(),gecisme()]
    for i in checking:
        i
    if all(checking):
        print("Bir Denklik bağıntısıdır.")
    else:
        print("Bir Denklik bağıntısı değildir.")

BagintiTuru = input("Kontrol etmek istediğiniz bağıntı türünü 'denklik','siralama' şekilde giriniz: ").lower()
while (BagintiTuru != "denklik") and (BagintiTuru != "siralama"):
    print("Yanlış bir bağıntı türü girdiniz! ")
    BagintiTuru = input("Kontrol etmek istediğiniz bağıntı türünü 'denklik','siralama' şekilde giriniz: ").lower()

if BagintiTuru == "denklik":
    denklikBagintisi()
else:
    siralamaBagintisi()


