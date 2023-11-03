# Problem : UnzipMe
## Category : Misc
## Points : 230

Can you unzip me ? :D

Attachments:
[link1](https://drive.google.com/drive/folders/15mKKauXfCTWgNFGVwLlVQ-get19KIpCw?usp=sharing)

The flag.zip is a large file.Unzipping it gave a flag.tar.gz.After that I got a .zip and .tar.gz files one after another.

So the challenge is basically a unzipping challenge of .zip and .tar.gz alternatively.

I initially got a py script from chatgpt.
```py
import zipfile
import tarfile
import gzip
import os

def unzip_file(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.tar.gz'):
                tar_file_path = os.path.join(os.path.dirname(zip_file_path), file_name)
                with open(tar_file_path, 'wb') as tar_file:
                    tar_file.write(zip_ref.read(file_name))
                with tarfile.open(tar_file_path, 'r:gz') as tar_ref:
                    tar_ref.extractall(os.path.dirname(zip_file_path))
                os.remove(tar_file_path)
            elif file_name.endswith('.gz'):
                gz_file_path = os.path.join(os.path.dirname(zip_file_path), file_name)
                with open(gz_file_path, 'wb') as gz_file:
                    gz_file.write(zip_ref.read(file_name))
                with gzip.open(gz_file_path, 'rb') as gz_ref:
                    with open(os.path.splitext(gz_file_path)[0], 'wb') as uncompressed_file:
                        uncompressed_file.write(gz_ref.read())
                os.remove(gz_file_path)
            else:
                extracted_file_path = os.path.join(os.path.dirname(zip_file_path), file_name)
                with open(extracted_file_path, 'wb') as extracted_file:
                    extracted_file.write(zip_ref.read(file_name))
    print("Extraction completed.")

if __name__ == "__main__":
    zip_file_path = input("Enter the path to the zip file: ")
    unzip_file(zip_file_path)
```

Alas ! I produced some bugs.At the end may be it would work but I found this [link](https://monliclican.medium.com/encryptctf2019-forensics-writeup-3f3930cae57d) helpful.

In the problem __Journey to the Center of the File 1__ there was a bash script which solved the problem where the flag was zipped and gzipped.

```bash
#!/bin/bash
# made with <3 by mon from hackstreetboys
mkdir staging
cp ziptunnel1.gz staging/
cd staging
for i in {1..1000}
do
    if [ $((i%2)) -eq 0 ]
    then
        gzip -df *
    else
        unzip *
        rm ziptunnel1 > /dev/null 2>&1
    fi
done
```

I modified the script for unzipping .tar.gz files.

```bash
#!/bin/bash

# Create the 'solv' folder if it doesn't exist
mkdir -p solv

# Copy the original file to the 'solv' folder
cp flag.zip solv/

# Change directory to 'solv'
cd solv

# Counter for iterations
iteration=1
while true; do
    # Check if the file exists
    if [ -f "flag.zip" ]; then
        if [ $((iteration%2)) -eq 0 ]; then
            # Even iteration: unzip the file
            unzip flag.zip > /dev/null 2>&1
        else
            # Odd iteration: extract .tar.gz file
            tar -xzf flag.tar.gz > /dev/null 2>&1
            # Remove the .tar.gz file
            rm flag.tar.gz > /dev/null 2>&1
        fi

        # Increment the iteration counter
        ((iteration++))
    else
        # No more files to unzip, break the loop
        break
    fi
done
```
After unzipping I got a `interesting.txt`.It contained the flag : 
```
C3{uNzip_iS_NoT_eaSy}
```

Well it is if you know