
import json
import os
isim = input("İsminizi giriniz: ")
print(f"Merhabai, {isim}! Hoş geldiniz.\n{input('Tanıdığınız birini giriniz: ')} ile aranız nasıl?") #print("Merhaba, {isim}! Hoş geldiniz.\n{a} ile aranız nasıl?".format(isim=isim, a=input("Tanıdığınız birini giriniz: ")))
karakter = input("Bir karakter giriniz: ")
sehir = input("Bir şehir giriniz: ")
hikaye = {
    "karakter": karakter,
    "sehir": sehir
}
with open("hikaye.json", "w") as h:
    json.dump(hikaye, h, ensure_ascii=False, indent=4)
print(f"{karakter}, sabah erkenden uyanıp sehir sokaklarında yürümeye başladı.Güneş yeni doğuyordu ve hava hafif serindi.Küçük bir kafe bulup sıcak bir çay içti.Birden dışarıda bir köpek havlamaya başladı.Merakla dışarı çıkıp köpeğin yanına gitti.Köpek ona dostça baktı ve kuyruğunu salladı. {karakter}, köpeğin aç olabileceğini düşündü.Hemen bir fırına gidip biraz ekmek aldı.Köpeğe uzattığında köpek hızla yedi.Bu olay {karakter}'i mutlu etti.Günün geri kalanında şehrin güzel yerlerini keşfetti. {karakter}, {sehir}'in ne kadar güzel olduğunu düşündü.Akşam olunca eve dönmek için yürümeye başladı.Yolda eski bir arkadaşını gördü.Arkadaşıyla kahve içip sohbet etti.Sonra eve dönerken gökyüzüne baktı.Yıldızlar parlıyordu ve {karakter} huzur doluydu.")
i = input("\n\n\tJson dosyası oluşturuldu. hikaye.json dosyasını silmek için 'y' tuşuna basın...\t")
if (i=='y'):
    os.remove("hikaye.json")