## Matematiksel mantık işlevlerini içeren python uygulaması

Boolean = True
while Boolean:
    p = int(input("p değerini 1 veya 0 olacak şekilde bir değer giriniz: "))
    q = int(input("q değerini 1 veya 0 olacak şekilde bir değer giriniz: "))
    if (p == 1) or (p == 0) and (q == 1) or (q == 0):
        Boolean = False
    else:
        print("Hatalı değer girdiniz. Lütfen 1 veya 0 olarak giriniz.")
        continue

def DeMorgan(x):
    if x == 1:
        return 0
    else:
        return 1

def baglacVe(p,q):
    print(f"p = {p} ve q = {q} değerleri için sonuç: ")
    if p == 0 or q == 0:
        return 0
    else:
        return 1

def baglacVeya(p,q):
    print(f"p = {p} veya q = {q} değerleri için sonuç: ")
    if p == 1 or q == 1:
        return 1
    else:
        return 0

def baglacIse(p,q):

    if p == 1 and q == 0: 
        print(f"p = {p} ise q = {q} değerleri için sonuç: 0")
        print(f"q = {q} ise p = {p} değerleri için sonuç: 1")

    elif q == 1 and p == 0: 
        print(f"p = {p} ise q = {q} değerleri için sonuç: 1")
        print(f"q = {q} ise p = {p} değerleri için sonuç: 0")

    else:
        print(f"sonuç: 1")
    
def baglacYada(p,q):
    print(f"p = {p} ya da q = {q} değerleri için sonuç: ")
    if p == q:
        return 0
    else:
        return 1

def baglacAncak(p,q):
    print(f"p = {p} Ancak ve Ancak q = {q} değerleri için sonuç: ")
    if p == q:
        return 1
    else:
        return 0



Boolean = True  # En son döngüde False olduğu için looplar tekrar çalışsın diye her loop başına True verir
while Boolean:
    sorguBaglac = input("Yapmak istediğiniz işlemi bağlaç türünden 've','veya','ise','yada','ancakveancak' olacak şekilde giriniz: ").lower()
    if (sorguBaglac != "ve") and (sorguBaglac !="veya") and (sorguBaglac != "ise") and (sorguBaglac !="yada") and (sorguBaglac != "ancakveancak"):
        print("Yanlış  bağlaç girdisi yaptınız. Lütfen 've','veya','ise','yada','ancakveancak' olacak şekilde giriniz: ")
        continue
    else:
        Boolean = False

Boolean = True
while Boolean:
    sorguDeMorgan =input("DeMorgan kullanmak ister misiniz?: ").lower()
    if (sorguDeMorgan != "evet") and (sorguDeMorgan != "hayır"):
        print("Yanlış cevap verdiniz, Lütfen 'evet' veya 'hayır' olarak cevap veriniz !")
        continue
    else:
        Boolean = False

if sorguDeMorgan == "evet":
    Boolean = True
    while Boolean:
        sorguHarf = input("DeMorgan uygulamak istediğiniz harfi giriniz: ")
        if (sorguHarf != "p") and (sorguHarf != "q"):
            print("Yanlış cevap verdiniz, Lütfen 'p' veya 'q' olarak cevap veriniz !")
            continue
        else:
            if sorguHarf == "p":
                p = DeMorgan(p)
                break
            else:
                q = DeMorgan(q)
                break
else:
    pass

if sorguBaglac == "ve":
    print(baglacVe(p,q))

elif(sorguBaglac == "veya"):
    print(baglacVeya(p,q))
    
elif(sorguBaglac == "ise"):
    baglacIse(p,q)

elif(sorguBaglac == "yada"):
    print(baglacYada(p,q))

else:
    print(baglacAncak(p,q))