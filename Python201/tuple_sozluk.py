# Veri Yapıları - Tuple (demet)

"""
1.Kapsayıcıdır
2.Sıralıdır
3.Değiştirilemez!!
"""

t = ("ali", "veli", 1, 2, 3.2, [1,2,3,4])

t = "ali", "veli", 1, 2, 3.2, [1,2,3,4]

# tuple()

t = ("eleman")
type(t) # str / tuplelarda tek eleman olunca

t = ("eleman" ,)
type(t) # tuple

# Tuple Eleman Islemleri

t = ("ali", "veli", 1, 2, 3, [1,2,3,4])
t # çıktısı ->('ali', 'veli', 1, 2, 3, [1, 2, 3, 4])

t[1] # çıktı -> 'veli'
t[0:3] # çıktı -> ('ali', 'veli', 1)


t[2] = 99 # TypeError: 'tuple' object does not support item assignment

# Veri Yapıları - Dictionary (Sözlük)

"""
1.Kapsayıcıdır
2.Sırasızdır
3.Değiştirilebilir

-> Listelerde olduğu gibi index işlemleri yapılamaz.
"""

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification adn Reg"}

sozluk
len(sozluk) # çıktı -> 3

sozluk = {"REG": 10,
          "LOJ": 20,
          "CART": 30}

sozluk

sozluk = {"REG": ["RMSE" ,10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE",30] }

sozluk

# Sozluk Eleman Islemleri

sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification adn Reg"}

sozluk[0] # KeyError: 0 -> sırasız olduğundan dolayı index ile gerçekleşmez

sozluk["REG"] # çıktısı -> 'Regresyon Modeli'
sozluk["LOJ"] # çıktısı -> 'Lojistik Regresyon'

sozluk = {"REG": ["RMSE" ,10],
          "LOJ": ["MSE", 20],
          "CART": ["SSE",30] }

sozluk["REG"] # çıktısı -> ['RMSE', 10]

sozluk = {"REG": {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "LOJ": {"RMSE": 10,
                  "MSE" : 20,
                  "SSE" : 30},
          
          "CART": {"RMSE": 10,
                  "MSE" : 20,
                  "SSE" : 30} 
          }

sozluk
sozluk["REG"] # çıktısı -> {'RMSE': 10, 'MSE': 20, 'SSE': 30}
sozluk["REG"]["SSE"] # -> 30


# Sozluk - Eleman Eklemek & Degistirmek


sozluk = {"REG": "Regresyon Modeli",
          "LOJ": "Lojistik Regresyon",
          "CART": "Classification adn Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk ["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"
sozluk

l = [1]
l

sozluk [l] = " yeni bir sey" # TypeError: unhashable type: 'list'
# sozluklerde key değerleri ancak sabit veri yapıları ile oluşturulabilir
# listeyi atayamadık -> çünkü değişen bir veri yapısı

t = ("tuple", )

sozluk[t] = "yeni bir sey"
sozluk
"""
 {'REG': 'Coklu Dogrusal Regresyon',
 'LOJ': 'Lojistik Regresyon',
 'CART': 'Classification adn Reg',
 'GBM': 'Gradient Boosting Mac',
 1: 'Yapay Sinir Aglari',
 ('tuple',): 'yeni bir sey'}
 """
