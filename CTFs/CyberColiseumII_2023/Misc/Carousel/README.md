# Carousel
## Category : Misc
## Points : 200
The task contained a [task_file](/CTFs/CyberColiseumII_2023/Misc/Carousel/task_file.txt) . 

The file contained binary,hex and base64 encoded strings seperated by '|' seperator.

So I read the file, splitted based on '|' and used the appropriate decoding scheme.
```py
for i in range(len(inp)):
    if i % 3 == 0:
        e = "0b" + inp[i]
        out += str(chr(int(e,2))) # convert from binary to ascii
    elif i % 3 == 1:
        e = "0x" + inp[i]
        out += str(chr(int(e,16))) # convert from hexadecimal to ascii
    elif i % 3 == 2:
        e = base64.b64decode(inp[i]).decode("utf-8") # convert from binary to ascii
        out += e
```

Decoding gives the following message containing the flag:
```txt
Great job, buddy! Did you do it manually? In principle it doesn't matter.
Check out the lines: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
Take your flag - CODEBY{bin4ry_h3x_and_b4s3}. 
Thanks for passing and good luck in the next tasks.
```
