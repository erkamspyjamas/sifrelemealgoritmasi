import re #regEx kütüphanesini kullanmak için import ettim
 #burada üç farklı dizi oluşturdum.
sifrelenmisdizi = []#şifrelenmiş verileri tutan dizi
kelimeler = []#tdk verilerini çekmek için kullandığım dizi
bulunankelimeler = []#sonucu elde ederken içine veri eklediğim dizi
input = input("Lütfen Şifrelenmiş Veriyi giriniz : ")
def sifrecoz(message): #burada kullanıcıdan alınan şifrelenmiş diziyi loopa sokarak şifreyi kırıyoruz.
    encrypted = ""
    for i in range(25):
        for char in message:
            value = ord(char) + 1
            valuex = value % 123
            if (valuex <= 0):
                valuex = 97
                encrypted += chr(valuex)
            elif (valuex == 33):
                encrypted += chr(32)
            else:
                encrypted += chr(valuex)

        message = encrypted
        sifrelenmisdizi.append(encrypted)
        encrypted = ""

def kelime_getir(dosya_adi): #burada tdk verilerini çekmek için bir fonksiyon açıyorum
    with open(dosya_adi, 'r', encoding='utf-8') as input_file:
        dosya_icerigi = input_file.read()
        kelime_listesi = dosya_icerigi.split()
        index = 0
        while index <= 65493:
            kelimeler.append(kelime_listesi[index])
            index += 1
    return kelimeler

sifrecoz(input) #bu satırda kullanıcı şifrelenmiş veriyi girerek fonksiyonu çağırmış olacak
kelime_getir("D:/repository/sifrelemevekirmaalgoritmasi-1/kelimeler.txt") # bu satırda tdk verilerinin bulunduğu konumu girdim
for i in range(len(kelimeler)):      #burada kelimeler dizisinin uzunluğunda döngü başlattım bu sayede dizi içerisindeki her kelime dönecek.
    for j in range(len(sifrelenmisdizi)): # burada 26 defa dönen loopumuzun ürettiği şifreleri döndüren bir loop açtım ki her bir şifre için doğrulama denensin.
        x = re.split("\s", sifrelenmisdizi[j])  # burada regEx ile 2. bir kelime var ise almak için boşluktan sonra yeni eleman olarak ekliyoruz
        for k in range(len(x)): # burada x değişkeninin uzunluğu kadar, yani kullanıcının girdiği kelime kadar dönmesi için bir daha döngü oluşturduk
            if (kelimeler[i] == x[k]): #burada split komutu ile aldığımız kelime tdk listemizde var ise eklemesi için koşul oluşturuyoruz
                bulunankelimeler.append(kelimeler[i])
print("Kırılmış şifreniz : ",bulunankelimeler)

# ç = 231
# ı = 305
# ö = 246
# ş = 351
# ü = 252
# ğ = 287
# selam daktilo dalga = ugnco eblujmp ebmhb
