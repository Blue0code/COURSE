"""
print(len(input("Lütfen bir metin giriniz: "))) #len() fonksiyonu, bir dizinin uzunluğunu döndürür. Bu örnekte, kullanıcıdan alınan metnin uzunluğunu hesaplar ve ekrana yazdırır.
"""

# string tipi
harf="A"
print(harf)
print(type(harf)) # type() fonksiyonu, bir değişkenin veri tipini döndürür. Bu örnekte, harf değişkeninin veri tipi ekrana yazdırılır.
ad="Hasan"
soyad="Kaya"
isim=ad*2+soyad # ad * 2 = ad + ad anlamına gelir. Yani ad değişkenini 2 kez yazdırır ve soyad değişkenini ekler.
print(isim)
print(ad, ad, soyad, sep=" ")

# integer tipi(int)
sayi1=10
print(sayi1)
print(type(sayi1))
print(12345678901234567890) # Python'da integer tipi, çok büyük sayıları da destekler.
print(type(12345678901234567890))
print(123_456_789) # Python'da integer tipinde sayılar, alt çizgi (_) ile ayrılabilir. Bu, sayının okunabilirliğini artırır.
print(type(123_456_789))
print(999999999999999999999999999999999999999) # Python'da integer tipi, çok büyük sayıları da destekler. Bu örnekte, 999999999999999999999999999999999999999 sayısı ekrana yazdırır.
print(type(999999999999999999999999999999999999999))
print(999999999999999999999999999999999999999+1) # Python'da integer tipi, çok büyük sayıları da destekler. Bu örnekte, 999999999999999999999999999999999999999 sayısına 1 ekler ve sonucu ekrana yazdırır.
print(type(999999999999999999999999999999999999999+1))

# float tipi(float) (kayan noktalı sayılar)




"""
print(0b1010) # 0b ile başlayan sayılar binary (ikili) sayı sisteminde yazılır. Bu örnekte, 0b1010 binary sayısı decimal (onluk) sayı sisteminde 10'a eşittir.
print(0o12) # 0o ile başlayan sayılar octal (sekizli) sayı sisteminde yazılır. Bu örnekte, 0o12 octal sayısı decimal (onluk) sayı sisteminde 10'a eşittir.
print(0xA) # 0x ile başlayan sayılar hexadecimal (onaltılı) sayı sisteminde yazılır. Bu örnekte, 0xA hexadecimal sayısı decimal (onluk) sayı sisteminde 10'a eşittir.
"""