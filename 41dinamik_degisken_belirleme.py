# Python'da Type Cast / Tür Dönüşümü
## Implicit type casting
a = 10  # a => int
b = 2.5 # b => float

sonuc = a + b # sonuc => float
print(sonuc)
print(type(sonuc))

## Explicit Type Casting
x = "123"
y = int(x) ### str -> int dönüşümü
print(type(y)) #### <class 'int'>
print(y + 7) #### 130

"""
a = 10
b = "20"

'toplam = a + b ### a => int, b => str, a + b == 30 ==> false, error'
toplam = a + int(b) ### a => int, => int, a + b == 30 ==> true
print(toplam) ### toplam => int #### 30
"""

"""
a = 10
b = "20"

'toplam = a + b ### a => int, b => str, a + b == 1020 ==> false, error'
toplam = str(a) + b ### a => str, => str, a + b == 1020 ==> true
print(toplam) ### toplam => str #### 1020
"""

## Diğer sık kullanılan typecast dönüşümleri
"""
int(x)
float(x)
str(x)
bool(x)
"""

c = "3.14"
d = float(c)
print("\n\ttype(c = \"3.14\") => {}\n\ttype(d = float(c)) => {}".format(type(c), type(d)))