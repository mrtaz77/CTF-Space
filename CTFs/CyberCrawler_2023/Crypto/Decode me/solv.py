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

encoded = "Lo<6{X>?OxWnoi!Us5q=Xg6Pd"

print(encoded)

decrypt = undoingMagic(encoded)

print(decrypt)

# C3{_itS_eaSy_R1gh7_}
