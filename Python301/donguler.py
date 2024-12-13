# DONGULER - for

ogrenci = ["ali", "veli", "isik", "berk"]

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci:
    print(i)
    
print(ogrenci[0])

# for - devam 
maaslar = [1000,2000,3000,4000,5000]

maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]

for i in maaslar:
    print(i)
    
for maas in maaslar:
    print(maas)
    

# dongu ve fonksiyonları birlikte kullanmak

def kare_al(x):
    print(x**2)
    
kare_al(2)
maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
       
# maaslara yuzde 20 zam yapilacak gerekli kodları yaziniz

maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]
maaslar[2]*20/100 + maaslar[2]

# dongu yazilacak
# fonksiyon yazilacak

def yeni_maas(x):
    print(x*20/100 + x)
        
yeni_maas(1000)
yeni_maas(2000)    
yeni_maas(3000)     

for i in maaslar:
    yeni_maas(i)
        
# mini uygulama
# if, for, fonksiyonlari birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def yeni_maas(x):
    if x >= 3000:
        print(x*10/100 + x)          
    else:
        print(x*20/100 + x)

for i in maaslar:
    yeni_maas(i)
        
        
        
def maas_ust(x):
    print(x*10/100 + x)
        
def maas_alt(x):
    print(x*20/100 + x)
           
for i in maaslar:
    if i>=3000:
        maas_ust(i)
    else:
        maas_alt(i)
    
      
# break & continue       

maaslar = [8000,5000,2000,1000,3000,7000,1000]
maaslar.sort()
maaslar # [1000, 1000, 2000, 3000, 5000, 7000, 8000]

for i in maaslar:
    if i == 3000:
        print("kesildi") # 1000 1000 2000 kesildi
        break
    print(i)


for i in maaslar:
    if i == 3000:
        continue
    print(i)

# çıktı da 3000 atlanır ->
# 1000
# 1000
# 2000
# 5000
# 7000
# 8000


# while -> bu şart sağlandığı sürece


sayi = 1

while sayi < 9:
    sayi += 1
    print(sayi)


# sınav 301

sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        break
    print(i)


A = []

for i in [1,2,3,4]:
    A.append(i)

A[0]


a = [1,2,3]
b = []
for i in a:
    b.append(i**2)
b


def islem(x):
    if (x<0):
        return "NO"
    else:
        x*5
 
islem(2)


sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        continue
    print(i)

liste = ["a","b","c"]
liste.reverse()
print(liste)


def islem(x, y):
    print(x - y)

islem(3)


def harf_say(x):
    len(x)
 
harf_say("Merhaba!")

A = "*A*"    
if type(A) == str:
    A = A.strip("*")
    print(A) 
 
def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

islem(1,3)     
    
    
if [1,2,3,4][2] == 2:
    print("YES")
else:
    print("NO") 
    
    
def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)
    
def islem(x, y):
    print(x - y)

islem(3)
    
for i in ["a",11]:
    print(i)   
    
    
a = [2,4,6,8]
for i in a:
    print(i**2)       
        
        
urun_fiyatlari = [19,29,39]
 
for i in urun_fiyatlari:
    if i >= 30:
        print(i/2)
    else:
        print(i*0)
        
               
def yazdir(metin):
    print(metin, "yazanlar")
 
yazdir("gelecegi")


A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())