from Crypto.Util.number import getPrime, inverse, bytes_to_long

def generate_key(key_size=133, e=65537):
    p = getPrime(key_size)
    q = getPrime(key_size)
    n = p * q
    l = (p - 1) * (q - 1)
    d = inverse(e, l)
    return n, e, d, p  

def encrypt_message(message, n, e):
    m_bytes = message.encode() 
    ciphertext = pow(bytes_to_long(m_bytes), e, n)
    return ciphertext

def main():
    with open('flag.txt', 'r') as file:
        flag = file.read()
    n, e, _, p = generate_key()  
    ciphertext = encrypt_message(flag, n, e)
    
    print('Ciphertext: ', ciphertext)
    print('n: ', n)
    
    binary_p = "{0:b}".format(p)
    print('binary: ', binary_p[:117])

if __name__ == "__main__":
    main()
