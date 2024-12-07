"""
verilen bir dizginin aşşağıdaki kurala göre 2li dfa olup olmadıgını kontrol eden program

    Q = {q0,q1,q2,q3} , F = {q3} , E = {0,1} için
   
         |   0   |    1 
    -----|-------|---------
     q0 =| q1, R |  q2, R       ## 0-1 harflerine göre verilen dizgideki o anki sıradaki harfin 
    -----|-------|---------     ## sola veya sağa ve hangi harfe gitceğini gösteren tablo
     q1 =| q3, L |  q2, L       ## q3'te biten dizgiler geçerlidir '00' gibi
    -----|-------|---------
     q2 =| q2, R |  q3, R
    -----|-------|---------
     q3  | q1, R |  q2, L

"""
kalinanYer = ""
solTaraf = ""
sagTaraf = input("Lütfen dizinizi (0/1) türünden olacak şekilde giriniz: ")

def q3(harf):
    global kalinanYer, solTaraf, sagTaraf
    if harf == "0":
        print("q1'e geldiniz")
        solTaraf += sagTaraf[0]
        sagTaraf = sagTaraf[1:]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q1"
    else:
        print("q2'ye geldiniz")
        sagTaraf = solTaraf[-1] + sagTaraf
        solTaraf = solTaraf[:-1]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q2"

def q2(harf):
    global kalinanYer, solTaraf, sagTaraf
    if harf == "0":
        print("q2'ye geldiniz")
        solTaraf += sagTaraf[0]
        sagTaraf = sagTaraf[1:]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q2"
    else:
        print("q3'e geldiniz")
        solTaraf += sagTaraf[0]
        sagTaraf = sagTaraf[1:]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q3"

def q1(harf):
    global kalinanYer, solTaraf, sagTaraf
    if harf == "0":
        print("q3'e geldiniz")
        sagTaraf = solTaraf[-1] + sagTaraf
        solTaraf = solTaraf[:-1]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q3"
    else:
        print("q2'ye geldiniz")
        sagTaraf = solTaraf[-1] + sagTaraf
        solTaraf = solTaraf[:-1]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q2"

def q0(harf):
    global kalinanYer, solTaraf, sagTaraf
    if harf == "0":
        print("q1'e geldiniz")
        solTaraf += sagTaraf[0]
        sagTaraf = sagTaraf[1:]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q1"
    else:
        print("q2'ye geldiniz")
        solTaraf += sagTaraf[0]
        sagTaraf = sagTaraf[1:]
        print(f"Sol taraf: {solTaraf}, Sağ taraf: {sagTaraf}")
        kalinanYer = "q2"
     

baslangic = True
for i in sagTaraf:
     harf = i  # ilk harf q0'a kıyasla başlar ve kendince devam eder 
     if baslangic:
          q0(harf)
          baslangic = False
     else:
          if kalinanYer == "q0":
               q0(harf)
          elif kalinanYer == "q1":
               q1(harf)
          elif kalinanYer == "q2":
               q2(harf)
          else:
               q3(harf)


if kalinanYer == "q3":  ## Uç durumda en son kalırsa kod okunur
    print("Başlangıçta girmiş olduğunuz dizgi geçerlidir")
else:
    print("Başlangıçta girmiş olduğunuz dizgi geçerli değildir")