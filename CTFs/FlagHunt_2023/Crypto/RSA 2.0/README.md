# RSA 2.0
## Category : Crypto
## Points : 200

## Description
![img](/CTFs/FlagHunt_2023/Crypto/RSA%202.0/chall.png)

__Solved post ctf__

I downloaded the [zip file](https://drive.google.com/drive/folders/100y9SfkRJf3VdFZwrYGRVYRp80y2GyYZ?usp=sharing) which contained the following ciphertext
```py
Ciphertext:  42215186860008813166236773400733103956726183177154610644607876116447486521133856
n:  50057288776921281723975594148690987728601324019166931604097170720693481410035513
binary:  101100000110011110000000100011100100110000010010110111111100000101100110011000000110100111110101001010110001011000001
```

This gives the flavour of rsa. So I checked the given `rsa_2.0_.py` as well.

```py
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
```

Yep,this is an RSA.From here we get `e = 65537`.The primes `p` & `q` are 133 bits long, so not crackable by factorization.

However, the main function does look interesting...
```py
def main():
    with open('flag.txt', 'r') as file:
        flag = file.read()
    n, e, _, p = generate_key()  
    ciphertext = encrypt_message(flag, n, e)
    
    print('Ciphertext: ', ciphertext)
    print('n: ', n)
    
    binary_p = "{0:b}".format(p)
    print('binary: ', binary_p[:117])
```

Clearly, `p` is given but in binary. Moreover, only the first 117 bits are given in contrast to the 133 bits `p` originally was.

So , we have to brute force for the remaining 16 bits, which is from 0 - 65535.I did bitwise or of those 16 bits with the 117 bits present in the original `Ciphertext` after right shifting the given 117 bits by 16 bits.

```py
p_first_part = (0b101100000110011110000000100011100100110000010010110111111100000101100110011000000110100111110101001010110001011000001) << 16

p = p_first_part | 0
for i in range(1,65536):
    p = p_first_part | i
    if isPrime(p) == True and n % p == 0:
        break
```

From there I took the candidate p and found the corresponding q as well

```py
q = n // p

print(n == p*q and isPrime(p) and isPrime(q))
```

After that I decrypted the rsa cipher as I have found the private keys `p` & `q` and found the following flag:

```
CTF_BD{53cR3t_R54_L00k1nG_W0W}
```

