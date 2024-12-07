"""
    n adet girdi için n+1 adet çıktı oluşturur(hiçbir girdi olmadan lambda)
    q0 = {A} , Δ = {0,1,2,3,4} , E = {0,1} için bir Moore makinesi tasarlayınız
"""

alfabe = ""
cikti = ""
alfabeBiterse = False
donguSonlandirici = True

def alfabeBittiMi():
    global alfabeBiterse
    global donguSonlandirici
    alfabeSonuSorgu = input("Alfabenizi tamamladınız mı ? (evet/hayır) olarak giriniz: ").lower()
    while alfabeSonuSorgu not in ["evet","hayır"]:
        print("Yanlış cevap verdiniz! ")
        alfabeSonuSorgu = input("Alfabenizi tamamladınız mı ? (evet/hayır) olarak giriniz: ").lower()
    if alfabeSonuSorgu == "evet":
        alfabeBiterse = True
        donguSonlandirici = False
        print(f"Girilen alfabe '{alfabe}' dir. ")
        
def alfabeKontrol (durum):
    if alfabeBiterse:
        if durum == "A":
            print("Çıktı: 0'dır")
        elif durum == "B":
            print("Çıktı: 1'dir")
        elif durum == "C":
            print("Çıktı: 2'dir")
        elif durum == "D":
            print("Çıktı: 3'tür")
        else:
            print("Çıktı: 4'tür")

def girdiAl(durum):
    global alfabe
    global cikti
    girdi = input(f"{durum} için alfabe giriniz (0/1): ")
    while girdi not in ["0", "1"]:
        print("Yanlış alfabe girdiniz!")
        girdi = input(f"{durum} için alfabe giriniz (0/1): ")
    alfabe += girdi
    cikti = girdi

def A():
    girdiAl("A")
    alfabeBittiMi()
    if alfabeBiterse:
        alfabeKontrol("A")
    if donguSonlandirici:
        if cikti == "0":
            print("Başa dönüldü")
            return A() 
        else:
            print("B'ye gelindi")
            return B()  

def B():
    girdiAl("B")
    alfabeBittiMi()
    if alfabeBiterse:
        alfabeKontrol("B")
    if donguSonlandirici:
        if cikti == "0":
            print("C'ye gelindi")
            return C() 
        else:
            print("D'ye gelindi")
            return D() 

def C():
    girdiAl("C")
    alfabeBittiMi()
    if alfabeBiterse:
        alfabeKontrol("C")
    if donguSonlandirici:
        if cikti == "1":
            print("A'ya geri dönüldü")
            return A()  
        else:
            print("E'ye gelindi")
            return E() 

def D():
    girdiAl("D")
    alfabeBittiMi()
    if alfabeBiterse:
        alfabeKontrol("D")
    if donguSonlandirici:
        if cikti == "0":
            print("B'ye gidildi")
            return B() 
        else:
            print("C'ye gelindi")
            return C() 

def E():
    girdiAl("E")
    alfabeBittiMi()
    if alfabeBiterse:
        alfabeKontrol("E")
    if donguSonlandirici:
        if cikti == "1":
            print("E'ye dönüldü")
            return E()
        else:
            print("D'ye dönüldü")
            return D()

A()


