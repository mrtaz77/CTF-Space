from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import time

passwd = b"pass"

KEY_LEN = 16
BS = 16

time_s = int(time.time())


random.seed(time_s)

key = bytes([random.randint(0, 255) for _ in range(KEY_LEN)])
iv = bytes([random.randint(0, 255) for _ in range(BS)])

cipher = AES.new(key, AES.MODE_CBC, iv)
final = cipher.encrypt(pad(passwd, BS))

print(f"iv = {iv.hex()}")
print(f"final = {final.hex()}")
print(f"[Don't copy] key = {key.hex()}")
