# How should passwords be made?
## Category : Crypto
## Points : 200
![img](/CTFs/CyberColiseumII_2023/Crypto/How%20should%20passwords%20be%20made/description.png)

Downloading the task I worked through the [gen_pass.py](/CTFs/CyberColiseumII_2023/Crypto/How%20should%20passwords%20be%20made/gen_pass.py).
```py
KEY_LEN = 16
BS = 16

time_s = int(time.time())


random.seed(time_s)
```
Here the seed is *pseudo random*,i.e, the random function is using time as seed.However,not only the timestamp but also the place matters for estimating the seed accurately.

Then I saw the whatsapp ss.

![img](/CTFs/CyberColiseumII_2023/Crypto/How%20should%20passwords%20be%20made/whatsapp_chat.png)

This implies that :
Location : Lead,Moscow
Time of encryption : Between `5:09 pm` and `5:10 pm`.

Since the location is Moscow,which is `UTC+6:00`, I changed my local time zone accordingly...

![img](/CTFs/CyberColiseumII_2023/Crypto/How%20should%20passwords%20be%20made/change%20time%20zone.png)

Then I just generated timestamps(possible seeds) in the time frame betwen `5:08 pm` and `5:11 pm`,just to be on the safe side.Only __121__ possible seeds,so not many values to bruteforce.

From gen_pass.py, I understood it was an AES CBC encryption.So for each seed , I generated key-iv pair and decrypted the `final`.
```py
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
```

When the try portion executed without any error, I got the flag
```
CODEBY{P$eUdorAnDom_1S_d@ngEr0us}
```