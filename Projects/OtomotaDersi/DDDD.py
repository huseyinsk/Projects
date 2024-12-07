#Düzgün Diller Düzgün Deyimler konusunu ele alan python uygulaması

bittiMi = False
girdi = ""
alfabe = ""

def girdiAl(durum):
    global girdi
    girdi = input(f"{durum} için (0/1) girdisini seçiniz: ")
    while girdi not in ["0","1"]:
        print("Yanlış girdi yaptınzı, Lütfen tekrar deneyiniz!")
        girdi = input(f"{durum} için (0/1) girdisini seçiniz: ")

def bitirmeSorgu():
    global bittiMi
    global alfabe
    sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
    while sorgu not in ["evet","hayır"]:
        print("Yanlış cevap verdiniz, Lütfen tekrar deneyiniz! ")
        sorgu = input("Bitirmek ister misiniz ? (evet/hayır) olarak giriniz: ").lower()
    if sorgu == "evet":
        bittiMi = True
        print(f"Alfabeniz: '{alfabe}' dir.")

def ornek1():
    """
    p = (a+bc*)*  problemi
    """
    global alfabe
    while True:
        bitirmeSorgu()
        if bittiMi:
            break
        q0 = input(f"q0 için (a/b) girdisini seçiniz: ").lower()
        while q0 not in ["a","b"]:
            print("Yanlış girdi yaptınzı, Lütfen tekrar deneyiniz!")
            q0 = input(f"q0 için (a/b) girdisini seçiniz: ").lower()
        alfabe += q0
        if q0 =="a":
            print("q0'a geri dönüldü")
            continue
        else:
            print("q1'e gidildi")
            while True:
                bitirmeSorgu()
                if bittiMi:
                    break
                q1 = input(f"q1 için (c/x(λ için)) girdisini seçiniz: ").lower()
                while q1 not in ["c","x"]:
                    print("Yanlış girdi yaptınzı, Lütfen tekrar deneyiniz!")
                    q1 = input(f"q1 için (b/x(λ için)) girdisini seçiniz: ").lower()
                if q1 == "x":
                    alfabe += "λ"
                    print("q0'a dönüldü")
                    break
                else:
                    alfabe += q1
                    print("Tekrar q1'e dönüldü")
                    continue
        if bittiMi:
            break

def ornek2():
    """
    p = 0+1+(01)*+1
    """        
    def A():
        global alfabe
        girdiAl("A")
        alfabe += girdi
        if girdi == "0":
            print("D'ye gidildi")
            return D()
        else:
            print("B'ye gidildi")
            return B()    
        
    def B():
        global alfabe
        girdiAl("B")
        alfabe += girdi
        if girdi == "0":
            print("C'ye gidildi")
            return C()
        else:
            print("D'ye gidildi")
            return D()
    
    def C():
        global alfabe
        girdi = input("C için '1' harfini giriniz: ")
        while girdi != "1":
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz!")
            girdi = input("C için '1' harfini giriniz: ")

        alfabe += girdi
        if girdi == "1":
            print("B'ye geri gidildi")
            return B()
        
    def D():
        global alfabe
        print(f"Otomat sona ermiştir"
              +f"\nAlfabeniz: {alfabe}'dir")
    A()

def ornek3():
    """
    p = a(bc*b+cb*c)
    """
    global alfabe
    global girdi

    def q0():
        global alfabe
        girdi = input("q0 için a değerini giriniz: ").lower()
        while girdi != "a":
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q0 için a değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "a":
            print("q1'e gidildi")
            return q1()
    
    def q1():
        global alfabe
        girdi = input("q1 için (b/c) değerini giriniz: ").lower()
        while girdi not in ["b","c"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q1 için (b/c) değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "b":
            print("q2'ye gidildi")
            return q2()
        else:
            print("q3'e gidildi")
            return q3()

    def q2():
        global alfabe
        girdi = input("q2 için (b/c) değerini giriniz: ").lower()
        while girdi not in ["b","c"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q2 için (b/c) değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "b":
            print("q4'e gidildi")
            return q4()
        else:
            print("Tekrar q2'ye gelindi")
            return q2()

    def q3():
        global alfabe
        girdi = input("q3 için (b/c) değerini giriniz: ").lower()
        while girdi not in ["b","c"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q3 için (b/c) değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "c":
            print("q4'e gidildi")
            return q4()
        else:
            print("Tekrar q3'e gelindi")
            return q3()
        
    def q4():
        global alfabe
        print("Otomata sona ermiştir"
              +f"\nAlfabeniz: {alfabe}'dir")
    q0()

def ornek4():
    """
    p = (a(bb)*a + b*ab)
    """
    global alfabe
    global girdi

    def q0():
        global alfabe
        sorgu = input("Bitirmek ister misiniz? (evet/hayır) olarak cevaplayınız: ").lower()
        while sorgu not in ["evet","hayır"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            sorgu = input("Bitirmek ister misiniz? (evet/hayır) olarka cevaplayınız: ").lower()
        if sorgu == "evet":
            print(f"Otomota sona ermiştir."
                  +f"\nAlfabeniz: {alfabe}'dir.")
        else:
            girdi = input("q0 için (a/b) değerini giriniz: ").lower()
            while girdi not in ["a","b"]:
                print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
                girdi = input("q0 için (a/b) değerini giriniz: ").lower()
            alfabe += girdi
            if girdi == "a":
                print("q1'e gidildi")
                return q1()
            else:
                print("q3'e gidildi")
                return q3()
    
    def q1():
        global alfabe
        girdi = input("q1 için (a/b) değerini giriniz: ").lower()
        while girdi not in ["a","b"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q1 için (a/b) değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "b":
            print("q2'ye gidildi")
            return q2()
        else:
            print("q0'a geri dönüldü")
            return q0()

    def q2():
        global alfabe
        girdi = input("q2 için (b) değerini giriniz: ").lower()
        while girdi not in ["b"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q2 için (b) değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "b":
            print("q1'e geri gidildi")
            return q1()

    def q3():
        global alfabe
        girdi = input("q3 için (a/b) değerini giriniz: ").lower()
        while girdi not in ["a","b"]:
            print("Yanlış girdi yaptınız, Lütfen tekrar deneyiniz")
            girdi = input("q3 için (a/b) değerini giriniz: ").lower()
        alfabe += girdi
        if girdi == "a":
            print("Tekrar q3'e gidildi")
            return q3()
        else:
            print("Tekrar q0'a gidildi")
            return q0()
        
    q0()

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
else:
    print("4. Örnek seçildi !")
    ornek4()


