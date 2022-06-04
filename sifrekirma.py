sifrelenmisdizi = []
kelimeler = []
bulunankelimeler = []

def sifrecoz(message):
    encrypted = ""
    for i in range(25):
        for char in message:
            value = ord(char) + 1
            valuex = value % 123
            if(valuex <= 0):
                valuex = 97
                encrypted += chr(valuex)
            elif(valuex == 33):
                encrypted += chr(32)
            else:
                encrypted += chr(valuex)
        
        message = encrypted
        sifrelenmisdizi.append(encrypted)
        encrypted = ""
    #print(sifrelenmisdizi)

def kelime_getir(dosya_adi):

    with open(dosya_adi, 'r',encoding='utf-8') as input_file:
        dosya_icerigi = input_file.read()

        kelime_listesi = dosya_icerigi.split()
        index = 0
        while (index <= 65493):
            kelimeler.append(kelime_listesi[index])
            index +=1

    return kelimeler


sifrecoz("kwdse")
kelime_getir("sifrelemealgoritmasi/kelimeler.txt")

for i in range(len(kelimeler)):
    for j in range(len(sifrelenmisdizi)):
        if(kelimeler[i]==sifrelenmisdizi[j]):
            bulunankelimeler.append(kelimeler[i])

print(bulunankelimeler)
#ç = 231
#ı = 305
#ö = 246
#ş = 351
#ü = 252
#ğ = 287