"""
    n adet girdi için n adet çıktı oluşturur q0 = {A}
    Δ = {0,1} , E = {0,1} için sırasıyla "101" dizgisi geldiğinde
    çıkış olarak sonu 1 üreten Mealy makinesi tasarlayınız
"""
alfabe = ""
cikti = ""
girdi = ""
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
        
def ciktiKontrol ():
    global cikti
    print(f"Vermiş olduğunuz alfabeye göre çıktı: {cikti}")

def girdiAl(durum):
    global alfabe
    global girdi
    girdi = input(f"{durum} için alfabe giriniz (0/1): ")
    while girdi not in ["0", "1"]:
        print("Yanlış alfabe girdiniz!")
        girdi = input(f"{durum} için alfabe giriniz (0/1): ")
    alfabe += girdi

def C():
    global cikti
    alfabeBittiMi()
    if alfabeBiterse:
        ciktiKontrol()
    if donguSonlandirici:
        girdiAl("C")
        if girdi == "1":
            print("Tekrar C'ye gelindi")
            cikti += "1"
            return C() 
        else:
            print("A'ya geri dönüldü")
            cikti += "0"
            return A()

def B():
    global cikti
    girdiAl("B")
    if girdi == "1":
        print("Tekrar B'ye gelindi")
        cikti += "0"
        return B() 
    else:
        print("C'ye gidildi")
        cikti += "0"
        return C()

def A():
    global cikti
    girdiAl("A")
    if girdi == "0":
        print("A'ya geri dönüldü")
        cikti += "0"
        return A() 
    else:
        print("B'ye gidildi")
        cikti += "0"
        return B()
    
A()
