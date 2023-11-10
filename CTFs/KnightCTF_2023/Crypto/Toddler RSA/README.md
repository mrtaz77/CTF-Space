# Toddler RSA
## Category : Crypto
You may have heard of baby RSA. But did you know that toddler RSA is a thing as well?

Demo Flag : KCTF{fl4g_h3r3}

Attachments: [Link](https://drive.google.com/file/d/1wRzK1eWa891SclKwkz_N9kb_5UB4-ejF/view)

__Solved post-ctf__

In [toddler_rsa](/CTFs/KnightCTF_2023/Crypto/Toddler%20RSA/toddler_rsa.py), we see right at the start the flag is split into two parts.
```py
flag1 = b"kctf{*****"
flag2 = b"******}"
```

The first part of the flag is encoded using rsa
```py
p, q = getPrime(512), getPrime(512)
n = p * q
e = 0x10001
phi = (p - 1) * (q - 1) 
m = bytes_to_long(flag1)
ct = pow(m, e, n)

primes = [p, q]

for _ in range(98):
    primes.append(getPrime(512))

random.shuffle(primes)
```

The random shuffle shuffles the private keys p,q with another 98 prime numbers.

For the second part,16 prime numbers are generated 
```py
primes2 = []

while True:
    if len(primes2) == 16:
        break
    p = getPrime(128)
    if p not in primes2:
        primes2.append(p)
```

After that , we generate the public key n2 which is a product of many prime numbers.We multiply prime numbers until n2 has a bit length greater than 1024

```py
while True:
    n2 = 1
    for p in primes2:
        r = random.randint(0, 1)
        if r:
            n2 *= p
    if n2.bit_length() > 1024:
        break
```

Next we simply encrypt flag2 using rsa and write all infos to [infos.txt](/CTFs/KnightCTF_2023/Crypto/Toddler%20RSA/infos.txt).

### Decrypting first part:

For 100 primes, we iterate for 100C2 pairs and check which pair is the required value of p,q. Only this pair gives the correct output , the flag. If the try portion executes without any error, then we have found the first part of the flag.
```py
for i in range(len(primes)):
    found = False
    for j in range(i + 1, len(primes)):
        p = primes[i]
        q = primes[j]
        n = p * q
        phi = (p - 1) * (q - 1)
        d = pow(e,-1,phi)
        msg = pow(ct1,d,n)
        try :
            msg = long_to_bytes(msg).decode('utf8')
            print(i,j)
            flag += msg
            found = True
            break
        except:
            continue
    if found:
        break
```
First part:
```
KCTF{rsa_and
```

### Decrypting second part:
In order to get the desired n2, we generate all possible candidates for n2 and store the indices of the primes whose product is equal to the candidate n2.The __generate_candidates__ function takes the list of primes and does this.

After that , we tried for each candidate n2 and its corresponding prime factors and using chinese remainder theorem cracked the rsa.If the try portion executes without any error, then we have found the second part of the flag.

Second part:
```
_only_rsa_ftw}
```

Entire Flag:
```
KCTF{rsa_and_only_rsa_ftw}
```

