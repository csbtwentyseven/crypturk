#C.Said BERK
#Necati EROL
#CRYPTURK

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import random
import time


class Kir():
    def oeSade(hash):  # oe modunu sadeleştirir.
        dosyaoe = open('parcasade.txt', 'w') #Parcasade dosyasına yazmaya hazırlanır.

        parcailk = hash[16:len(hash) - 17]
        parcasade = parcailk[:int(len(parcailk) / 2)]  #Hash'ı Fazlalıklarından Ayırır.

        dosyaoe.write(parcasade)#İlkel Şifreyi Döner.
        dosyaoe.close()
        Kir.decode()#Decode fonksiyonunu tetikler

    def oaSade(hash):  # oa modunu sadeleştirir.
        dosyaoa = open("parcasade.txt", "w")#Parcasade dosyasına yazmaya hazırlanır.
        j = 0#Döngü Değişkeni
        nt = 0  # ilk nokta tespit edici
        for i in hash:  # noktayı bulana dek ara
            if (i == "." and nt == 0):  # ilk noktayı bulursan
                parcason = hash[:j - 2]  # ilk indexten itibaren nokta indeksine kadar hepsini parcason isimli degiskene ata(son iki indeksi alma).#Böylelikle Fazlalıkları Ayıkla,İlkel Şifreyi Elde Et.
                break  # döngüyü durdur

            j = j + 1

        dosyaoa.write(parcason)
        dosyaoa.close()
        Kir.decode()#Decode fonksiyonunu tetikler

    def decode():  # gelen sade hash'in sayisal verilerini ayıklar.
        dosyaYaz = open('decrypt.txt', 'w')
        dosyaOku = open('parcasade.txt', 'r')
        parcasade = dosyaOku.read()#İlkel Sifreyi Elde Eder.

        j = 0  # döngü index degiskeni
        tc = 0  # ilk durak tespit degiskeni

        for i in parcasade:
            if ((i == "☾" or i == "☪")):  # durak tespti
                if (tc == 0):  # ilk durak tespiti
                    dosyaYaz.write(parcasade[j - 2] + parcasade[j - 1])  # ilk durağın solundaki iki sayıyı yazıyor.
                    tc = 1  # ilk duraktan sonra degiskeni degistirerek ilk duragı isaretliyor.
                try:
                    dosyaYaz.write(parcasade[j + 3] + parcasade[j + 4])  # durakların iki index sağındaki harfleri dosyaya yazıyor.bkz:pdf 5.Sayfa,3.Adım(Tekrar Eden Değerleri Almaz,Sadece Anlamlı Kısımlar Çekilir.)
                except:
                    pass
            j = j + 1

        dosyaOku.close()
        dosyaYaz.close()
        Eslestir.sayidanharf()#İLkel Şifreyi Harflerle Eşleştiren Fonksiyonu Tetikliyor.


class Eslestir():
    osman_tablo = {"21": "a",  # boslugu karakter olarak goruyor.
                   "Q2": "b",
                   "Q6": "c",
                   "Q7": "ç",
                   "10": "d",
                   "Q1": "e",
                   "23": "f",
                   "26": "g",
                   "22": "ğ",
                   "Q8": "h",
                   "37": "ı",
                   "38": "i",
                   "97": "j",
                   "24": "k",
                   "28": "l",
                   "29": "m",
                   "27": "n",
                   "39": "o",
                   "40": "ö",
                   "Q3": "p",
                   "12": "r",
                   "Q5": "s",
                   "16": "ş",
                   "Q4": "t",
                   "41": "u",
                   "42": "ü",
                   "31": "v",
                   "36": "y",
                   "11": "z",
                   "T": "T",
                   "C": "C",
                   "14": " ",
                   "70": ".",
                   "71": ",",
                   "72": "!",
                   "73": "?",
                   "74": ":",
                   "75": ";",
                   "76": "'",
                   "77":"/",
                   "78":"@",
                   "79":"(",
                   "80":")",
                   "81":"{",
                   "82":"}",
                   "83":"+",
                   "84":"-",
                   "85":"*",
                   "86":"%",
                   "87":"₺",
                   "88":"$",
                   "89":"€",
                   "90":"'",
                   "91":"â",
                   "92":">",
                   "93":"<",
                   "94":'"',
                   "50": "0",
                   "51": "1",
                   "52": "2",
                   "53": "3",
                   "54": "4",
                   "55": "5",
                   "56": "6",
                   "57": "7",
                   "58": "8",
                   "59": "9",
                   "95":" \n ",
                   "61":"q",
                   "62":"w",
                   "96":"\\",
                   "98":"x",
                   "99":"A",
                   "I9":"B",
                   "I8":"C",
                   "I7":"Ç",
                   "I6":"D",
                   "I5":"E",
                   "I4":"F",
                   "I3":"G",
                   "I2":"Ğ",
                   "I1":"H",
                   "I0":"I",
                   "M9":"İ",
                   "M8":"J",
                   "M7":"K",
                   "M6":"L",
                   "M5":"M",
                   "M4":"N",
                   "M3":"O",
                   "M2":"Ö",
                   "M1":"P",
                   "M0":"R",
                   "G9":"S",
                   "G8":"Ş",
                   "G7":"T",
                   "G6":"U",
                   "G5":"Ü",
                   "G4":"V",
                   "G3":"Y",
                   "G2":"Z",
                   "G1":"W",
                   "G0":"X",
                   "J9":"Q",
                   "J8":"=",
                   "J7":"`",
                   "J6":"#",
                   "J5":"_",
                   "J4":"^",
                   "C9":"|",
                   "C8":"&",
                   "C7":"[",
                   "C6":"]",
                   "C1":"~",
                   }  # latin - osmanlı alfabe karşılığı

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

        return temiz_metin

def decrypt(sifrelenmisMetin):
    global csb #Arayüze Verilen İnputun Referansı
    csb = sifrelenmisMetin.strip() # sağdaki,soldaki boşlukları temizleme.
    #if (time.strftime("%H" + "%M") == "0415"):  # saat 4.15 ise kırılım işlemini başlat
    if (True):#DİKKAT! GÜVENLİ MOD KAPALI.GÜVENLİ MOD DECRYPTION TOOL'UN İSTENMEYEN KİŞİLERCE ELE GEÇİRİLMESİ DURUMUNA ÖNLEM OLARAK GELİŞTİRİLMİŞ,YALNIZCA SAAT 4.15'TE KIRILMA İŞLEMİNE İZİN VEREN VE 4.15 DIŞINDA KIRILMAYA ÇALIŞILDIĞINDA UYARI VERMEYEN EMNİYET MODUDUR.BÖYLECE DECRYPTION TOOL ÇALINSA DAHİ DECRYPTION İŞLEMİ YAPILAMAZ.

        if (csb != "" and csb[2] == "."):  #Mod OE ise yani şifrelemek istenen metinin harf sayısı çift sayı ise OE kırılım modu başlar.
            Kir.oeSade(csb)  # oe sadeleştirmeyi başlat

        elif (csb != "" and csb[2] != "."):  # #Mod OA ise yani şifrelemek istenen metinin harf sayısı tek sayı ise OA kırılım modu başlar.
            Kir.oaSade(csb)  # oa sadeleştirmeyi başlat.

        else:
            raise SyntaxError
        dosya_oku = open("duz_metin.txt","r")
        return dosya_oku.read()

