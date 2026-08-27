"""
# Pythonda değişken tipleri dinamik olarak belirlenir. Yani bir değişkenin tipini belirtmek zorunda değilsiniz. Python, değişkenin değerine göre tipini otomatik olarak belirler.
x = 10 # x bir integer (tam sayı) tipindedir
print(type(x)) # <class 'int'>

x = 'Merhaba' # x artık bir string (metin) tipindedir
print(type(x)) # <class 'str'> # x e farklı bir değer atadığımızda, Python değişkenin tipini otomatik olarak değiştirir. Bu, Python'un dinamik tip özelliğinin bir örneğidir.

x = 3.14 # x artık bir float (ondalıklı sayı) tipindedir
print(type(x)) # <class 'float'>
"""

a = 5    # integer (tam sayı)
b = "5"  # string (metin)
c = 5.0  # float (ondalıklı sayı)
print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'float'>

x = 10
y = "5"
print(x + int(y))  # 15, y string olduğu için int() ile integer'a çevirdik / typecast (tip dönüşümü) yaptık