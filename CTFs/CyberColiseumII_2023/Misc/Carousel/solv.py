import base64
import os

inp = []

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "task_file.txt")


# Open a file for reading
with open(file_path, 'r') as file:
    # Read the file line by line
    for line in file:
        inp = line.strip().split("|") # strip() removes leading and trailing whitespaces

# print(inp)

out = ""
for i in range(len(inp)):
    if i % 3 == 0:
        e = "0b" + inp[i]
        out += str(chr(int(e,2)))
    elif i % 3 == 1:
        e = "0x" + inp[i]
        out += str(chr(int(e,16)))
    elif i % 3 == 2:
        e = base64.b64decode(inp[i]).decode("utf-8")
        out += e

print(out)
