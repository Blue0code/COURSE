import os
import json
isim = input("İsminizi giriniz: ") # Kullanıcıdan isim girişi al
print("Merhaba, " + isim + "! Hoş geldiniz.")
isim_sozluk = {"isim": isim} # Kullanıcının girdiği ismi bir sözlükte sakla
with open("0json01.json", "w", encoding="utf-8") as js1:
    json.dump(isim_sozluk, js1, ensure_ascii=False, indent=4)
with open("0json01.json", "r", encoding="utf-8") as js2:
    data = json.load(js2)
    print(data)
    print(data["isim"])
i = input("Json dosyası oluşturuldu. Silmek için 0json01.json dosyasını silmek için 'y' tuşuna basın")
if (i=='y'):
    os.remove("0json01.json") # Dosyayı sil.