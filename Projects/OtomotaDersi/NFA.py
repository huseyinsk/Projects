# # Non-Deterministik Sonlu Özdevinir Örnekleri
alfabe = ""
boolean = False

def ornek1():
    """
    Q = {q0,q1,q2,q3} , F = {q2} , E = {a,b,λ} için
    S(q0,a)=q1, S(q1,b)=q2, S(q2,λ)=q3 ve S(q3,λ)=q0
    olan NFA'yı çiziniz
    """
    global alfabe
    global boolean
    while True:
        q0 = input("q0 için 'a' değerini giriniz: ").lower()
        while q0 != "a":
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
            q0 = input("q0 için 'a' değerini giriniz: ").lower()
        
        alfabe += q0
        print("q1'e geldiniz")
        q1 = input("q1 için b değerini giriniz: ").lower()
        while q1 != "b":
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
            q1 =input("q1 için b değerini giriniz: ").lower()
        
        alfabe += q1
        print("q2'ye geldiniz")
        while True:
            sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
            while sorgu not in ["evet","hayır"]:
                print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
                sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
            if sorgu == "evet":
                boolean = True
                print(f"Alfabeniz: {alfabe}")
                break
            else:
                print("Lambda ile q3 daha sonra lambda ile q0'a dönüldü")
                alfabe += "λλ"
                break
        if boolean:
            break

def ornek2():
    """
    Q = {q0,q1,q2} , F = {q0} , E = {0,1,λ} için
    S(q0,1)=q1, S(q1,0)=q2, S(q2,λ)=q0 ve S(q1,0)=q0
    olan NFA'yı çiziniz
    """
    global alfabe
    while True:
        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
        while sorgu not in ["evet","hayır"]:
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
        if sorgu == "evet":
            print(f"Alfabeniz: {alfabe}")
            break
        q0 = input("q0 için '1' değerini giriniz: ").lower()
        while q0 != "1":
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
            q0 = input("q0 için '1' değerini giriniz: ").lower()
        alfabe+=q0
        print("q1'e gelindi ")
        q1 = input("q1 için '0' değeri ile nereye gidileceğini (q0/q2) olarak giriniz: ").lower()
        alfabe += "0"
        while q1 not in ["q0","q2"]:
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
            q1 = input("q1 için '0' değeri ile nereye gidileceğini (q0/q2) olarak giriniz: ").lower()
        if q1 == "q0":
            continue
        else:
            print("q2'ye gelindi"
                  +"\nλ ile q0'a dönüldü")
            alfabe += "λ"
            continue

def ornek3():
    """
    Q = {q0,q1,q2,q3,q4} , F = {q4} , E = {a,b,c,λ} için
    S(q0,(a,b,c))=q0, S(q0,a)=q1, S(q1,b)=q3 ve S(q3,c)=q4
    S(q0,b)=q2, S(q2,a)=q3 
    olan NFA'yı çiziniz
    """
    global alfabe
    while True:
        q0 = input("q0 için (a/b/c) değerini giriniz: ").lower()
        while q0 not in ["a","b","c"]:
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
            q0 = input("q0 için (a/b/c) değerini giriniz: ").lower()
        alfabe += q0
        if q0 == "c":
            print("q0'a geri döndünüz ")
            continue
        elif q0 == "b":
            yonSorgu = input("b ile q0'a mı dönmek istersiniz yoksa q2'ye mi? (q0/q2) olarak giriniz: ").lower()
            while yonSorgu not in ["q0","q2"]:
                print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz!")
                yonSorgu = input("b ile q0'a mı dönmek istersiniz yoksa q2'ye mi? (q0/q2) olarak giriniz: ").lower()

            if yonSorgu =="q0":
                print("b ile q0'a dönüldü")
                continue
            else:
                print("q2'ye gelindi")
                q2 = input("q2 için a değerini giriniz: ").lower()
                while q2 not in ["a"]:
                    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                    q2 = input("q2 için a değerini giriniz: ").lower()
                alfabe+=q2
                print("q3'e gelindi")
                q3 = input("q3 için c değerini giriniz: ").lower()
                while q3 not in ["c"]:
                    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                    q3 = input("q3 için c değerini giriniz: ").lower()
                alfabe+=q3
                print("q4'e gelindi")
                print(f"Alfabeniz: {alfabe}")
                break

        else:
            yonSorgu = input("a ile q0'a mı dönmek istersiniz yoksa q1'e mi? (q0/q1) olarak giriniz: ").lower()
            while yonSorgu not in ["q0","q1"]:
                print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz!")
                yonSorgu = input("a ile q0'a mı dönmek istersiniz yoksa q1'ye mi? (q0/q2) olarak giriniz: ").lower()

            if yonSorgu =="q0":
                print("a ile q0'a dönüldü")
                continue
            else:
                print("q1'e gelindi")
                q1 = input("q1 için b değerini giriniz: ").lower()
                while q1 not in ["b"]:
                    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                    q1 = input("q1 için b değerini giriniz: ").lower()
                alfabe+=q1
                print("q3'e gelindi")
                q3 = input("q3 için c değerini giriniz: ").lower()
                while q3 not in ["c"]:
                    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                    q3 = input("q3 için c değerini giriniz: ").lower()
                alfabe+=q3
                print("q4'e gelindi")
                print(f"Alfabeniz: {alfabe}")
                break

def ornek4():
    """
    Q = {q0,q1,q2,q3} , F = {q2} , E = {0,1,λ} için
    S(q0,(0,1))=q0, S(q0,0)=q1, S(q1,0)=q2 ve S(q2,0)=q2
    S(q0,1)=q3, S(q3,1)=q2 olan ve içerisinde en az bir tane "00"
     veya "11" içeren ve tüm dizgileri tanıyan NFA'yı çiziniz
    """
    global alfabe
    global boolean
    while True:
        q0 = input("q0 için (0/1) değerini giriniz: ").lower()
        while q0 not in ["0","1"]:
            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
            q0 = input("q0 için (0/1) değerini giriniz: ").lower()
        alfabe += q0
        if q0 == "0":
            yonSorgu = input("0 ile hangi yöne gidileceğini (q0/q1) şeklinde giriniz: ").lower()
            while yonSorgu not in ["q0","q1"]:
                print("Hatalı girdi yaptınız, Tekrar deneyiniz !")
                yonSorgu = input("0 ile hangi yöne gidileceğini (q0/q1) şeklinde giriniz: ").lower()
            if yonSorgu == "q0":
                print("0 ile q0'a dönüldü !")
                continue
            else:
                print("q1'e gelindi")
                q1 = input("q1 için 0 değerini giriniz: ").lower()
                while q1 not in ["0"]:
                    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                    q1 = input("q1 için 0 değerini giriniz: ").lower()
                alfabe += q1
                print("q2'ye gelindi")
                while True:
                    sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                    while sorgu not in ["evet","hayır"]:
                        print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
                        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                    if sorgu == "evet":
                        boolean = True
                        print(f"Alfabeniz: {alfabe}")
                        break
                    else:
                        q2 = input("q2 için (0/1) değerini giriniz: ").lower()
                        while q2 not in ["0","1"]:
                            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                            q2 = input("q2 için (0/1) değerini giriniz: ").lower()
                        alfabe += q2
                        print(f"{q2} ile q2'ye dönüldü")
                        continue

        else:
            yonSorgu = input("1 ile hangi yöne gidileceğini (q0/q3) şeklinde giriniz: ").lower()
            while yonSorgu not in ["q0","q3"]:
                print("Hatalı girdi yaptınız, Tekrar deneyiniz !")
                yonSorgu = input("0 ile hangi yöne gidileceğini (q0/q3) şeklinde giriniz: ").lower()
            if yonSorgu == "q0":
                print("1 ile q0'a dönüldü !")
                continue
            else:
                print("q3'e gelindi")
                q3 = input("q3 için 1 değerini giriniz: ").lower()
                while q3 not in ["1"]:
                    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                    q3 = input("q3 için 1 değerini giriniz: ").lower()
                alfabe += q3
                print("q2'ye gelindi")
                while True:
                    sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                    while sorgu not in ["evet","hayır"]:
                        print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
                        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                    if sorgu == "evet":
                        boolean = True
                        print(f"Alfabeniz: {alfabe}")
                        break
                    else:
                        q2 = input("q2 için (0/1) değerini giriniz: ").lower()
                        while q2 not in ["0","1"]:
                            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz !")
                            q2 = input("q2 için (0/1) değerini giriniz: ").lower()
                        alfabe += q2
                        print(f"{q2} ile q2'ye dönüldü")
                        continue
        if boolean:
            break

ornekSecimi = input("Lütfen uygulamak istediğiniz örneği (ornek1/ornek2/ornek3/ornek4) şeklinde giriniz: ").lower()

while ornekSecimi not in ["ornek1","ornek2","ornek3","ornek4"]:
    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
    ornekSecimi = input("Lütfen uygulamak istediğiniz örneği (ornek1/ornek2/ornek3/ornek4) şeklinde giriniz: ").lower()

if ornekSecimi == "ornek1":
    print("1. Örnek seçildi !")
    ornek1()
elif ornekSecimi == "ornek2":
    print("2. Örnek seçildi !")
    ornek2()
elif ornekSecimi == "ornek3":
    print("3. Örnek seçildi !")
    ornek3()
else:
    print("4. Örnek seçildi !")
    ornek4()

