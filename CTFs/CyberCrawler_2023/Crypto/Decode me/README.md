# DecodeMe
## Category : Crypto
## Points : 500(dynamic)
I wrote an encryption script for our Knight Squad team members. Can you help me write the decryption script?

Attachments: [link1](https://drive.google.com/drive/folders/1JEA0hwYJ9XAF3RUB5wU6XqGNGY2MzZbe?usp=sharing)

At first glance, the main function was the __doingMagic()__ : 
```py
def doingMagic(text):
    charsList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"

    result = ""
    i = 0
    while i < len(text):
        chunk = text[i:i+4]
        chunk_value = 0
        for char in chunk:
            chunk_value = chunk_value * 256 + ord(char)
        
        encoded_chars = []
        for _ in range(5):
            encoded_chars.append(charsList[chunk_value % 85])
            chunk_value //= 85
        
        result += ''.join(reversed(encoded_chars))
        i += 4
    
    return result
```

I tried to understand what the function did.The number 85 reminded me of base85 encoding.Giving chatgpt to explain the function, I confirmed it was indeed base85.

So the __undoingMagic__ function decrypts (From base85) :
```py
def undoingMagic(encoded_text):
    charsList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
    decoded_text = ""

    i = 0
    while i < len(encoded_text):
        chunk = encoded_text[i:i+5]
        chunk_value = 0
        for char in chunk:
            chunk_value = chunk_value * 85 + charsList.index(char)
        
        decoded_chunk = ""
        for _ in range(4):
            decoded_chunk = chr(chunk_value % 256) + decoded_chunk
            chunk_value //= 256
        
        decoded_text += decoded_chunk
        i += 5
    
    return decoded_text
```

Also you can use cyberchef's "From base85" to do the same

Flag: 
```
C3{_itS_eaSy_R1gh7_}
```



