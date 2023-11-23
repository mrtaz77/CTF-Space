from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import time


KEY_LEN = 16
BS = 16

date = "2023-11-01"
start_time = "17:09:00"
end_time = "17:11:00"

# Convert date and time to a timestamp
timestamp = int(time.mktime(time.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M:%S")))
end_timestamp = int(time.mktime(time.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M:%S")))

possible_seeds = []
while timestamp <= end_timestamp:
    possible_seeds.append(timestamp)
    timestamp += 1  # incrementing by 1 second

print(len(possible_seeds))

iv = "e49af1c15dad9962c45547b81414a399"
final = "c84a7c6245ebf7221ff60ec0541512b3a27c303c7302f9f85fa1aab9f53562e9e04ce4ace8cb7a09d875488dc9df4a61"

iv = bytes.fromhex(iv)
final = bytes.fromhex(final)

for seed in possible_seeds:
    random.seed(seed)

    key = bytes([random.randint(0, 255) for _ in range(KEY_LEN)])
    iv = bytes([random.randint(0, 255) for _ in range(BS)])

    cipher = AES.new(key, AES.MODE_CBC, iv)
    passwd = cipher.decrypt(final)

    try :
        msg = passwd.decode("utf8")
        print(seed)
        print(msg)
    except :
        continue