
alphabet = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z'] 
#Burada alfabe listesi oluşturdum.


def encryptmessage(message,key):
    encrypted_message = ""  #Şifrelenecek mesajı içerecek boş bir string tanımladım.
    sayac = 0 #Key içerisinde index değeri döndürmek için bir sayaç tanımladım.
    str(key)#Keyi parçaladım.
    for i in message: #mesaj içerisindeki her harfi döngüye soktum.
        if i not in alphabet: #eğer alfabe listesinin içerisinde bulunmayan bir karakterle karşılaşırsak listeye eklemesi için koşul atadım.
            encrypted_message += i
        else:
            encrypted_message += alphabet[(alphabet.index(i)+alphabet.index(key[sayac])) % len(alphabet)] #Burada mesajın value'suna key value'sunu ekledim ve diziyi aşmaması için modunu aldım.
            sayac+=1 #Burda sayacı bir arttırdım çünkü mesaj içerisindeki her bir harfin key içerisindeki harflerle senkronize bir biçimde şifrelenmesi gerekiyor.
            if(sayac==len(key)):# Out of range hatasının önüne geçmek için ve key uzunluğu sayaç değeriyle eşitlenirse keyin baştan başlaması için 0'a eşitledim. 
                sayac=0    
    print("The encrypted message is : ", encrypted_message)

encryptmessage("merhaba dünya03abc", "hayat")

def decryptmessage(message,key):
    decrypted_message = ""
    sayac = 0
    str(key)
    for i in message:
        if i not in alphabet:
            decrypted_message += i
        else:
            
            decrypted_message += alphabet[(alphabet.index(i)-alphabet.index(key[sayac])) % len(alphabet)] #decrypt ederken sadece toplamayı çıkarma olarak değiştirdim
            sayac+=1
            if(sayac==len(key)):
                sayac=0     
    print("The decrypted message is : ", decrypted_message)

decryptmessage("tephtıa cüğga03ybü","hayat")