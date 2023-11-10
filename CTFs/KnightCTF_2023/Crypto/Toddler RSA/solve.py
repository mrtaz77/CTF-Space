from Crypto.Util.number import getPrime, bytes_to_long,long_to_bytes
import itertools,os

def generate_candidates(numbers):
    candidates = []
    indices = []

    # Generate all possible combinations of indices
    for r in range(0, len(numbers) + 1):
        for combination in itertools.combinations(range(len(numbers)), r):
            # Generate the candidate number using the chosen indices
            candidate = 1
            for index in combination:
                candidate *= numbers[index]

            # Check if the candidate number meets the bit length condition
            if candidate.bit_length() > 1024:
                candidates.append(candidate)
                indices.append(list(combination))

    return candidates, indices


def decrypt_message(n, c, e, primes):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    ts = []
    xs = []
    ds = []

    for i in range(len(primes)):
        ds.append(modinv(e, primes[i] - 1))

    m = primes[0]

    for i in range(1, len(primes)):
        ts.append(modinv(m, primes[i]))
        m = m * primes[i]

    for i in range(len(primes)):
        xs.append(pow((c % primes[i]), ds[i], primes[i]))

    x = xs[0]
    m = primes[0]

    for i in range(1, len(primes)):
        x = x + m * ((xs[i] - x % primes[i]) * (ts[i - 1] % primes[i]))
        m = m * primes[i]

    return long_to_bytes(x % n)

ct = 0
ct2 = 0
primes = []
primes2 = []

# Read the file
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "infos.txt")
with open(file_path, "r") as file:
    # Read the first integer and store it in ct
    ct1 = int(file.readline())

    # Read the second integer and store it in ct2
    ct2 = int(file.readline())


    # Read the next 100 numbers and store them in primes[]
    primes = list(map(int, file.readline().split()))

    # Read the next 16 numbers and store them in primes2[]
    primes2 = list(map(int, file.readline().split()))

e = 0x10001
flag = ""

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
    
# KCTF{rsa_and


candidates,indices = generate_candidates(primes2)
print(len(candidates))

for i in range(len(candidates)):
    n = candidates[i]
    primeInd = []
    for ind in indices[i]:
        primeInd.append(primes2[ind]) 
    
    decrypted_message = decrypt_message(n, ct2, e, primeInd)
    try:
        flag += decrypted_message.decode('utf8')
        print(i)
        print(indices[i])
        break
    except :
        continue

# _only_rsa_ftw}

print(flag)