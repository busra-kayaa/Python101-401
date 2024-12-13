#NESNE YONELIMLI PROGRAMLAMA

# Sinif Nedir? - > benzer özellikler , ortak amaçlar taşıyan,
# içerisinde metod ve değişkenler olan yapılardır.

class VeriBilimi():
    print("Bu bir siniftir")

# Sinif Ozellikleri (Class Attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

# Siniflarin ozelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

# Siniflarin ozelliklerini degistirmek
VeriBilimci.sql= "Hayir"
VeriBilimci.sql

# Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()
ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller


veli = VeriBilimci()
veli.sql

veli.bildigi_diller # çıktısı -> ['Python']

# Ornek Ozellikleri

class VeriBilimci():
    bildigi_diller = ["R", "PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self): # self orneklemleri temsil eder
        self.bildigi_diller = []
        self.bolum = ''
        
# Bu işlem her bir örneğin kendi içinde değişen özelliklerden
# oluşabildiği bilgisini vermek

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller # çıktısı -> []

veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller # çıktısı -> ['R', 'PYTHON']

ali.bolum # çıktısı -> ''

VeriBilimci.bolum
ali.bolum = "istatistik"

VeriBilimci.bolum # ''
veli.bolum # ''

veli.bolum = "end_muh"
veli.bolum # çıktısı -> 'end_muh'
ali.bolum # çıktısı -> 'istatistik'

VeriBilimci.bolum # ''

# Ornek Metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller

# Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = "" 
        
class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
# veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
# mar1.


class Employees_yeni():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

ali = Employees_yeni("FirstName", "LastName", "Address")
ali.FirstName