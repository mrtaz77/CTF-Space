from Crypto.Util.number import long_to_bytes , getPrime, inverse, bytes_to_long ,isPrime

n = 50057288776921281723975594148690987728601324019166931604097170720693481410035513

p_first_part = (0b101100000110011110000000100011100100110000010010110111111100000101100110011000000110100111110101001010110001011000001) << 16

# print(p_first_part)

p = p_first_part | 0
for i in range(1,65536):
    p = p_first_part | i
    if isPrime(p) == True and n % p == 0:
        break

q = n // p

# print(n == p*q and isPrime(p) and isPrime(q))

e = 65537

l = (p - 1) * (q - 1)
d = pow(e,-1,l)

c = 42215186860008813166236773400733103956726183177154610644607876116447486521133856

m = pow(c,d,n)

m = long_to_bytes(m)

print(m.decode('utf8'))