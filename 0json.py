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

def find_file(file_name):
    """ PyInstaller ile paketlenmiş dosyanın gerçek yolunu bulur """
    if hasattr(sys, '_MEIPASS'):
        # EXE çalışırken dosyaların açıldığı geçici klasör yolu
        return os.path.join(sys._MEIPASS, file_name)
    # Geliştirme aşamasındaki normal klasör yolu
    return os.path.join(os.path.abspath("."), file_name)

# JSON dosyanızı artık bu fonksiyonla çağırın:
json_yolu = find_file("veri.json") #veri.json yerine dosyanızın adını yazabilirsiniz

with open(json_yolu, "r", encoding="utf-8") as dosya:
    data = json.load(dosya) # data değişkeni artık bir Python sözlüğüdür ve JSON dosyasındaki verileri içerir.

'pyinstaller --onefile --add-data \"veri.json;.\" ana_kod.py'