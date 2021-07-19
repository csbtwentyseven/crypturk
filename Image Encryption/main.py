import random
import time

class Eslestir():
    def sayidanharf():
        sayisalTM = open('decrypt.txt', 'r').read()  # sayisalTM = Sayısal Temiz Metin
        j = 0  # döngü index degiskeni
        sozelTM = list()  # sozelTM = Sözel Temiz Metin
        for i in sayisalTM:
            if (j % 2 == 0):
                sozelTM.append(Eslestir.osman_tablo[sayisalTM[j] + sayisalTM[j + 1]])#sayilari harflerle eslestirip sozelTM listesine sırasıyla ekliyoruz
            j = j + 1  # index değişkenini arttır.

            temiz_metin = ''.join(map(str, sozelTM))  # sozelTM listemizi stringe ceviriyoruz.

        dosyaYaz = open("duz_metin.txt", 'w')
        dosyaYaz.write(temiz_metin)#Kırılmış Şifreyi Dosyaya Yazıyoruz.

class Incele():
    basla = 0
    bitir = 1
    harfler = list()

    def durak():
        durak = ["T", "C"] #T,C DURAKLARI KELİME SETLERİ ARASINA YERLEŞİR.DAHA FAZLA DURAK EKLEYEREK KAOSU ARTTIRMAK MÜMKÜNDÜR.BKZ:PDF SAYFA4,KELİME SETLERİ
        durakEkle = random.sample(durak, 1)  # durak aralarına rastgele t ya da c harflerinden birini seçip ekler.
        return durakEkle

    def parcala():  # STRİNGİ PARÇALAR,LİSTEYE ELEMAN OLARAK VEREREK ITERE EDİLEBİLİR VAZİYETE SOKAR.
        Incele.harfler = list()  # GRAFİKSEL ARAYÜZDE OUTPUTUN ÜST ÜSTE BİNMEMESİ AMACIYLA LİSTEYİ SIFIRLIYORUZ.
        for i in range(0, len(csb)):
            Incele.harfler.append(csb[Incele.basla + i:Incele.bitir + i])  # harfi al
            Incele.harfler = Incele.harfler + Incele.durak()  # durak ekle

        return Incele.harfler#Sayısal Karşılık + Durak Listesini Döner.

class Sifre():
    sifre_liste = list()

    asal_liste = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]#İşlevsizdir.Karışıklık Amaçlı Eklenmiştir.

    sayı_liste = [10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39,
                  40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72,
                  74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]#İşlevsizdir.Karışıklık Amaçlı Eklenmiştir.


    latin_tablo = {"a": "21",
                   "b": "Q2",
                   "c": "Q6",
                   "ç": "Q7",
                   "d": 10,
                   "e": "Q1",
                   "f": 23,
                   "g": 26,
                   "ğ": 22,
                   "h": "Q8",
                   "ı": 37,
                   "i": 38,
                   "j": 97,
                   "k": 24,
                   "l": 28,
                   "m": 29,
                   "n": 27,
                   "o": 39,
                   "ö": 40,
                   "p": "Q3",
                   "r": 12,
                   "s": "Q5",
                   "ş": 16,
                   "t": "Q4",
                   "u": 41,
                   "ü": 42,
                   "v": 31,
                   "y": 36,
                   "z": 11,
                   "x":985,
                   "T": "T",
                   "C": "C",
                   " ": 1453,
                   ".": 70,
                   ",": 71,
                   "!": 72,
                   "?": 73,
                   ":": 74,
                   ";": 75,
                   "'": 76,
                   "/": 77,
                   "0": 50,
                   "1": 51,
                   "2": 52,
                   "3": 53,
                   "4": 54,
                   "5": 55,
                   "6": 56,
                   "7": 57,
                   "8": 58,
                   "9": 59,
                   "@": 78,
                   "(": 79,
                   ")": 80,
                   "{": 81,
                   "}": 82,
                   "+": 83,
                   "-": 84,
                   "*": 85,
                   "%": 86,
                   "₺": 87,
                   "$": 88,
                   "€": 89,
                   " ' ": 90,
                   "â": 91,
                   ">": 92,
                   "<": 93,
                   '"': 94,
                   "\\":95,


                   }  # latin - osmanlı alfabe karşılığı

    def latinDeger(harf):  # hata denetleme fonksiyonu.
        if (len(harf) != 1):
            return "lütfen bir harf giriniz!"
        else:
            return Sifre.latin_tablo.get(harf)

    def sayisal():
        for i in Incele.parcala():
            Sifre.sifre_liste.append(Sifre.latinDeger(i))  # harfleri sayısal değerlerine çeviren fonksiyonu tetikler.
        return Sifre.sifre_liste  # sayısal değerli liste döner.

    def ikilikimlik():  # asil sayılarla ikili kimlik oluşturuyoruz.
        kimlik_sifre = list()  # GRAFİKSEL ARAYÜZDE OUTPUTUN ÜST ÜSTE BİNMEMESİ AMACIYLA LİSTEYİ SIFIRLIYORUZ.
        j = -1
        for i in Sifre.sayisal():
            kimlik_sifre.append(i) #Sifre.sayisal listesini kimlik_sifre ismi altında tekrar kopyalıyoruz.
        try:
            for i in range(1, (len(kimlik_sifre) + 1) + len(csb)):  # girilen kelimenin harf sayısı kadar iki asal sayı ekleneceğinden harf sayısının 2 katı kadar döngüyü  döndürüyoruz.
                if ((i - 2) % 3 == 0 or i - 2 == 0):  # ikinci beşinci yedinci dokuzuncu ... indexlere asal sayi ekleniyor.Bkz:Kelime Setleri.
                    kimlik_sifre.insert(i, Sifre.asal_liste[random.randint(0, 20)])
        except:
            print("Hata!")
        return kimlik_sifre  # asal sayi eklenmiş degisken donuyor.

    def output():#Oluştuurlmuş Kelime Setleri Birleştirilip İlkel Şifre Haline Getiriliyor.İlkel Şifre Kendi İçinde Karıştırılıp Output Hazırlanıyor.
        dosya = open('hash.txt', 'w')#Hash.txt'ye yazılmaya hazırlanıyor.

        cikti1 = ''.join(map(str, Sifre.ikilikimlik()))#Sifre Listesini Stringe Çeviriyor.
        cikti2 = ''.join(reversed(cikti1))#Sifre Listesinin Stringinin Tersini Alıyor.Karıştırma Unsuru.
        cikti3 = random.uniform(10.000, 50.000)#10.000 - 50.000 arası Random Sayı Üretiyor.Karıştırma Unsuru.
        cikti4 = random.uniform(50.000, 90.000)#50.000 - 90.000 arası Random Sayı Üretiyor.Karıştırma Unsuru.

        if (len(csb) % 2 == 0): #INput'Un harf sayısının cift veya tek olmasına göre mod belirlenir.Karısıtrma Unsuru.(Mod OE)
            dosya.write(str(cikti4) + cikti1 + cikti2 + str(cikti3))#Mod OE ise OE dizilimini Yapıyor.Karıştırma Unsuru.
            return str(cikti4) + cikti1 + cikti2 + str(cikti3)
            dosya.close()

        else :#Mod OA
            dosya.write(cikti1 + str(cikti4) + str(cikti3) + cikti2)#Mod OA ise OA dizilimini Yapıyor.Karıştırma Unsuru.
            return cikti1 + str(cikti4) + str(cikti3) + cikti2
            dosya.close()





def sifirla():#hash.txt dosyasında önceki işlemlerden kalma şifreler varsa temizler.
    dosya = open("hash.txt", "w")

    dosya.write(" ")

def encrypt():
    global csb
    sifirla()#hash.txt dosyasında önceki işlemlerden kalma şifreler varsa temizler.

    metin = input("Sifrelemek IStediginiz Metni Gİrin") #arayüze input olarak verilen şifrelenmek istenen metni çeker.
    csb = metin.lower()  # inputu alıp küçük harflere döker.

    print(Sifre.output()) #Oluşturulan Şifreyi Arayüze Basar.


encrypt()
