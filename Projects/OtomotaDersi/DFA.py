# Deterministik Sonlu Özdevinir Örnekleri

def ornek1():
    """
    Q = {q0,q1,q2} , F = {q2} , E = {0,1} için
    "1001" dizgisini içeren DFA'yı oluşturunuz
    """
    boolean = False
    alfabe = ""
    while True:
        q0 = input("q0 için alfabe giriniz(0/1): ")
        while q0 not in ["0","1"]:
            print("Yanlıs alfabe girdiniz!")
            q0 = input("q0 için alfabe giriniz(0/1): ")
        if q0 == "1":
            print("q0'a döndünüz")
            alfabe += q0
            continue
        else:
            alfabe += q0
            print("q1'e geldiniz !")
            while True:
                q1 = input("q1 için alfabe giriniz(0/1): ")
                while q1 not in ["0","1"]:
                    print("Yanlıs alfabe girdiniz!")
                    q1 = input("q1 için alfabe giriniz(0/1): ")
                if q1 in ["0","1"]:
                    alfabe += q1
                    while True:
                        print("q2'ye geldiniz")
                        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                        while sorgu not in ["evet","hayır"]:
                            print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
                            sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                        if sorgu == "evet":
                            boolean = True
                            print(f"Alfabeniz: {alfabe}")
                            break
                        q2 = input("q2 için alfabe giriniz(0/1): ")
                        while q2 not in ["0","1"]:
                            print("Yanlıs alfabe girdiniz!")
                            q2 = input("q2 için alfabe giriniz(0/1): ")
                        if q2 == "1":
                            alfabe += q2
                            continue
                        else:
                            alfabe += q2
                            print("q1'e geri döndünüz! ")
                            break
                if boolean:
                        break
            if boolean:
                break

def ornek2():
    """
    Q = {q0,q1,q2,q3(ölü durum)} , F = {q2} , E = {a,b} için
    içerisinde iki adet "a" içeren DFA'yı oluşturunuz
    (En fazla 2 adet a olacak)
    """
    alfabe = ""
    boolean = False
    while True:    
        q0 = input("q0 için alfabe giriniz(a/b): ")
        while q0 not in ["a","b"]:
            print("Yanlıs alfabe girdiniz!")
            q0 = input("q0 için alfabe giriniz(a/b): ")
        if q0 == "b":
            alfabe += q0
            print("q0'a döndünüz")
            continue
        else:
            alfabe += q0
            while True:
                print("q1'e geldiniz")
                q1 = input("q1 için alfabe giriniz(a/b): ")
                while q1 not in ["a","b"]:
                    print("Yanlıs alfabe girdiniz!")
                    q1 = input("q1 için alfabe giriniz(a/b): ")
                if q1 == "b":
                    alfabe += q1
                    print("Tekrar q1'e dönüyorsunuz")
                    continue
                else:
                    alfabe += q1
                    print("q2'ye geldiniz")
                    while True:
                        sorgu = input("Bitirmek ister misiniz? (evet/hayır) olarak cevaplayınız: ").lower()
                        while sorgu not in ["evet","hayır"]:
                            print("Yanlış cevap verdiniz, Tekrar deneyiniz!")
                            sorgu = input("Bitirmek ister misiniz? (evet/hayır) olarak cevaplayınız: ").lower()
                        if sorgu =="evet":
                            print(f"Alfabeniz: {alfabe}")
                            boolean = True
                            break
                        q2 = input("q2 için alfabe giriniz(a/b): ")
                        while q2 not in ["a","b"]:
                            print("Yanlıs alfabe girdiniz!")
                            q2 = input("q2 için alfabe giriniz(a/b): ")
                        if q2 == "b":
                            print("Tekrar q2'ye döndünüz")
                            alfabe += q2
                            continue
                        else:
                            print("Ölü durum yani q3'e geldiniz!")
                            print(f"Alfabeniz: {alfabe}")
                            boolean = True
                            break
        
                    if boolean:
                        break
            if boolean:
                break

def ornek3():
    """
    Q = {q0,q1} , F = {q0} , E = {0,1} için
    çift sayıda birleri içeren DFA'yı oluşturunuz
    (1'lerin kullanılma toplamı sayısı çift olacak)
    ** 0 tane 1 de çifttir **
    """
    alfabe = ""
    
    while True:
        boolean = False
        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()  # Başlangıç durum olduğu için lambda alabilir
        while sorgu not in ["evet","hayır"]:
            print("Yanlış cevap verdiniz,Lütfen tekrar deneyiniz!")
            sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
        if sorgu == "evet":
            print(f"Alfabeniz: {alfabe}")
            boolean = True
        else:
            pass
        if boolean:
            break
        q0 = input("q0 için alfabe giriniz(0/1): ")
        while q0 not in ["0","1"]:
            print("Yanlıs alfabe girdiniz!")
            q0 = input("q0 için alfabe giriniz(0/1): ")
        if q0 =="0":
            alfabe += q0
            print("q0'a geri döndünüz")
            continue
        else:
            alfabe += q0
            print("q1'e geldiniz")
            while True:
                q1 = input("q1 için alfabe giriniz(0/1): ")
                while q1 not in ["0","1"]:
                    print("Yanlıs alfabe girdiniz!")
                    q1 = input("q1 için alfabe giriniz(0/1): ")
                if q1 == "0":
                    alfabe += q1
                    print("q1'a geri döndünüz")
                    continue
                else:
                    alfabe += q1
                    print("q0'a döndünüz!")
                    break

def ornek4():
    """
    Q = {q0,q1} , F = {q0} , E = {0,1} için
    tek sayıda birleri içeren DFA'yı oluşturunuz
    (1'lerin kullanılma toplamı sayısı tek olacak)
    """
    alfabe = ""
    boolean = False 
    while True:
        q0 = input("q0 için alfabe giriniz(0/1): ")
        while q0 not in ["0","1"]:
            print("Yanlıs alfabe girdiniz!")
            q0 = input("q0 için alfabe giriniz(0/1): ")
        if q0 =="0":
            alfabe += q0
            print("q0'a geri döndünüz")
            continue
        else:
            alfabe += q0
            print("q1'e geldiniz")
            while True:
                sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower() 
                while sorgu not in ["evet","hayır"]:
                    print("Yanlış cevap verdiniz,Lütfen tekrar deneyiniz!")
                    sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                if sorgu == "evet":
                    print(f"Alfabeniz: {alfabe}")
                    boolean = True
                if boolean:
                    break
                q1 = input("q1 için alfabe giriniz(0/1): ")
                while q1 not in ["0","1"]:
                    print("Yanlıs alfabe girdiniz!")
                    q1 = input("q1 için alfabe giriniz(0/1): ")
                if q1 == "0":
                    alfabe += q1
                    print("q1'a geri döndünüz")
                    continue
                else:
                    alfabe += q1
                    print("q0'a döndünüz!")
                    break

def ornek5():
    """
    Q = {q0,q1,q2} , F = {q2} , E = {a,b} için
    w'si "..ab" ile biten DFA'yı çiziniz
    """
    alfabe = ""
    boolean = False
    basaDon = False
    while True:
        q0 = input("q0 için alfabe giriniz(a/b): ")
        while q0 not in ["a","b"]:
            print("Yanlıs alfabe girdiniz!")
            q0 = input("q0 için alfabe giriniz(a/b): ")
        if q0 =="a":
            alfabe += q0
            print("q0'a geri döndünüz")
            continue
        else:
            alfabe += q0
            print("q1'e geldiniz")
            while True:
                q1 = input("q1 için alfabe giriniz(a/b): ")
                while q1 not in ["a","b"]:
                    print("Yanlıs alfabe girdiniz!")
                    q1 = input("q1 için alfabe giriniz(a/b): ")
                if q1 == "b":
                    alfabe += q1
                    print("Tekrar q1'e geldiniz")
                    continue
                else:
                    alfabe += q1
                    print("q2'ye geldiniz")
                    while True:
                        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower() 
                        while sorgu not in ["evet","hayır"]:
                            print("Yanlış cevap verdiniz,Lütfen tekrar deneyiniz!")
                            sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
                        if sorgu == "evet":
                            print(f"Alfabeniz: {alfabe}")
                            boolean = True
                        if boolean:
                            break
                        q2 = input("q2 için alfabe giriniz(a/b): ")
                        while q1 not in ["a","b"]:
                            print("Yanlıs alfabe girdiniz!")
                            q2 = input("q2 için alfabe giriniz(a/b): ")
                        if q2 == "b":
                            alfabe += q2
                            print("q1'e geri geldiniz")
                            break
                        else:
                            alfabe += q2
                            print("q0'a geri geldiniz")
                            basaDon = True
                            break
                    if boolean:
                        break
                    if basaDon:
                        break
            if boolean:
                break

def ornek6():
    """
    Q = {q0,q1,q2,q3} , F = {q0} , E = {a,b,c} için
    w ="x" dizgisi 4 ün katı olan DFA'yı oluşturunuz
    (En fazla 2 adet a olacak)
    """
    boolean = False
    alfabe = ""
    while True:
        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()  # Başlangıç durum olduğu için lambda alabilir
        while sorgu not in ["evet","hayır"]:
            print("Yanlış cevap verdiniz,Lütfen tekrar deneyiniz!")
            sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
        if sorgu == "evet":
            print(f"Alfabeniz: {alfabe}")
            break
        
        q0 = input("q0 için alfabe giriniz(a/b/c): ")
        while q0 not in ["a","b","c"]:
            print("Yanlıs alfabe girdiniz!")
            q0 = input("q0 için alfabe giriniz(a/b/c): ")
        if q0 in ["a","b","c"]:
            alfabe += q0
            print("q1'e geldiniz")
        
        q1 = input("q1 için alfabe giriniz(a/b/c): ")
        while q1 not in ["a","b","c"]:
            print("Yanlıs alfabe girdiniz!")
            q1 = input("q1 için alfabe giriniz(a/b/c): ")
        if q1 in ["a","b","c"]:
            alfabe += q1
            print("q2'ye geldiniz")
        
        q2 = input("q2 için alfabe giriniz(a/b/c): ")
        while q2 not in ["a","b","c"]:
            print("Yanlıs alfabe girdiniz!")
            q2 = input("q2 için alfabe giriniz(a/b/c): ")
        if q2 in ["a","b","c"]:
            alfabe += q2
            print("q0'a geri dönüldü")
            continue

ornekSecimi = input("Lütfen uygulamak istediğiniz örneği (ornek1/ornek2/ornek3/ornek4/ornek5/ornek6) şeklinde giriniz: ").lower()

while ornekSecimi not in ["ornek1","ornek2","ornek3","ornek4","ornek5","ornek6"]:
    print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
    ornekSecimi = input("Lütfen uygulamak istediğiniz örneği (ornek1/ornek2/ornek3/ornek4/ornek5/ornek6) şeklinde giriniz: ").lower()

if ornekSecimi == "ornek1":
    print("1. Örnek seçildi !")
    ornek1()
elif ornekSecimi == "ornek2":
    print("2. Örnek seçildi !")
    ornek2()
elif ornekSecimi == "ornek3":
    print("3. Örnek seçildi !")
    ornek3()
elif ornekSecimi == "ornek4":
    print("4. Örnek seçildi !")
    ornek4()
elif ornekSecimi == "ornek5":
    print("5. Örnek seçildi !")
    ornek5()
else:
    print("6. Örnek seçildi !")
    ornek6()


