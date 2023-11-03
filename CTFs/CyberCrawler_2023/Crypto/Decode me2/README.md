# DecodeMe 2
## Category : Crypto
## Points : 500(dynamic)
This time I have created another magical script. Can you break the magic ?

Attachments:
[link1](https://drive.google.com/drive/folders/13Ay3qE5Ku1yMQ6VwrY1_G1YiWZqifAgY?usp=sharing)

This time I wasted no time and gave the function to chatgpt.
```py
def doingMagic(text, monkey):
    spell = [[' ' for _ in range(len(text))] for _ in range(monkey)]
    magician_number = 1 
    abraka, dabra = 0, 0

    for char in text:
        spell[abraka][dabra] = char
        if abraka == 0:
            magician_number = 1
        elif abraka == monkey - 1:
            magician_number = -1
        abraka += magician_number
        dabra += 1

    magic_spell = ''.join(char for abraka in spell for char in abraka if char != ' ')
    return magic_spell
```


Although it did not give an exact interpretation of the function, it was able to give the undoing spell:
```py
def undoingMagic(magic_spell, monkey):
    spell_length = len(magic_spell)
    spell = [[' ' for _ in range(spell_length)] for _ in range(monkey)]
    magician_number = 1
    abraka, dabra = 0, 0

    for char in magic_spell:
        spell[abraka][dabra] = char
        if abraka == 0:
            magician_number = 1
        elif abraka == monkey - 1:
            magician_number = -1
        abraka += magician_number
        dabra += 1

    original_text = ''.join(char for abraka in spell for char in abraka if char != ' ')
    return original_text
```

which saddly did not work. But then I checked the output of magic function for `hello world` and got :
```cmd
Original Text: hello world
Magic Spell: hreollwdlo
```

which made me wonder whether this is just a simple __rail fence cipher__ with *5* rows or not.

The following code segment gave me the idea that the number of rows is 5.
```py
if __name__ == "__main__":
    plaintext = "hello world"
    monkey = 5

    magic_spell = doingMagic(plaintext, monkey)

    print("Original Text:", plaintext)
    print("Magic Spell:", magic_spell)
```
Here `monkey` = 5 is passed as a paramter to `magic_spell`

So I went to decode:
![img](/CTFs/CyberCrawler_2023/Crypto/Decode%20me2/ssOfSolv.png)

Flag : 
```
C3{1tS_alS0_eaSy_R1gh7}
```


