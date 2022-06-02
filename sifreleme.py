
alphabet = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z']


def encryptmessage(message,key):
    encrypted_message = ""
    sayac = 0
    str(key)
    for i in message:
        if i not in alphabet:
            encrypted_message += i
        else:
           
            encrypted_message += alphabet[(alphabet.index(i)+alphabet.index(key[sayac])) % len(alphabet)]
            sayac+=1
            if(sayac==len(key)):
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
            
            decrypted_message += alphabet[(alphabet.index(i)-alphabet.index(key[sayac])) % len(alphabet)]
            sayac+=1
            if(sayac==len(key)):
                sayac=0     
    print("The decrypted message is : ", decrypted_message)

decryptmessage("tephtıa cüğga03ybü","hayat")