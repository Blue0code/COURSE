# Python'da TypeCast / Tür dönüşümü

## Implicit Type Casting
### Python'da otomatik yapılan Type Casting
"""
a = 10 #int
b = 2.5 #float

sonuc = a + b # sonuc => float
print(sonuc)
print(type(sonuc))
"""
## Explicit Type Casting
### Python'da bizim yaptığımız Type Casting
"""x = "123"
y = int(x) # string -> int dönüşümü
print(type(y))
print(y + 7)"""

a = 10
b = "20"
toplam = a + int(b)
print("int->", toplam, sep=("\t"), end=("\n"))

toplam = str(a) + b 
print("str->", toplam, sep=("\t"), end=("\n"))


"""
bool
str
int
float
"""