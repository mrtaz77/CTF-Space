# Reverse Me 1
## Category : Reverse
## Points : 500(dynamic)
Grab the flag from the given binary.

[Link 1](https://drive.google.com/drive/folders/1CRXCVdac8SgjacvO5k0BAUc_0FkA6dNg?usp=sharing)

I opened the binary in ghidra and went to the main function.

```c
int main(void){
    int iVar1;
    size_t sVar2;
    long in_FS_OFFSET;
    char input [264];
    long local_10;

    local_10 = *(long *)(in_FS_OFFSET + 40);
    printf("%s",
            "  ____  ______              _  ___   _ _____ _____ _    _ _______\n |  _ \\|  ____|     /\ \     | |/ / \\ | |_   _/ ____| |  | |__   __|\n | |_) | |__       /  \\    | \' /|  \\| |  | || |  __| |__| |  | |   \n |  _ <|  __|     / /\\ \\   |  < | . ` | | || | |_ |  __  |  |  |   \n | |_) | |____   / ____ \\  | . \\| |\\  |_| || |__| | |  | |  | |   \n |____/|_____ _| /_/    \\_\\ |_|\\_\\_| \\_|_____\\_____|_|  |_|  |_|   \n\n"
        );
    printf("Enter the flag: ");
    fgets(input,0x100,stdin);
    sVar2 = strcspn(input,"\n");
    input[sVar2] = '\0';
    magic(input);
    printWithTypingEffect("Doing magic...");
    fflush(stdout);
    usleep(1000000);
    putchar(0x2e);
    fflush(stdout);
    usleep(1000000);
    putchar(0x2e);
    fflush(stdout);
    usleep(1000000);
    puts(".");
    fflush(stdout);
    iVar1 = strcmp(input,"9)qh[L[hI[Ub?a[UWUAd\'=>Js");
    if (iVar1 == 0) {
    printWithTypingEffect("Congratulations! Submit the flag and get your reward.\n");
    }
    else {
    printWithTypingEffect("Sorry, you entered wrong flag.\n");
    }
    if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
    }
    return 0;
}
```

So the function at first takes user input using `fgets` into the buffer `input[264]`.After that the function `magic` modifies the buffer.
```c
magic(input);
```

After that the modified input buffer is matched with _"9)qh[L[hI[Ub?a[UWUAd\'=>Js"_ . If it is match , then the flag will be displayed.

So , I observed the `magic` function:
```c
void magic(long param_1)

{
  int counter;
  int i;
  
  for (i = 0; *(char *)(param_1 + i) != 0; i = i + 1) {
    if ((31 < *(char *)(param_1 + i)) && (*(char *)(param_1 + i) != 127)) {
      counter = *(char *)(param_1 + i) + 53;
      *(char *)(param_1 + i) = (char)counter + (char)(counter / 95) * -95 + ' ';
    }
  }
  return;
}

```

It is a simple function which loops through an array(param1 is casted to char*) and changes its contents.

In the [solv.py](/CTFs/CyberCrawler_2023/Reverse/Reverse%20me%201/pysolv.py), its equivalent in python:
```py
def magic(input_str):
    result = []
    for char in input_str:
        if 31 < ord(char) and ord(char) != 127:
            counter = ord(char) + 53
            result_char = chr(counter + (counter // 95) * -95 + ord(' '))
            result.append(result_char)
            print(ord(result_char),end=" ")
        else:
            result.append(char)
    return ''.join(result)
```

The main function which magic does is :
```py
 if 31 < ord(char) and ord(char) != 127:
            counter = ord(char) + 53
            result_char = chr(counter + (counter // 95) * -95 + ord(' '))
            result.append(result_char)
            print(ord(result_char),end=" ")
        else:
            result.append(char)
```

So I wrote it seperately in [solv.py](/CTFs/CyberCrawler_2023/Reverse/Reverse%20me%201/pysolv.py)

While solving, I mapped each candidate character of the flag and stored their output in a dictionary.Lastly by mapping in reverse for the expected flag, we get:

```
C3{reVerSe_lIke_a_Kn1GHT}
```