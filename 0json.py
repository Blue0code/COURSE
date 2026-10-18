'''
Python Sözlüğünü JSON'a Çevirmek (json.dumps)
'''
import json

# Python Sözlüğü (Dictionary)
kullanici_veri = {
    "isim": "Ahmet",
    "yas": 28,
    "yazilimci_mi": True,
    "diller": ["Python", "JavaScript"]
}

# Python nesnesini JSON string'ine çevirme
# ensure_ascii=False -> Türkçe karakterlerin doğru görünmesini sağlar.
# indent=4 -> Çıktının düzenli ve okunabilir (girintili) olmasını sağlar.
json_verisi = json.dumps(kullanici_veri, ensure_ascii=False, indent=4)

print(json_verisi)



'''
JSON Metnini Python Sözlüğüne Çevirmek (json.loads)
'''
import json

# JSON formatında bir metin (string)
gelen_json = '{"isim": "Ahmet", "yas": 28, "yazilimci_mi": true}'

# JSON string'ini Python sözlüğüne çevirme
python_sozluk = json.loads(gelen_json)

# Artık normal bir Python sözlüğü gibi kullanabiliriz
print(python_sozluk["isim"])  # Çıktı: Ahmet
print(python_sozluk["yas"])   # Çıktı: 28

'''
JSON Dosyası Okumak ve Yazmak (json.load ve json.dump)
'''
#Dosyaya Yazma (json.dump):

with open("veri.json", "w", encoding="utf-8") as dosya: # dosya nedir? dosya, veri.json dosyasını temsil eden bir dosya nesnesidir. open() fonksiyonu ile veri.json dosyasını yazma modunda açıyoruz ve bu dosya nesnesini dosya değişkenine atıyoruz. encoding="utf-8" parametresi, dosyanın UTF-8 karakter kodlamasıyla açılmasını sağlar.
    json.dump(kullanici_veri, dosya, ensure_ascii=False, indent=4)

#Dosyadan Okuma (json.load):

with open("veri.json", "r", encoding="utf-8") as dosya:
    data = json.load(dosya) # data değişkeni artık bir Python sözlüğüdür ve JSON dosyasındaki verileri içerir.
    print(data)
    print(data["isim"])  # Çıktı: Ahmet


'''
EKLEME YAPMAK (JSON Dosyasına Yeni Veri Eklemek)
'''
import json

# 1. Adım: Mevcut JSON dosyasını okuyup hafızaya alıyoruz
with open("veri.json", "r", encoding="utf-8") as dosya:
    mevcut_veri = json.load(dosya)

# 2. Adım: Yeni veriyi sözlüğe ekliyoruz
mevcut_veri["yeni_anahtar"] = "Yeni Değer"
mevcut_veri["yas"] = 30  # Eğer 'yas' varsa güncellenir, yoksa yeni eklenir

# 3. Adım: Güncellenmiş veriyi tekrar dosyaya yazıyoruz
with open("veri.json", "w", encoding="utf-8") as dosya:
    json.dump(mevcut_veri, dosya, ensure_ascii=False, indent=4)











import os   # os modülü, işletim sistemi ile ilgili işlemler yapmak için kullanılır. Örneğin, dosya yollarını birleştirmek veya geçici klasörleri bulmak gibi işlemler için kullanılır.
import sys  # sys modülü, Python'un çalışma ortamı ile ilgili bilgileri ve işlevleri sağlar. Örneğin, programın çalıştığı platformu öğrenmek veya komut satırı argümanlarını almak gibi işlemler için kullanılır.
import json # json modülü, Python'da JSON (JavaScript Object Notation) formatında veri ile çalışmak için kullanılır. JSON, veri değişimi için yaygın olarak kullanılan bir formattır ve Python'da json modülü sayesinde JSON verilerini kolayca okuyabilir, yazabilir ve işleyebilirsiniz.

def find_file(file_name): #def fonksiyonu, find_file adında bir fonksiyon tanımlar ve file_name parametresini alır. Bu fonksiyon, PyInstaller ile paketlenmiş bir uygulamada dosyanın gerçek yolunu bulmak için kullanılır.
    """ PyInstaller ile paketlenmiş dosyanın gerçek yolunu bulur """
    if hasattr(sys, '_MEIPASS'): #hasattr() fonksiyonu, bir nesnenin belirli bir özelliğe sahip olup olmadığını kontrol eder. Burada sys modülünün '_MEIPASS' özelliğine sahip olup olmadığını kontrol eder. Bu özellik, PyInstaller ile paketlenmiş bir uygulamanın geçici çalışma dizinini temsil eder.
        # EXE çalışırken dosyaların açıldığı geçici klasör yolu
        return os.path.join(sys._MEIPASS, file_name) #os.path.join() fonksiyonu, verilen dizin ve dosya adlarını birleştirerek tam bir dosya yolu oluşturur. Burada sys._MEIPASS ile file_name birleştirilir ve geçici klasördeki dosyanın tam yolu elde edilir.
    # Geliştirme aşamasındaki normal klasör yolu
    return os.path.join(os.path.abspath("."), file_name) #os.path.abspath(".") fonksiyonu, geçerli çalışma dizininin mutlak yolunu döndürür. Bu, geliştirme aşamasında dosyanın bulunduğu klasörün tam yolunu elde etmek için kullanılır. os.path.join() ile file_name birleştirilir ve normal klasördeki dosyanın tam yolu elde edilir.

# JSON dosyanızı artık bu fonksiyonla çağırın:
json_yolu = find_file("veri.json") #veri.json yerine dosyanızın adını yazabilirsiniz

with open(json_yolu, "r", encoding="utf-8") as dosya:
    data = json.load(dosya) # data değişkeni artık bir Python sözlüğüdür ve JSON dosyasındaki verileri içerir.

'pyinstaller --onefile --add-data \"veri.json;.\" ana_kod.py'




















from cryptography.fernet import Fernet
import json

# 1. Anahtar üretme ve Fernet başlatma
key = Fernet.generate_key()
fernet = Fernet(key)

# 2. Sözlüğü JSON string yapıp bayta çevirme
sozluk = {"kullanici": "admin", "sifre": "12345"}
json_verisi = json.dumps(sozluk).encode('utf-8')

# 3. Şifreleme
sifreli_veri = fernet.encrypt(json_verisi)
print("Şifreli:", sifreli_veri)

# 4. Çözme (Decryption)
cozulmus_bayt = fernet.decrypt(sifreli_veri)
cozulmus_sozluk = json.loads(cozulmus_bayt.decode('utf-8'))
print("Çözülmüş:", cozulmus_sozluk)









from cryptography.fernet import Fernet # cryptography kütüphanesinden Fernet sınıfını içe aktarır. Fernet, simetrik şifreleme ve çözme işlemleri için kullanılan bir sınıftır. Bu sınıf, verileri güvenli bir şekilde şifrelemek ve çözmek için kullanılır.
import json

# 1. Anahtar üretme ve Fernet nesnesini oluşturma
# (Gerçek bir projede bu anahtarı güvenli bir yerde saklamalısınız)
key = Fernet.generate_key()
fernet = Fernet(key)

# Şifrelenecek örnek sözlük verisi
sozluk_verisi = {
    "kullanici_adi": "ahmet_yilmaz",
    "eposta": "ahmet@ornek.com",
    "rol": "admin"
}

# --- 1. DOSYAYA ŞİFRELİ KAYDETME (YÜKLEME) ---

# Sözlüğü JSON string yapıp bayta (bytes) çeviriyoruz
json_bayt = json.dumps(sozluk_verisi).encode('utf-8')

# Veriyi şifreliyoruz
sifreli_veri = fernet.encrypt(json_bayt)

# Şifreli veriyi ikili (binary) dosya olarak diske yazıyoruz
# Uzantısını .json yapabilirsiniz ancak içi şifreli (okunamaz) olacaktır.
dosya_yolu = "sifreli_veri.json"
with open(dosya_yolu, "wb") as dosya:
    dosya.write(sifreli_veri)

print(f"Sözlük başarıyla şifrelendi ve '{dosya_yolu}' dosyasına kaydedildi.")


# --- 2. DOSYADAN OKUMA VE ÇÖZME ---

# Şifreli dosyayı ikili (binary) modda okuyoruz
with open(dosya_yolu, "rb") as dosya:
    okunan_sifreli_veri = dosya.read()

# Verinin şifresini çözüyoruz
cozulmus_bayt = fernet.decrypt(okunan_sifreli_veri)

# Bayt verisini önce string'e, sonra tekrar Python sözlüğüne (dict) çeviriyoruz
orijinal_sozluk = json.loads(cozulmus_bayt.decode('utf-8'))

print("\nDosyadan okunup çözülen orijinal sözlük:")
print(orijinal_sozluk)











import base64 as b
import json

sozluk = {"id": 1, "rol": "editor"}
json_str = json.dumps(sozluk)

# Base64 Encode
encoded_bytes = b.b64encode(json_str.encode('utf-8'))
encoded_str = encoded_bytes.decode('utf-8')
print("Base64:", encoded_str)

# Base64 Decode
decoded_bytes = b.b64decode(encoded_str.encode('utf-8'))
cozulmus_sozluk = json.loads(decoded_bytes.decode('utf-8'))
















import base64
import hashlib
from cryptography.fernet import Fernet

# 1. Kendi belirlediğiniz şifre (Metin)
kendi_sifrem = "BenimCokGizliOzelSifrem123!"

# 2. Metni SHA-256 ile 32 baytlık benzersiz bir özete dönüştürüyoruz
# (Böylece girdi ne olursa olsun her zaman tam 32 bayt olur)
hasher = hashlib.sha256(kendi_sifrem.encode('utf-8')) # encode() metodu, metni (string) bayt dizisine (bytes) dönüştürür. SHA-256 algoritması, bayt dizisini alır ve 32 baytlık bir hash değeri üretir.
i32_baytlik_sifre = hasher.digest() # digest() metodu, hash nesnesinin özetini (hash değerini) bayt dizisi olarak döndürür. Bu, şifrenin SHA-256 algoritması ile üretilmiş 32 baytlık benzersiz bir temsilidir.

# 3. Fernet standartları için Base64 formatına kodluyoruz
fernet_anahtari = base64.urlsafe_b64encode(i32_baytlik_sifre) # urlsafe_b64encode() metodu, bayt dizisini Base64 formatına dönüştürür ve URL güvenli bir şekilde kodlar. Bu, Fernet'in gerektirdiği formatta bir anahtar üretir.

# Artık bu anahtarla Fernet nesnesini başlatabiliriz
fernet = Fernet(fernet_anahtari)
print("Üretilen Geçerli Fernet Anahtarınız:", fernet_anahtari.decode()) # decode() metodu, bayt dizisini (bytes) UTF-8 formatında bir string'e dönüştürür. Bu sayede anahtarın okunabilir bir temsilini ekrana yazdırabiliriz.