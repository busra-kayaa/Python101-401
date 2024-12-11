# SAYILAR VE STRINGLERE GIRIS
9
9.2
9+9
9*9

print("HELLO AI ERA")
'HELLO AI ERA'

type(9) #int tipi
type(9.2) #float tipi
type("HELLO AI ERA") # str tipinde

# STRINGLERE YAKINDAN BAKALIM
123
type(123) #int
"123"
type("123") #str

"a" + "b" # çıktısı-> 'ab'
"a" " b"

"a" + "-b"

"a" - "b" # stringlerde çıkartma yapamazsın

"a "*3 # çıktısı-> 'a a a '
"a"/3 # bölme işlemi de yapamazsın.

# String Metodları -len()

# bsr = "gelecegi_yazanlar"
# del bsr

gel_yaz = "gelecegi_yazanlar" # atama işlemi

a = 9
b = 9

a*b # 9*9 = 81

len(gel_yaz) #çıktısı -> 17
len("gelecegi_yazanlar")

# String Metodları - upper() & lower()

gel_yaz = "gelecegi_yazanlar" 

gel_yaz.upper() # çıktısı -> 'GELECEGI_YAZANLAR'
gel_yaz.lower() # çıktısı -> 'gelecegi_yazanlar'

gel_yaz.islower() # çıktısı-> True

B = gel_yaz.upper()

B.islower() # çıktısı -> False
B.isupper() # çıktısı -> True

# String Metodları - replace()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.replace("e", "a") # çıktısı -> galacagi_yazanlar'

gel_yaz # çıktısı -> 'gelecegi_yazanlar'

gel_yaz.replace("a", "i") # çıktısı -> 'gelecegi_yizinlir'

# String Metodları - strip()

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip() # default boşluk geliyor
# çıktısı -> 'gelecegi_yazanlar'

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip() # çıktısı -> '*gelecegi_yazanlar*'
gel_yaz.strip("*") # çıktısı -> 'gelecegi_yazanlar'


gel_yaz = "lgelecegi_yazanlarl"
gel_yaz.strip("l") # çıktısı -> 'gelecegi_yazanlar'


# METHODALRA GENEL BAKIS

gel_yaz = "gelecegi_yazanlar"

dir(gel_yaz)
dir(str) # bu veri tipinin üzerine uygulanabilecek metodları gösterir

gel_yaz.capitalize() # ç-> 'Gelecegi_yazanlar'
gel_yaz.title() # ç-> 'Gelecegi_Yazanlar'


# SUBSTRINGLER

gel_yaz = "gelecegi_yazanlar"
gel_yaz[0] # köşeli parantezi girince python köşeli parantezden önce girmiş 
# olduğu ifadenin içerinde bir seçim işlemi gerçekleştirecek diye anlar.
# çıktısı -> 'g'

gel_yaz[1] # çıktısı -> 'e'
gel_yaz[20] # hata -> IndexError: string index out of range
gel_yaz[0:3] #sol dahil , sağ dahil değil.  Çıktısı ->'gel'
gel_yaz[3:7] # 7'ye kadar. çıktısı -> 'eceg'

# DEGİSKENLER

a = 9
b = "ali_uzaya_git"

c = a*2

a/c
a*c
a*5


type(100)
type(100.2)
type(1+2j) # çıktısı -> <class 'complex'>

a = 100.2 # değişken tanımlama / tipi = float

# TYPE DONUSUMLERI

birinci_sayi = input() # kullanıcıdan bilgi almak

toplama_bir = input()
toplama_iki = input()

type(toplama_bir) # str

toplama_bir + toplama_iki # yan yana yazar çıktı-> '54'

int (toplama_bir) + int(toplama_iki) # çıktısı -> 9

int (11.0) # 11

12

float(12) # 12.0
str(12) # '12'

type(str(12)) # <class 'str'>


# print()

print("HELLO AI ERA")

print("gelecegi", "yazanlar")

print("gelecegi", "yazanlar", sep = "_") # çıktısı -> gelecegi_yazanlar

# Fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirticilere argüman denir.

print()

# 101 Sınav
ifade = "gelecek_geldi"
ifade.replace("i", "ı")

ifade = "Merhaba!"
ifade = ifade.lower()
ifade = ifade.replace("!","")
ifade

a = "bu uzun bir metindir"
a[2:5]

ifade = "gelecegi yaziyoruz"
ifade[1]

ifade = "selam"
type(ifade)

"9" + 1

ifade = "gelecegi yaziyoruz"
ifade[0:2]

ifade = "Merhaba! "
ifade.strip("")

"a" + "b"

degisken = 4
degisken*degisken

"10" + 2

sakla = 9 
yeni_sakla = sakla*10

"_Python_".strip("_")

a = 5
b = 10
c = a*b
c