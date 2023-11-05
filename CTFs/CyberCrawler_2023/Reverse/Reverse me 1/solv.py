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

def actual_func(char):
    if 31 < ord(char) and ord(char) != 127:
            counter = ord(char) + 53
            return chr(counter + (counter // 95) * -95 + ord(' '))
    else:
        return char


# Example usage:
input_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_!@"
output_dict = []
for char in input_str:
    modified_char = actual_func(char)
    output_dict.append(modified_char)

# Write the character and corresponding output to out.txt
test_flag = "9)qh[L[hI[Ub?a[UWUAd\'=>Js"
flag = ""

for char in test_flag:
    i = 0
    for i in range(len(output_dict)):
        if output_dict[i] == char :
            flag += input_str[i]
            break

print(flag)

# decrypt = reverse_magic(output_str)
# print(decrypt)
