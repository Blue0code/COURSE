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
print(10.2) # float tipi, ondalıklı sayıları temsil eder. Bu örnekte, 10.2 sayısı ekrana yazdırılır.
print(type(10.2)) # type() fonksiyonu, bir değişkenin veri tipini döndürür. Bu örnekte, 10.2 sayısının veri tipi ekrana yazdırılır.

# boolean tipi(bool) (mantıksal değerler)
flag=True # boolean tipi, True veya False değerlerini alabilir. Bu örnekte, flag değişkeni True değerini alır.
print(flag) # flag değişkeninin değeri ekrana yazdırılır.
print(type(flag)) # type() fonksiyonu, bir değişkenin veri tipini döndürür. Bu örnekte, flag değişkeninin veri tipi ekrana yazdırılır.
print(10>5) # 10>5 ifadesi True değerini döndürür. Bu örnekte, 10 sayısı 5 sayısından büyük olduğu için ekrana True yazdırılır.7
print(10<5) # 10<5 ifadesi False değerini döndürür. Bu örnekte, 10 sayısı 5 sayısından küçük olmadığı için ekrana False yazdırılır.
print(type(10>5)) # type() fonksiyonu, bir değişkenin veri tipini döndürür. Bu örnekte, 10>5 ifadesinin veri tipi ekrana yazdırılır.
print(type(10<5)) # type() fonksiyonu, bir değişkenin veri tipini döndürür. Bu örnekte, 10<5 ifadesinin veri tipi ekrana yazdırılır.
flag = 0 # boolean tipi, True veya False değerlerini alabilir. Bu örnekte, flag değişkeni 0 değerini alır. 0 değeri False olarak değerlendirilir; 1 değeri ise True olarak değerlendirilir.
print(flag)
print(type(flag)) # integer dır çünkü 0 ve 1 değerleri integer tipindedir. Bu örnekte, flag değişkeninin veri tipi ekrana yazdırılır. Eğer flag boolean tipinde olsaydı, type() fonksiyonu ekrana bool yazdırırdı. 0 ı boolean tipine çevirmek için bool() fonksiyonu kullanılabilir. Örneğin, flag = bool(0) ifadesi ile flag değişkeni False değerini alır ve type(flag) ifadesi ekrana bool yazdırır.
flag = bool(0) # boolean tipi, True veya False değerlerini alabilir. Bu örnekte, flag değişkeni False değerini alır.
print(flag)
print(type(flag)) # type() fonksiyonu, bir değişkenin veri tipini döndürür. Bu örnekte, flag değişkeninin veri tipi ekrana yazdırılır. Eğer flag boolean tipinde olmasaydı, type() fonksiyonu ekrana int yazdırırdı.



"""
print(0b1010) # 0b ile başlayan sayılar binary (ikili) sayı sisteminde yazılır. Bu örnekte, 0b1010 binary sayısı decimal (onluk) sayı sisteminde 10'a eşittir.
print(0o12) # 0o ile başlayan sayılar octal (sekizli) sayı sisteminde yazılır. Bu örnekte, 0o12 octal sayısı decimal (onluk) sayı sisteminde 10'a eşittir.
print(0xA) # 0x ile başlayan sayılar hexadecimal (onaltılı) sayı sisteminde yazılır. Bu örnekte, 0xA hexadecimal sayısı decimal (onluk) sayı sisteminde 10'a eşittir.
"""